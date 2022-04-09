from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy
from PyQt5.Qt import Qt

from Views import View


# Класс формы для авторизации
class LoginForm(View):

    # Сигнал для запуска авторизации пользователя
    auth = pyqtSignal(str, str)

    def __init__(self, geometry=None):
        View.__init__(self, "LoginForm", geometry)
        self.setWindowTitle('Login')

        global_layout = QGridLayout()
        widget_layout = QGridLayout()
        self.widget = QWidget(self)
        self.widget.setObjectName("LoginBullet")
        self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.widget.setLayout(widget_layout)

        self.login_line = QLineEdit(parent=self.widget, placeholderText='Логин')
        self.login_line.setMinimumSize(300, 50)
        self.login_line.setMaximumSize(600, 50)
        self.password_line = QLineEdit(parent=self.widget, placeholderText='Пароль')
        self.password_line.setEchoMode(2)
        self.password_line.setMinimumSize(300, 50)
        self.password_line.setMaximumSize(600, 50)
        self.button = QPushButton(parent=self.widget, text='Войти')
        self.button.setObjectName("GreenButton")
        self.button.setMinimumSize(70, 40)
        self.button.setMaximumSize(140, 60)
        self.button.clicked.connect(self.login)

        widget_layout.addWidget(self.login_line, 0, 0, 2, 4)
        widget_layout.setVerticalSpacing(20)
        widget_layout.addWidget(self.password_line, 2, 0, 2, 4)
        widget_layout.addWidget(self.button, 4, 0, 2, 2)

        global_layout.addWidget(self.widget, 1, 1, 3, 3, alignment=Qt.AlignCenter)

        self.setLayout(global_layout)
        self.show()

    def login(self):
        text = self.login_line.text() if self.login_line.text() != '' else None
        passw = self.password_line.text() if self.password_line.text() != '' else None
        #print(f"Emmiting signal auth in LoginForm with value '{text}'")
        self.auth.emit(text, passw)
