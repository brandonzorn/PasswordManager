# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_w.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(473, 493)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name = QLabel(Form)
        self.name.setObjectName(u"name")

        self.horizontalLayout_2.addWidget(self.name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_edit = QPushButton(Form)
        self.btn_edit.setObjectName(u"btn_edit")

        self.horizontalLayout_2.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_2.addWidget(self.btn_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(38, 342, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.username = QLabel(Form)
        self.username.setObjectName(u"username")

        self.verticalLayout_3.addWidget(self.username)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_username_copy = QPushButton(Form)
        self.btn_username_copy.setObjectName(u"btn_username_copy")

        self.horizontalLayout_3.addWidget(self.btn_username_copy)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.password = QLabel(Form)
        self.password.setObjectName(u"password")

        self.verticalLayout_2.addWidget(self.password)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btn_password_copy = QPushButton(Form)
        self.btn_password_copy.setObjectName(u"btn_password_copy")

        self.horizontalLayout_4.addWidget(self.btn_password_copy)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name.setText(QCoreApplication.translate("Form", u"Name", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username", None))
        self.username.setText(QCoreApplication.translate("Form", u"_", None))
        self.btn_username_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Password", None))
        self.password.setText(QCoreApplication.translate("Form", u"_", None))
        self.btn_password_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
    # retranslateUi

