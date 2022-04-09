from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QPushButton, QSizePolicy, QDateEdit, QComboBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal

from datetime import datetime

from Views import View
from loader import db


class CreateClient(View):

    switch_to_menu = pyqtSignal()

    def __init__(self, geometry):
        View.__init__(self, "CreateClient", geometry)

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.topper = QWidget(parent=self)
        self.topper.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.body = QWidget(parent=self)
        self.body.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.topper, 1, 1, 1, 1)
        self.main_layout.addWidget(self.body, 2, 1, 4, 1)

        self.topper_grid = QGridLayout()
        self.topper.setLayout(self.topper_grid)

        self.body_grid = QGridLayout()
        self.body.setLayout(self.body_grid)

        # Задаем элементы верхней части менюшки
        num = db.get_new_client_id()
        self.title = QLabel(text=f"Создание заказа №{str(num)}", parent=self.topper)
        self.topper_grid.addWidget(self.title, 1, 1, 1, 2)

        d = datetime.date(datetime.now())
        self.date = QLabel(text=f"Создан {d}", parent=self.topper)
        self.topper_grid.addWidget(self.date, 2, 1, 1, 1)

        self.saver = QPushButton(text="Сохранить", parent=self.topper)
        self.saver.clicked.connect(self.try_to_save)
        self.topper_grid.addWidget(self.saver, 1, 3, 1, 1)

        self.home = QPushButton(text="В меню", parent=self.topper)
        self.home.clicked.connect(self.go_home)
        self.topper_grid.addWidget(self.home, 1, 4, 1, 1)

        # теперь нижняя часть менюшки
        lab_flight_date = QLabel(text="Дата вылета", parent=self.body)
        self.body_grid.addWidget(lab_flight_date, 1, 1, 1, 1, alignment=Qt.AlignBottom)

        self.flight_date = QDateEdit(date=datetime.date(datetime.now()),
                                     minimumDate=datetime.date(datetime.now()),
                                     parent=self.body)
        self.body_grid.addWidget(self.flight_date, 2, 1, 1, 1)

        lab_return_date = QLabel(text="Дата прилета", parent=self.body)
        self.body_grid.addWidget(lab_return_date, 3, 1, 1, 1, alignment=Qt.AlignBottom)

        self.return_date = QDateEdit(date=datetime.date(datetime.now()),
                                     minimumDate=datetime.date(datetime.now()),
                                     parent=self.body)
        self.body_grid.addWidget(self.return_date, 4, 1, 1, 1)

        lab_country = QLabel(text="Страна", parent=self.body)
        self.body_grid.addWidget(lab_country, 5, 1, 1, 1, alignment=Qt.AlignBottom)

        self.country = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.country, 6, 1, 1, 1)

        lab_customer = QLabel(text="Покупатель", parent=self.body)
        self.body_grid.addWidget(lab_customer, 7, 1, 1, 1, alignment=Qt.AlignBottom)

        self.customer = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.customer, 8, 1, 1, 1)

        lab_flight = QLabel(text="Вылет", parent=self.body)
        self.body_grid.addWidget(lab_flight, 1, 2, 1, 1, alignment=Qt.AlignBottom)

        self.flight = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.flight, 2, 2, 1, 1)

        lab_status = QLabel(text="Статус", parent=self.body)
        self.body_grid.addWidget(lab_status, 3, 2, 1, 1, alignment=Qt.AlignBottom)

        self.status = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.status, 4, 2, 1, 1)

        lab_visa = QLabel(text="Виза", parent=self.body)
        self.body_grid.addWidget(lab_visa, 5, 2, 1, 1, alignment=Qt.AlignBottom)

        self.visa = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.visa, 6, 2, 1, 1)

        lab_profit = QLabel(text="Профит (только цифры)", parent=self.body)
        self.body_grid.addWidget(lab_profit, 7, 2, 1, 1, alignment=Qt.AlignBottom)

        self.profit = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.profit, 8, 2, 1, 1)

        lab_tour = QLabel(text="Тур. оператор", parent=self.body)
        self.body_grid.addWidget(lab_tour, 1, 3, 1, 1, alignment=Qt.AlignBottom)

        self.tour = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.tour, 2, 3, 1, 1)

        lab_bron = QLabel("Бронирование", parent=self.body)
        self.body_grid.addWidget(lab_bron, 3, 3, 1, 1, alignment=Qt.AlignBottom)

        self.bron = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.bron, 4, 3, 1, 1)

        lab_partner = QLabel(text="Партнер", parent=self.body)
        self.body_grid.addWidget(lab_partner, 5, 3, 1, 1, alignment=Qt.AlignBottom)

        try:
            self.partner = QComboBox(parent=self.body)
            parts = db.get_partners_options()
            for i in parts:
                self.partner.addItem(i[1], userData=i[0])
        except Exception as e:
            print(e)
        self.body_grid.addWidget(self.partner, 6, 3, 1, 1)

        lab_deposit = QLabel(text="Депозит", parent=self.body)
        self.body_grid.addWidget(lab_deposit, 7, 3, 1, 1, alignment=Qt.AlignBottom)

        self.deposit = QLineEdit(parent=self.body)
        self.body_grid.addWidget(self.deposit, 8, 3, 1, 1)

    def go_home(self):
        self.switch_to_menu.emit()

    def try_to_save(self):
        part_flight_date = self.flight_date.date()
        part_return_date = self.return_date.date()
        try:
            flight_date = datetime.date(datetime.now())
            return_date = datetime.date(datetime.now())
        except Exception as e:
            print(e)

        flight_date = flight_date.replace(day=part_flight_date.day(),
                                          month=part_flight_date.month(),
                                          year=part_flight_date.year())

        return_date = return_date.replace(day=part_return_date.day(),
                                          month=part_return_date.month(),
                                          year=part_return_date.year())

        part_flight = self.flight.text()
        part_country = self.country.text()
        part_status = self.status.text()
        part_visa = self.visa.text()
        part_customer = self.customer.text()
        part_tour = self.tour.text()
        part_bron = self.bron.text()
        part_partner = self.partner.currentText()
        part_partner_data = self.partner.currentData()
        part_profit = self.profit.text()
        part_deposit = self.deposit.text()

        obj = [self.flight, self.country, self.visa, self.status,
               self.customer, self.tour, self.bron, self.profit,
               self.deposit]
        can_add = True
        for i in obj:
            if i.text() == "":
                can_add = False
                with open("Styles/lineempty.txt", "r") as st:
                    i.setStyleSheet(st.read())
            else:
                with open("Styles/lineok.txt", "r") as st:
                    i.setStyleSheet(st.read())

        if can_add:
            try:
                part_per = float(part_profit)
                part_deposit = float(part_deposit)
                db.add_client([flight_date, str(part_flight), str(part_country),
                               str(part_status), str(part_visa), str(part_tour),
                               return_date, int(part_partner_data), str(part_bron), str(part_customer),
                               float(part_deposit), float(part_profit)])
                self.switch_to_menu.emit()
            except Exception as e:
                print("Percent and deposit MUST BE digits ONLY!")







