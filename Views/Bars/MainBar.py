from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QSizePolicy
from PyQt5.QtCore import pyqtSignal


class MainBar(QWidget):

    switch_to_create_client = pyqtSignal()
    switch_to_partners = pyqtSignal()
    switch_to_clients = pyqtSignal()
    switch_to_calendar = pyqtSignal()
    switch_exit = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.setObjectName("DarkTopper")
        self.style().unpolish(self)
        self.style().polish(self)

        main_layout = QGridLayout()

        self.picture = QPushButton("Картинка типа", self)
        self.picture.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.login = QPushButton("Логин типа", self)
        self.login.clicked.connect(self.emit_exit)
        self.login.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.create = QPushButton("Создать", self)
        self.create.setObjectName("GreenButton")
        self.create.clicked.connect(self.emit_create_client)
        self.create.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.clients = QPushButton("Клиенты", self)
        self.clients.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.clients.clicked.connect(self.emit_clients)

        self.partners = QPushButton("Партнеры", self)
        self.partners.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.partners.clicked.connect(self.emit_partners)

        self.calendar = QPushButton("Календарь", self)
        self.calendar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.calendar.clicked.connect(self.emit_calendar)

        main_layout.addWidget(self.picture, 0, 0, 1, 1)
        main_layout.addWidget(self.login, 0, 3, 1, 1)
        main_layout.addWidget(self.create, 1, 0, 1, 1)
        main_layout.addWidget(self.clients, 1, 1, 1, 1)
        main_layout.addWidget(self.partners, 1, 2, 1, 1)
        main_layout.addWidget(self.calendar, 1, 3, 1, 1)

        self.setLayout(main_layout)

    def set_login(self, val):
        self.login.setText(val)

    def get_partners_signal(self):
        return self.switch_to_partners

    def get_clients_signal(self):
        return self.switch_to_clients

    def get_calendar_signal(self):
        return self.switch_to_calendar

    def emit_partners(self):
        self.switch_to_partners.emit()

    def emit_clients(self):
        self.switch_to_clients.emit()

    def emit_calendar(self):
        self.switch_to_calendar.emit()

    def emit_create_client(self):
        self.switch_to_create_client.emit()

    def emit_exit(self):
        self.switch_exit.emit()

