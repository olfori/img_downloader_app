"""
One row in a scroll area
"""
from PyQt5.QtWidgets import QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap

from .utils import get_img_name_size


class HBox(QHBoxLayout):
    """Class create one row in a scroll area"""

    def __init__(self, parent, img_path):
        super().__init__()

        pixmap = QPixmap(img_path)
        pixmap = pixmap.scaled(100, 100)

        labelImg = QLabel(parent)
        labelImg.setPixmap(pixmap)
        labelImg.resize(100, 100)

        img_name, img_size = get_img_name_size(img_path)

        labelName = QLabel(parent)
        labelName.setText(img_name)

        labelSize = QLabel(parent)
        labelSize.setText(img_size)

        self.addWidget(labelImg)
        self.addWidget(labelName)
        self.addWidget(labelSize)
