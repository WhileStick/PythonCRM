from Utils import DB
from Views import LoginForm, MainMenu, CreateClient
from loader import db


class Controller:

    def __init__(self):
        self.current_window = None
        self.db = db
        self.current_user = None

    def hide_current_window(func):
        def wrapper(self, *args):
            geometry = None
            if self.current_window:
                self.current_window.close()
                geometry = self.current_window.get_geometry()
            func(self, geometry, *args)
        return wrapper

    @hide_current_window
    def show_login(self, frgeo):
        self.current_window = LoginForm(frgeo)
        self.current_window.auth.connect(self.authorize)
        self.current_window.show()

    @hide_current_window
    def show_main(self, frgeo, log="logged_in_user"):
        if log == "logged_in_user":
            log = self.current_user
        self.current_window = MainMenu(frgeo, log)
        self.current_user = log
        self.current_window.switch_to_create_client.connect(self.show_create_client)
        self.current_window.switch_exit.connect(self.show_login)
        #self.current_window.switch_window.connect(self.show_login)
        self.current_window.show()

    @hide_current_window
    def show_create_client(self, frgeo):
        self.current_window = CreateClient(frgeo)
        self.current_window.switch_to_menu.connect(self.show_main)
        self.current_window.show()

    def authorize(self, login, password):
        try:
            authorized = self.db.try_to_auth(login, password)
            if authorized:
                print("[Controller] authorization complete")
                self.show_main(login)
            else:
                print("[Controller] Cannot authorize - incorrect login or password")
        except Exception as e:
            print(e)
