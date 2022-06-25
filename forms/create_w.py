# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_w.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(335, 638)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txt_name = QLineEdit(Form)
        self.txt_name.setObjectName(u"txt_name")

        self.verticalLayout.addWidget(self.txt_name)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.txt_username = QLineEdit(Form)
        self.txt_username.setObjectName(u"txt_username")

        self.verticalLayout_2.addWidget(self.txt_username)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.txt_password = QLineEdit(Form)
        self.txt_password.setObjectName(u"txt_password")

        self.verticalLayout_3.addWidget(self.txt_password)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 386, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(Form)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Password", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

