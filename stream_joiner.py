"""Contains functions used for joining of audio & video streams."""

import ffmpeg


def ffmpeg_joiner(stream_title: str):
    """
    Joins files with audio & video tracks of a given stream_title using ffmpeg.

    Args:
        - stream_title - title of the stream appearing in file names
    """
    audio_path = f"{stream_title}_audio.mp4"
    audio_stream = ffmpeg.input(filename=audio_path)
    video_path = f"{stream_title}_video.mp4"
    video_stream = ffmpeg.input(filename=video_path)
    output_file_name = f"{stream_title}.mp4"

    print("started joining audio & video stream")
    ffmpeg.output(audio_stream, video_stream, output_file_name).run(quiet=True)
    print("finished joining audio & video stream")
