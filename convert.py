import os
import argparse
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_folder, wav_folder):
    if not os.path.exists(wav_folder):
        os.mkdir(wav_folder)    
    for file in os.listdir(mp3_folder):
        if file.endswith(".mp3"):
            mp3_path = os.path.join(mp3_folder, file)
            wav_path = os.path.join(wav_folder, os.path.splitext(file)[0] + ".wav")
            sound = AudioSegment.from_mp3(mp3_path)
            sound.export(wav_path, format="wav")
            print(f"Converted {mp3_path} to {wav_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert MP3 audio clips to WAV format')
    parser.add_argument('mp3_folder', type=str, help='The folder containing the MP3 files')
    parser.add_argument('wav_folder', type=str, help='The folder to save the converted WAV files')
    args = parser.parse_args()
    convert_mp3_to_wav(args.mp3_folder, args.wav_folder)