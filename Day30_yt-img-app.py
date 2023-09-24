import streamlit as st

st.title('🖼️yt-img-app')
st.header('Youtube Thumbnail Image Extractor App')

with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image from a YouTube video.')

#画像設定
st.sidebar.header('Settings')
img_dict={'Max':'maxresdefault','High':'hqdefault','Medium':'mqdefault','Standard':'sddefault'}
selected_img_quality= st.sidebar.selectbox('Select image quality',['Max','High','Medium','Standard'])
img_quality= img_dict[selected_img_quality]

#YoutubeURLと区切り位置設定
yt_url=st.text_input('Paste YouTube URL','https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
    if 'youtu.be' in input_url:
        ytid = input_url.split('/')[-1]
    if 'youtube.com' in input_url:
        ytid = input_url.split('=')[-1]
    return ytid

#Youtubeサムネイル画像設定
if yt_url != '':
    ytid = get_ytid(yt_url)
    
    yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
    st.image(yt_img)
    st.write('Youtube video thumbnail image URL: ', yt_img)
else:
    st.write('☝️Enter URL to continue ...')