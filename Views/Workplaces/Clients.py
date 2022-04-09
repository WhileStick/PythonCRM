from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QPushButton, QSizePolicy, QGridLayout, QLabel
from PyQt5.Qt import Qt

from Views.Elements import DBTableClients
from loader import db


class ClientsWorkplace(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.table = DBTableClients(self)
        self.main_layout.addWidget(self.table)
        self.table.set_source(db)


