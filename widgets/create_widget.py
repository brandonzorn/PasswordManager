from PySide6.QtWidgets import QWidget

from forms.create_w import Ui_Form


class CreateWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
