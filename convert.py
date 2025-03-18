import os
import ffmpeg
import re
import sys
import subprocess
from tqdm import tqdm
import time

def get_media_type(extension):
    video_exts = {"mp4", "mkv", "avi", "mov", "flv", "webm", "h265", "hevc", "mpeg", "mpg", "3gp", "wmv", "asf"}
    audio_exts = {"mp3", "aac", "wav", "flac", "ogg", "m4a", "ac3", "opus", "amr", "wma"}
    image_exts = {"jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"}
    
    if extension in video_exts:
        return "video"
    elif extension in audio_exts:
        return "audio"
    elif extension in image_exts:
        return "image"
    return None

def get_convertible_formats(media_type):
    if media_type == "video":
        return ["mp4", "mkv", "avi", "mov", "flv", "webm", "h265", "hevc", "mpeg", "mpg", "3gp", "wmv", "asf"]
    elif media_type == "audio":
        return ["mp3", "aac", "wav", "flac", "ogg", "m4a", "ac3", "opus", "amr", "wma"]
    elif media_type == "image":
        return ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]
    return []

def loading_animation(message):
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.25)
        print(".", end="", flush=True)
    print()

def convert_file(input_file, output_ext):
    output_file = os.path.splitext(input_file)[0] + "." + output_ext
    try:
        loading_animation("変換準備中")
        media_type = get_media_type(os.path.splitext(input_file)[1][1:].lower())
        
        if media_type == "video" or media_type == "audio":
            probe = ffmpeg.probe(input_file)
            duration = float(probe["format"]["duration"])

            process = subprocess.Popen(
                ["ffmpeg", "-i", input_file, output_file, "-y", "-progress", "pipe:1", "-v", "error"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True
            )

            pbar = tqdm(total=duration, unit="sec", desc="変換中")

            for line in process.stdout:
                match = re.search(r"out_time_ms=(\d+)", line)
                if match:
                    current_time = int(match.group(1)) / 1_000_000
                    pbar.update(current_time - pbar.n)

            process.wait()
            pbar.close()

        elif media_type == "image":
            process = subprocess.run(["ffmpeg", "-i", input_file, output_file, "-y"], capture_output=True, text=True)
        
        if process.returncode == 0:
            print(f"変換成功: {output_file}")
        else:
            print("変換エラーが発生しました")

    except ffmpeg.Error as e:
        print("変換エラー:", e)

def main():
    while True:
        print("\nメニュー:")
        print("1. ファイル変換")
        print("2. 終了")
        choice = input("選択してください: ")
        
        if choice == "1":
            input_file = input("変換するファイルを入力: ")
            
            if not os.path.exists(input_file):
                print("ファイルが見つかりません。")
                continue
            
            ext = os.path.splitext(input_file)[1][1:].lower()
            media_type = get_media_type(ext)
            
            if not media_type:
                print("動画、音声、または画像ファイルではありません。")
                continue
            
            formats = get_convertible_formats(media_type)
            print("変換可能な形式:", ", ".join(formats))
            
            output_ext = input("変換先の拡張子を入力: ")
            
            if output_ext not in formats:
                print("無効な拡張子です。")
                continue
            
            convert_file(input_file, output_ext)
        
        elif choice == "2":
            print("終了します。")
            break
        else:
            print("無効な選択です。")
    
if __name__ == "__main__":
    main()