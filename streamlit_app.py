import streamlit as st
import pandas as pd
import numpy as np

st.title("""pi value""")
df = pd.DataFrame(np.random.randn(50,20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)

st.image('Data/aloo.gif')

with st.sidebar:
    st.image('Data/monkey.gif')
    st.image('Data/panda.jpg')

col1, col2, col3 , col4 = st.columns(4)

with col1:
   st.header("A pandas")
   st.image("Data/panda.jpg")

with col2:
   st.header("A monkey")
   st.image('Data/monkey.gif')

with col3:
   st.header("Devil")
   st.image('Data/WhatsApp Image 2024-02-06 at 11.20.14 AM.jpeg')

with col4:
    st.header("Gaonwala")
    st.image('Data/WhatsApp Image 2024-02-06 at 11.22.29 AM.jpeg')

'''audio_file = open('Data/goku-kamehameha-wave-6988.mp3')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')
sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)'''

audio_file = open('Data/hello.oga', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

st.image('Data/ItachiUchiha.jpg')
st.snow()

video_file = open('Data/Naruto vs Sasuke kokuten.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)