from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QPushButton, QSizePolicy
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal

from loader import db


class CreatePartner(QWidget):

    on_added_partner = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.main_layout = QGridLayout()

        self.name_lab = QLabel(parent=self, text="Название")
        self.name = QLineEdit(parent=self, maxLength=255)

        self.fin_lab = QLabel(parent=self, text="Финансы")
        self.fin = QLineEdit(parent=self, maxLength=255)

        self.cont_lab = QLabel(parent=self, text="Контакты")
        self.cont = QLineEdit(parent=self, maxLength=255)

        self.acc_lab = QLabel(parent=self, text="Доступ")
        self.acc = QLineEdit(parent=self, maxLength=255)

        self.brand_lab = QLabel(parent=self, text="Бренд")
        self.brand = QLineEdit(parent=self, maxLength=255)

        self.per_lab = QLabel(parent=self, text="% (только число)")
        self.per = QLineEdit(parent=self, maxLength=255)

        self.deposit_lab = QLabel(parent=self, text="Депозит (только число)")
        self.deposit = QLineEdit(parent=self, maxLength=255)

        self.create = QPushButton(parent=self, text="Добавить партнера")
        self.create.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.create.clicked.connect(self.check_input)

        self.main_layout.addWidget(self.create, 1, 1, 1, 3)

        self.main_layout.addWidget(self.name_lab, 2, 1, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.name, 3, 1, 1, 1)
        self.name.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.fin_lab, 2, 2, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.fin, 3, 2, 1, 1)
        self.fin.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.cont_lab, 2, 3, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.cont, 3, 3, 1, 1)
        self.cont.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.acc_lab, 4, 1, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.acc, 5, 1, 1, 1)
        self.acc.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.brand_lab, 4, 3, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.brand, 5, 3, 1, 1)
        self.brand.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.per_lab, 6, 1, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.per, 7, 1, 1, 1)
        self.per.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.main_layout.addWidget(self.deposit_lab, 6, 3, 1, 1, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.deposit, 7, 3, 1, 1)
        self.deposit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.setLayout(self.main_layout)

    def check_input(self):
        part_name = self.name.text()
        part_fin = self.fin.text()
        part_cont = self.cont.text()
        part_acc = self.acc.text()
        part_brand = self.brand.text()
        part_per = self.per.text()
        part_deposit = self.deposit.text()

        obj = [self.name, self.fin, self.cont, self.acc,
               self.brand, self.per, self.deposit]
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
                part_per = float(part_per)
                part_deposit = float(part_deposit)
                db.add_partner([str(part_name), str(part_fin), str(part_cont),
                            str(part_acc), str(part_brand), part_per,
                            part_deposit])
                self.on_added_partner.emit()
            except Exception as e:
                print("Percent and deposit MUST BE digits ONLY!")




