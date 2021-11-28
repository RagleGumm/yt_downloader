"""Contains FileManager class to manage files downloaded by YtDownloader."""

import os


class FileManager:
    """
    Renames & deletes files processed by YtDownloader.

    Attributes:
        - cleaned_stream_title (str) - cleaned title
            of currently downloaded stream
    """

    def __init__(self):
        self.cleaned_stream_title = None

    def rename_file(self, file_ending: str):
        """
        Renames file using given file ending.

        Args:
            - file_ending - string that will be added at the end of file name
        """
        os.rename(
            f"{self.cleaned_stream_title}.mp4",
            f"{self.cleaned_stream_title}_{file_ending}.mp4",
        )

    def rename_file_to_video(self):
        """Adds 'video' ending to the name of the file."""
        self.rename_file(file_ending="video")

    def rename_file_to_audio(self):
        """Adds 'audio' ending to the name of the file."""
        self.rename_file(file_ending="audio")

    def delete_redundant_files(self):
        """Deletes files with _video.mp4/_audio.p4 ending."""
        os.remove(f"{self.cleaned_stream_title}_audio.mp4")
        os.remove(f"{self.cleaned_stream_title}_video.mp4")
