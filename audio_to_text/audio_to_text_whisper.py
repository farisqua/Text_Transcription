
import os
import whisper
from langdetect import detect

# make txt and write to it
def txt_write(text, filename):
    with open(filename, "w") as file:
        file.write(text)

# File list <add audio file names to bulk process>
audio_list = [
    'Week_1',
    'Week_2',
    'Week_3',
    'Week_4',
    'Week_5',
    'Week_6',
    'Week_7'
]

# Transcription functions with language detect and write
def transcribe(audio_file):
    # Transcription
    model = whisper.load_model("base")
    result = model.transcribe(f"assets/{audio_file}.mp3")
    transcription = result["text"]

    # Language detect
    language = detect(transcription)
    print(f"Audio language: {language}")

    # Create and open a txt file with the text
    txt_write(transcription, f"{audio_file}_{language}.txt")

# Loop over audio_list file to process and export each
for file in audio_list:
    print(f"Opening {file} for transcription")
    transcribe(file)
    print(f"Successfuly wrote: {file} to txt")