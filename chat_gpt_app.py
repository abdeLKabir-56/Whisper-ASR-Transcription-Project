# -*- coding: utf-8 -*-
"""chat_gpt_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cLJowI7mE7hyMhMD8cdKfWiyv_NuoL26
"""

pip install -U openai-whisper

pip install ffmpeg

import whisper

!pip install pytube
from pytube import YouTube

model = whisper.load_model("tiny")

pip install moviepy

pip install git+https://github.com/openai/whisper.git

#video hosted locally
from moviepy.editor import *
video = VideoFileClip("video.mp4")
video.audio.write_audiofile("myaudio.mp3")

#audio hosted in youtube
yt = YouTube('https://www.youtube.com/watch?v=Aq92xxwYwSU')

# Select the highest quality video
stream = yt.streams.get_highest_resolution()

# Download the video
video_path = stream.download()
video = VideoFileClip(video_path)
video.audio.write_audiofile("myaudio.mp3")

#trascribe the audio
result = model.transcribe("myaudio.mp3",fp16=False)
with open("mySound.txt","w") as file:
  file.write(result["text"])
print(result["text"])