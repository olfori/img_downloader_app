"""
Scroll area in the main window
"""
from PyQt5.QtWidgets import QScrollArea, QGroupBox, QFormLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import QRect

from .h_box import HBox
from .utils import get_filenames


class ScrollArea(QScrollArea):
    """Class ScrollArea for main window"""

    def __init__(self, parent: "MainWindow", imgs_path: str):
        super().__init__(parent)

        self.parent = parent
        size = parent.size()
        self.resize(size)

        img_names = get_filenames(imgs_path)

        self.formLayout = QFormLayout()
        groupBox = QGroupBox()

        for img_name in img_names:
            img_path = imgs_path + img_name
            self.formLayout.addRow(HBox(parent, img_path))
        groupBox.setLayout(self.formLayout)

        self.setWidget(groupBox)
        self.setWidgetResizable(True)

    def add_rows(self, img_path_list: list) -> None:
        """
        Adding multiple rows to scrollArea
        """
        for img_path in img_path_list:
            self.add_row(img_path)

    def add_row(self, img_path) -> None:
        """
        Adding one row to scrollArea
        """
        self.formLayout.addRow(
            HBox(self.parent, img_path)
        )
