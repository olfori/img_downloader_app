"""
Downloading images in a thread
"""
from PyQt5.QtCore import QThread, pyqtSignal

from .utils import download_img, get_name_from_url


class DownloadThread(QThread):
    """Class for downloading images in a thread """

    signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.img_path = ''
        self.url_list = []
        self.img_folder_path = ''

    def run(self) -> None:
        """
        Overriding the run method
        """
        for url in self.url_list:
            img_name = get_name_from_url(url)
            self.img_path = self.img_folder_path + img_name
            if download_img(url, self.img_path):
                self.signal.emit()
