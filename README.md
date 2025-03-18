# Media Converter

動画、画像、音声の形式がバラバラな時、いちいちサイトを開いて「mp3 to wav」などと検索していませんか？
このスクリプトはこれらのファイルを相互に変換することができます。
ただ、ffmpegは必要です。

## 特徴
- **対応フォーマットの豊富さ**
  - **動画**: `mp4`, `mkv`, `avi`, `mov`, `flv`, `webm`, `h265`, `hevc`, `mpeg`, `mpg`, `3gp`, `wmv`, `asf`
  - **音声**: `mp3`, `aac`, `wav`, `flac`, `ogg`, `m4a`, `ac3`, `opus`, `amr`, `wma`
  - **画像**: `jpg`, `jpeg`, `png`, `gif`, `bmp`, `tiff`, `webp`
- **CLIインターフェースです**
- **動画から音声や画像の抽出ができる**
- **進捗バーで変換状況を確認できる**

## インストール方法
### 必要なツール
- Python3
- `ffmpeg` (先にインストールしておいて下さい)
- `tqdm` (インストールされていない場合は `pip install tqdm` で導入)

## 使い方
1. `python convert.py` を実行
2. メニューから`1. ファイル変換` を選択
3. 変換したいファイルを入力
4. 変換可能なフォーマットが表示されるので、希望のフォーマットを入力
5. 変換が完了すると、出力ファイルのパスが表示される

## 実行例
```sh
$ python convert.py

メニュー:
1. ファイル変換
2. 終了
選択してください: 1
変換するファイルを入力: sample.mp4
変換可能な形式: mp4, mkv, avi, mov, flv, webm, h265, hevc, mpeg, mpg, 3gp, wmv, asf
変換先の拡張子を入力: mkv
変換成功: sample.mkv
```

## ライセンス
GNU GPL 3.0
