from PyQt5.QtWidgets import QWidget, QScrollArea, QGridLayout, QPushButton, QSizePolicy
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal

from Views.Elements import DBTablePartners
from loader import db


class PartnerWorkplace(QWidget):

    switch_to_create = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.b = QPushButton(text="Добавить нового партнера", parent=self)
        self.b.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.b.clicked.connect(self.create_partner)

        self.main_layout.addWidget(self.b, 1, 0, 1, 1)

        self.table = DBTablePartners(self)
        self.main_layout.addWidget(self.table, 2, 0, 6, 2)
        self.table.set_source(db)

    def create_partner(self):
        self.switch_to_create.emit()


