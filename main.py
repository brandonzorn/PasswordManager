import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget

from database import Database
from forms.main import Ui_Form
from items import Login
from widgets.create_widget import CreateWidget
from widgets.edit_widget import EditWidget
from widgets.login_widget import LoginWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(self.screen().size().width() // 2, self.screen().size().height() // 2))
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle('PasswordManager')
        # self.setWindowIcon(QIcon(app_icon_path))

        self.db = Database()
        self.log = QStackedWidget()

        self.logins = []

        self.ui.horizontalLayout_4.addWidget(self.log)

        self.edit_w = EditWidget()
        self.log_w = LoginWidget()
        self.create_w = CreateWidget()

        self.create_w.ui.btn_cancel.clicked.connect(self.clicked_log)
        self.log_w.ui.btn_edit.clicked.connect(self.clicked_edit)
        self.edit_w.ui.btn_cancel.clicked.connect(self.clicked_log)
        self.ui.btn_create.clicked.connect(self.clicked_create)

        self.create_w.ui.btn_save.clicked.connect(self.create_login)

        self.ui.listWidget.doubleClicked.connect(self.double_click)

        self.log.addWidget(self.log_w)
        self.clicked_log()
        self.show()

    def clicked_create(self):
        self.log.removeWidget(self.log.currentWidget())
        self.log.addWidget(self.create_w)

    def clicked_log(self):
        self.log.removeWidget(self.log.currentWidget())
        self.log.addWidget(self.log_w)
        self.logins = self.db.get_logins()
        self.setup_logins()

    def double_click(self):
        self.log_w.setup(self.logins[self.ui.listWidget.currentIndex().row()])

    def clicked_edit(self):
        self.log.removeWidget(self.log.currentWidget())
        self.log.addWidget(self.edit_w)

    def create_login(self):
        if (self.create_w.ui.txt_name.text() and self.create_w.ui.txt_username.text()
                and self.create_w.ui.txt_password.text()):
            login_id = self.ui.listWidget.count()
            login = Login(login_id, self.create_w.ui.txt_name.text(),
                          self.create_w.ui.txt_username.text(), self.create_w.ui.txt_password.text())
            self.db.add_login(login)
            self.clicked_log()

    def setup_logins(self):
        self.ui.listWidget.clear()
        for login in self.logins:
            self.ui.listWidget.addItem(login.name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())
