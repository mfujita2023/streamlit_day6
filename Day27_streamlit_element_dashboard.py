import json
import streamlit as st
from pathlib import Path

#Streamlit Elementsでは、これらすべてのオブジェクトが必要になります。
from streamlit_elements import elements, dashboard,mui,editor,media,lazy,sync,nivo

#ダッシュボードがページ全体を占めるように、ページレイアウトを変更します。
#memo sidebarは左側の選択用の画面
with st.sidebar:
    st.title("🗓️30DaysOfStreamlit")
    st.header("Day27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    #YoutubeのURL
    media_url= st.text_input("Media URL",value="https//www.youtube.com/watch?v=vIQQR_yq-8I")

#コードエディターとチャートのデフォルトデータを初期化します。

#以下に示すように、このセッション状態の項目はコードエディターが変更されると更新され、
# Nivoバンプチャートがそれを読み取ってデータを描画します。
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

#デフォルトのダッシュボードレイアウトを定義します。
#ダッシュボードグリッドはデフォルトで12列あります。

layout = [
    dashboard.Item("editor", 0, 0, 6, 3),
    dashboard.Item("chart", 6, 0, 6, 3),
    dashboard.Item("media", 0, 6, 12, 4),
]

with elements("demo"):

    #上記で指定したレイアウトで新しいダッシュボードを作成します。
    #
    # draggableHandleは、各ダッシュボード項目のドラッグ可能な部分を定義するCSSクエリセレクターです。
    #ここでは、クラス名に「draggable」を含む要素がドラッグ可能になります。
     
    with dashboard.Grid(layout,draggableHandle=".draggable"):
        #最初のカードはコードエディターです。
        #
        #「key」パラメーターを使って、正しいダッシュボード項目を特定します。
        #カードのコンテンツが自動的に利用可能な高さになるようにするには、CSS Flexboxを使用します。 
        with mui.Card(key = "editor",sx={"display":"flex","flexDirection":"column"}):
 
            #このヘッダーをドラッグ可能にするには、上記のdashboard.GridのdraggableHandleで定義したように、
            #クラス名を「draggable」に設定する必要があります。           
            mui.CardHeader(title="Editor",className="draggable")

            # flex CSS値を1に設定することで、カードのコンテンツをすべて利用可能な高さにします。
            #また、minHeightを0に設定することで、カードを縮小するとカードのコンテンツも縮小されるようにします。
            with mui.CardContent(sx={"flex":1,"minHeight":0}):
            
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )
            with mui.CardActions:
                # Monacoエディターでは、onChangeに遅延コールバックをバインドしているため、
                # Monacoのコンテンツを変更しても、Streamlitには直接通知されず、毎回再読み込みされることはありません。
                #そのため、更新をトリガーするための遅延しない別のイベントが必要です。          
                mui.Button("Apply changes", onClick=sync())
        
        
        #Chart画面
        with mui.Card(key="chart",sx={"display":"flex","flexDirection":"column"}):
            mui.CardHeader(title="Chart",className="draggable")

            with mui.CardContent(sx={"flex":1,"minHeight":0}):
                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={"scheme":"spectral"},
                    linewidth=3,
                    activelinewidth=6,
                    inactivelinewidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={"theme":"background"},
                    activePointBorderWidth=3,
                    pointBorderwidth=3,
                    pointBorderColor={"from":"serie.color"},
                    
                    axisTop={
                        "tickSize":5,
                        "tickPadding":5,
                        "tickRotation":0,
                        "legend":"",
                        "legendPosition":"middle",
                        "legendOffset":-36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },  
                    margin={"top":40,"right":100,"bottom":40,"left":60},
                    axisRight=None,
                )

        with mui.Card(key="media",sx={"display":"flex","flexDirection":"column"}):
            mui.CardHeader(title="Media Player",className="draggable")
            with mui.CardContent(sx={"flex":1,"minHeight":0}):
                media.Player(url=media_url,width="100%",height="100%",controls=True)
