from PySide6.QtWidgets import QWidget

from forms.login_w import Ui_Form


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def setup(self, login):
        self.ui.name.setText(login.name)
        self.ui.username.setText(login.username)
        self.ui.password.setText(login.password)
