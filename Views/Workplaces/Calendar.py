from PyQt5.QtWidgets import QWidget, QTableWidget, QComboBox, QSpinBox, QGridLayout, QSizePolicy

from Views.Elements import CalendarDBTable
from loader import db
from datetime import datetime


class CalendarSpace(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.main_layout = QGridLayout()

        self.months = QComboBox(parent=self)
        self.months.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        monthes = ["Январь", "Февраль", "Март", "Апрель", "Май",
                   "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                   "Ноябрь", "Декабрь"]
        for i in range(len(monthes)):
            self.months.addItem(monthes[i], userData=str(i + 1))
        month_index = datetime.now().month
        self.months.setCurrentIndex(month_index - 1)
        self.months.currentIndexChanged.connect(self.change_date_info)

        self.years = QSpinBox(parent=self)
        self.years.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.years.setMinimum(2003)
        self.years.setMaximum(2100)
        self.years.setValue(datetime.now().year)
        self.years.valueChanged.connect(self.change_date_info)

        self.main_layout.addWidget(self.months, 1, 2, 1, 1)
        self.main_layout.addWidget(self.years, 1, 3, 1, 1)

        self.table = CalendarDBTable(self)
        self.table.set_source(db)
        self.main_layout.addWidget(self.table, 2, 1, 6, 4)
        self.table.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.setLayout(self.main_layout)
        self.change_date_info()

    def change_date_info(self):
        month = int(self.months.currentData())
        year = int(self.years.value())
        self.table.update_values(month, year)
