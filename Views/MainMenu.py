from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy

from Views import View
from Views.Bars import MainBar
from Views.Workplaces import PartnerWorkplace, ClientsWorkplace, CreatePartner, CalendarSpace


class MainMenu(View):

    switch_to_create_client = pyqtSignal()
    switch_exit = pyqtSignal()

    def __init__(self, geometry=None, login="user"):
        View.__init__(self, "MainMenu", geometry)
        self.setWindowTitle('Main Window')

        self.layout = QGridLayout()
        self.workplace = None

        self.bar = MainBar(self)
        self.bar.set_login(login)
        self.bar.switch_exit.connect(self.emit_exit)
        self.layout.addWidget(self.bar, 0, 0, 1, 1)
        self.bar.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #layout.addWidget(self.widget, 1, 0, 1, 1)
        #layout.addWidget(self.button, 1, 0, 2, 1)

        self.setLayout(self.layout)
        self.connect_menu_signals()
        self.open_partners()

    def switch(self):
        self.switch_window.emit()

    def connect_menu_signals(self):
        self.bar.get_partners_signal().connect(self.open_partners)
        self.bar.get_clients_signal().connect(self.open_clients)
        self.bar.switch_to_create_client.connect(self.switch_to_client)
        self.bar.switch_to_calendar.connect(self.open_calendar)

    def open_clients(self):
        if self.workplace:
            self.workplace.close()
        self.workplace = ClientsWorkplace(self)
        self.layout.addWidget(self.workplace, 1, 0, 4, 1)

    def open_partners(self):
        if self.workplace:
            self.workplace.close()
        self.workplace = PartnerWorkplace(self)
        self.workplace.switch_to_create.connect(self.create_partner_menu)
        self.layout.addWidget(self.workplace, 1, 0, 4, 1)

    def open_calendar(self):
        if self.workplace:
            self.workplace.close()
        self.workplace = CalendarSpace(self)
        self.layout.addWidget(self.workplace, 1, 0, 4, 1)

    def create_partner_menu(self):
        self.workplace.close()
        try:
            self.workplace = CreatePartner(self)
            self.workplace.on_added_partner.connect(self.open_partners)
        except Exception as e:
            print(e)
        self.layout.addWidget(self.workplace, 1, 0, 4, 1)

    def switch_to_client(self):
        self.switch_to_create_client.emit()

    def emit_exit(self):
        self.switch_exit.emit()

