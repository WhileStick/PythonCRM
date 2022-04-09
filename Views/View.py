from PyQt5.QtWidgets import QWidget

from Config import view_config


class View(QWidget):

    def __init__(self, name="", geometry=None):
        QWidget.__init__(self)
        self.name = name
        self.setObjectName(self.name)
        self.style().unpolish(self)
        self.style().polish(self)
        self.setGeometry(geometry) if geometry else self.setGeometry(view_config.WINDOW_GEOMETRY)
        #print(f"{self.name} geometry on init {self.geometry()}")

    def get_geometry(self):
        #print(f"{self.name} geometry {self.geometry()}")
        return self.geometry()

