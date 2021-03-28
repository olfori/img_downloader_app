"""
Main Window
"""
import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from collection.scroll_area import ScrollArea
from collection.utils import delete_last_element
from collection.download_thread import DownloadThread


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_FOLDER = os.path.join(CURRENT_DIR, 'img/')


class MainWindow(QMainWindow):
    """Class Main Window"""

    def __init__(self):
        super().__init__()

        uic.loadUi('design.ui', self)

        self.scrollArea = ScrollArea(self.widget_3, IMG_FOLDER)

        self.addButton.clicked.connect(self.click_addButton)
        self.downloadButton.clicked.connect(self.click_downloadButton)
        self.textEdit.setReadOnly(True)

        self.dt = DownloadThread()
        self.dt.img_folder_path = IMG_FOLDER
        self.dt.signal.connect(self.on_download_img)

        self.setWindowTitle('App img downloader')
        self.show()

    def click_addButton(self) -> None:
        """
        If addButton was clicked
        """
        url = self.lineEdit.text()
        if url == '':
            return
        self.lineEdit.clear()
        url = f'{url}\n'
        self.textEdit.insertPlainText(url)

    def get_url_list(self) -> list:
        """
        Return list of urls from textEdit
        """
        return self.textEdit.toPlainText().split('\n')

    def click_downloadButton(self) -> None:
        """
        If downloadButton was clicked
        """
        url_list = self.get_url_list()
        if len(url_list) < 2:
            return

        url_list = delete_last_element(url_list)

        self.dt.url_list = url_list
        self.dt.start()

    def on_download_img(self) -> None:
        """
        When one image was downloaded
        """
        img_path = self.dt.img_path
        self.scrollArea.add_row(img_path)
        self.cut_last_line()

    def cut_last_line(self) -> None:
        """
        Method deletes the last line in the textEdit element
        """
        url_list = self.get_url_list()
        if len(url_list) < 2:
            return
        self.textEdit.clear()

        url_list = delete_last_element(url_list, 2)
        urls_text = '\n'.join(url_list) + '\n'

        self.textEdit.setText(urls_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
