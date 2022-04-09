from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.Qt import Qt

from datetime import date
from calendar import monthrange


class DBTable(QTableWidget):

    def __init__(self, parent):
        QTableWidget.__init__(self, parent=parent)
        self.source = None

    def set_source(self, db):
        self.source = db
        pass


class DBTableClients(DBTable):

    def __init__(self, parent):
        DBTable.__init__(self, parent=parent)

    def set_source(self, db):
        super().set_source(db)
        titles = ["№", "Дата вылета", "Вылет", "Страна", "Статус", "Виза", "Тур Оператор",
                  "Дата прилета", "Партнер", "Бронирование", "Покупатель",
                  "Депозит", "Профит"]

        data = db.get_all_clients()
        self.setRowCount(len(data)+1)
        self.setColumnCount(len(titles))

        for i in range(len(titles)):
            self.setItem(0, i, QTableWidgetItem(titles[i]))

        for i in range(len(data)):
            for item in range(0, len(data[i])):
                self.setItem(i+1, item, QTableWidgetItem(str(data[i][item])))


class DBTablePartners(DBTable):

    def __init__(self, parent):
        DBTable.__init__(self, parent=parent)

    def set_source(self, db):
        super().set_source(db)
        titles = ["ID", "Название", "Финансы", "Контакты", "Доступ", "Бренд", "%",
                  "Депозит"]

        data = db.get_all_partners()
        self.setRowCount(len(data)+1)
        self.setColumnCount(len(titles))

        for i in range(len(titles)):
            self.setItem(0, i, QTableWidgetItem(titles[i]))

        for i in range(len(data)):
            for item in range(0, len(data[i])):
                self.setItem(i+1, item, QTableWidgetItem(str(data[i][item])))


class CalendarDBTable(DBTable):

    def __init__(self, parent):
        DBTable.__init__(self, parent=parent)

    def update_values(self, month, year):
        self.setRowCount(0)
        self.setColumnCount(0)
        days_in_month = monthrange(year, month)[1]

        if days_in_month == 28:
            self.setColumnCount(7)
            self.setRowCount(4)

        else:
            self.setColumnCount(7)
            self.setRowCount(5)
            for i in range(6, 6-(35-days_in_month), -1):
                self.setItem(4, i, QTableWidgetItem("XXXX"))

        try:
            res = self.source.get_flights_on(month, year)
            messages = {}
            for flight in res[0]:
                day = flight[1].day
                row = day // 7
                column = day % 7
                message = f"Дата вылета клиента №{flight[0]}"
                if f"{row}_{column}" not in messages.keys():
                    messages[f"{row}_{column}"] = []
                messages[f"{row}_{column}"].append(message)

            for flight in res[1]:
                day = flight[1].day
                row = day // 7
                column = day % 7
                message = f"Дата прилета клиента №{flight[0]}"
                if f"{row}_{column}" not in messages.keys():
                    messages[f"{row}_{column}"] = []
                messages[f"{row}_{column}"].append(message)

            for i in messages.keys():
                row, column = [int(j) for j in i.split("_")]
                self.setItem(row, column, QTableWidgetItem('\n'.join(messages[i])))
        except Exception as e:
            print(e)



