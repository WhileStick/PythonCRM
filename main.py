import sys
from PyQt5 import QtCore, QtWidgets

from Utils import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    with open("Styles/stylesheet.txt", "r") as styletxt:
        app.setStyleSheet(styletxt.read())
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
