from PySide6.QtWidgets import QWidget

from forms.edit_w import Ui_Form


class EditWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
