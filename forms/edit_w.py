# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_w.ui'
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
        Form.resize(443, 499)
        Form.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.txt_name = QLineEdit(Form)
        self.txt_name.setObjectName(u"txt_name")

        self.verticalLayout_2.addWidget(self.txt_name)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(28, 287, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.txt_username = QLineEdit(Form)
        self.txt_username.setObjectName(u"txt_username")

        self.verticalLayout.addWidget(self.txt_username)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(88, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_username_copy = QPushButton(Form)
        self.btn_username_copy.setObjectName(u"btn_username_copy")

        self.horizontalLayout_2.addWidget(self.btn_username_copy)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.txt_password = QLineEdit(Form)
        self.txt_password.setObjectName(u"txt_password")

        self.verticalLayout_3.addWidget(self.txt_password)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(155, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_password_copy = QPushButton(Form)
        self.btn_password_copy.setObjectName(u"btn_password_copy")

        self.horizontalLayout_3.addWidget(self.btn_password_copy)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_4.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(Form)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.btn_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Username", None))
        self.btn_username_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.btn_password_copy.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

