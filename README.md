# YtDownloader

## Description

Class for downloading YouTube videos using pytube library.<br>
Perfect for downloading old Italian horror movies.<br>
Works for Hammer movies as well.<br>

Offers two main methods:
- download_joined_audio_video - downloads streams that contain audio & video in a single file,
- download_audio_video_and_join - downloads audio & video track separately, then joins them, allows to obtain higher quality video.

## Requirements

Install with pip:

```
pip install -r requirements.txt
```

Windows: requires also installation of ffmpeg

## Quickstart

```python
from yt_downloader import YtDownloader
from file_manager import FileManager
from stream_joiner import ffmpeg_joiner

# instantiate FileManager, define links to download
file_manager = FileManager()
streams_to_download = [
    "https://www.youtube.com/watch?v=9-BOoO7AYK0",
    "https://www.youtube.com/watch?v=JKV7WUM-Ots",
]

# instantiate YtDownloader, download streams
yt_downloader = YtDownloader(
    stream_joiner=ffmpeg_joiner,
    file_manager=file_manager,
    links=streams_to_download
)
yt_downloader.download_joined_audio_video()
```

