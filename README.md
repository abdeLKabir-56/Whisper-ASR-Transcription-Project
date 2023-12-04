
# Whisper ASR Transcription Project

## Overview

This project utilizes the Whisper Automatic Speech Recognition (ASR) model developed by OpenAI to transcribe audio from both a locally hosted video and a YouTube video. The transcription results are saved as text files for further analysis.

## Dependencies

- [OpenAI Whisper](https://github.com/openai/whisper): A powerful ASR model for transcribing speech.
- [pytube](https://github.com/pytube/pytube): A lightweight, dependency-free Python library to download YouTube videos.
- [moviepy](https://zulko.github.io/moviepy/): A video editing library for Python.
- [ffmpeg](https://ffmpeg.org/): A multimedia framework to handle audio and video processing.

## Usage

1. Install the required dependencies:

    ```bash
    pip install -U openai-whisper
    pip install ffmpeg
    pip install pytube
    pip install moviepy
    ```

2. Load the Whisper ASR model:

    ```python
    import whisper
    model = whisper.load_model("tiny")
    ```

3. Run the provided Python script:

    - **Local Video Transcription:**

        ```python
        from moviepy.editor import VideoFileClip
        video = VideoFileClip("video.mp4")
        video.audio.write_audiofile("myaudio.mp3")

        result_local = model.transcribe("myaudio.mp3", fp16=False)
        with open("mySound_local.txt", "w") as file:
            file.write(result_local["text"])
        print(result_local["text"])
        ```

    - **YouTube Video Transcription:**

        ```python
        from pytube import YouTube
        yt = YouTube('https://www.youtube.com/watch?v=Aq92xxwYwSU')

        stream = yt.streams.get_highest_resolution()
        video_path = stream.download()

        video_youtube = VideoFileClip(video_path)
        video_youtube.audio.write_audiofile("myaudio.mp3")

        result_youtube = model.transcribe("myaudio.mp3", fp16=False)
        with open("mySound_youtube.txt", "w") as file:
            file.write(result_youtube["text"])
        print(result_youtube["text"])
        ```

4. Analyze the transcriptions saved in the generated text files (`mySound_local.txt` and `mySound_youtube.txt`).
