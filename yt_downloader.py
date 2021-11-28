"""Contains YtDownloader class for downloading YouTube videos."""

import pytube

from file_manager import FileManager


class YtDownloader:
    """
    Downloads YouTube videos using pytube library.
    Perfect for downloading old Italian horror movies.
    Works for Hammer movies as well.

    Offers two main methods:
        - download_joined_audio_video - downloads streams
            that contain audio & video in a single file,
        - download_audio_video_and_join - downloads audio & video track
            separately, then joins them, allows to obtain higher quality video

    Attributes:
        - stream_joiner (callable) - function used for joining
            audio & video track
        - file_manager (class instance) - instance of FileManager class,
        - links (list) - list of links (str) to be downloaded,
        - resolutions (list) - list of resolutions (str) that will be iterated
            to find best quality video
    """

    def __init__(
        self,
        stream_joiner: callable,
        file_manager: FileManager,
        links: list
    ):
        self.stream_joiner = stream_joiner
        self.file_manager = file_manager
        self.links = links
        self.resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']

    def download_stream(
        self,
        selected_stream,
        selected_resolution: str,
        yt,
    ):
        """
        Downloads selected stream.
        Prints basic info & progress.

        Args:
            - selected_stream (pytube.YouTube().streams.filter().first()) -
                YouTube stream selected for downloading
            - selected_resolution - best quality resolution available
                for selected stream
            - yt (pytube.YouTube())- core developer interface for pytube
        """
        print(yt.title)

        stream_type = selected_stream.type
        if stream_type == "video":
            print(f"{selected_resolution} resolution available")

        print(f"{stream_type} download started")
        selected_stream.download()
        print(f"{stream_type} download finished")

    def download_joined_audio_video(self):
        """
        Downloads streams that contain audio & video in a single file.
        Only resolution 720p and below available.
        """
        for link in self.links:
            # find all streams
            yt = pytube.YouTube(link)
            streams = yt.streams
            # find & download joined audio & video track
            for resolution in self.resolutions:
                selected_stream = streams.filter(
                    progressive=True, res=resolution
                ).first()
                if selected_stream:
                    self.download_stream(
                        selected_stream=selected_stream,
                        selected_resolution=resolution,
                        yt=yt
                    )
                    break

    def download_audio_video_and_join(self):
        """
        Downloads audio & video track separately,
            then joins them using stream_joiner.
        Allows to obtain higher quality than 720p if available.
        """
        for link in self.links:
            # find all streams
            yt = pytube.YouTube(link)
            streams = yt.streams

            # clean & save title in FileManager
            cleaned_title = yt.title.replace("/", "")
            self.file_manager.cleaned_stream_title = cleaned_title

            # find & download audio track, rename file
            selected_stream = streams.filter(
                only_audio=True, mime_type="audio/mp4", abr="128kbps"
            ).first()
            self.download_stream(
                selected_stream=selected_stream,
                selected_resolution=None,
                yt=yt
            )
            self.file_manager.rename_file_to_audio()

            # find & download video track
            for resolution in self.resolutions:
                selected_stream = streams.filter(
                    progressive=False, res=resolution
                ).first()

                # download if stream is found, rename file
                if selected_stream:
                    self.download_stream(
                        selected_stream=selected_stream,
                        selected_resolution=resolution,
                        yt=yt
                    )
                    self.file_manager.rename_file_to_video()

                    # join audio & video, delete redundant files, break
                    self.stream_joiner(stream_title=cleaned_title)
                    self.file_manager.delete_redundant_files()
                    break
