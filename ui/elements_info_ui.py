# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elements_info.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ElementsInfoForm(object):
    def setupUi(self, ElementsInfoForm):
        if not ElementsInfoForm.objectName():
            ElementsInfoForm.setObjectName(u"ElementsInfoForm")
        ElementsInfoForm.resize(772, 594)
        ElementsInfoForm.setStyleSheet(u"*{\n"
"	font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.verticalLayout = QVBoxLayout(ElementsInfoForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.elements_info_view = QListView(ElementsInfoForm)
        self.elements_info_view.setObjectName(u"elements_info_view")

        self.verticalLayout.addWidget(self.elements_info_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.copy_selected_info = QPushButton(ElementsInfoForm)
        self.copy_selected_info.setObjectName(u"copy_selected_info")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_selected_info.sizePolicy().hasHeightForWidth())
        self.copy_selected_info.setSizePolicy(sizePolicy)
        self.copy_selected_info.setMinimumSize(QSize(0, 30))
        self.copy_selected_info.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.copy_selected_info.setFont(font)
        self.copy_selected_info.setStyleSheet(u"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.copy_selected_info.setText(u"\u590d\u5236")

        self.horizontalLayout.addWidget(self.copy_selected_info)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ElementsInfoForm)

        QMetaObject.connectSlotsByName(ElementsInfoForm)
    # setupUi

    def retranslateUi(self, ElementsInfoForm):
        ElementsInfoForm.setWindowTitle(QCoreApplication.translate("ElementsInfoForm", u"\u5143\u7d20\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.copy_selected_info.setToolTip(QCoreApplication.translate("ElementsInfoForm", u"\u590d\u5236\u9009\u4e2d\u884c\u7684\u5185\u5bb9", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

