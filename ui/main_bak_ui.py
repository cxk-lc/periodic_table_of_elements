# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_bak.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1329, 873)
        MainWindow.setStyleSheet(u"*{\n"
"	font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.nature_tab = QWidget()
        self.nature_tab.setObjectName(u"nature_tab")
        self.verticalLayout_2 = QVBoxLayout(self.nature_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.group_2 = QLabel(self.nature_tab)
        self.group_2.setObjectName(u"group_2")
        self.group_2.setMinimumSize(QSize(0, 15))
        self.group_2.setMaximumSize(QSize(16777215, 15))
        self.group_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_2, 0, 2, 1, 1)

        self.pushButton_Pm = QPushButton(self.nature_tab)
        self.pushButton_Pm.setObjectName(u"pushButton_Pm")
        self.pushButton_Pm.setMinimumSize(QSize(70, 80))
        self.pushButton_Pm.setMaximumSize(QSize(70, 80))
        self.pushButton_Pm.setProperty("name", u"\u94b7")

        self.gridLayout.addWidget(self.pushButton_Pm, 9, 8, 1, 1)

        self.pushButton_Li = QPushButton(self.nature_tab)
        self.pushButton_Li.setObjectName(u"pushButton_Li")
        self.pushButton_Li.setMinimumSize(QSize(70, 80))
        self.pushButton_Li.setMaximumSize(QSize(70, 80))
        self.pushButton_Li.setProperty("name", u"\u9502")

        self.gridLayout.addWidget(self.pushButton_Li, 3, 1, 1, 1)

        self.pushButton_Bi = QPushButton(self.nature_tab)
        self.pushButton_Bi.setObjectName(u"pushButton_Bi")
        self.pushButton_Bi.setMinimumSize(QSize(70, 80))
        self.pushButton_Bi.setMaximumSize(QSize(70, 80))
        self.pushButton_Bi.setProperty("name", u"\u94cb")

        self.gridLayout.addWidget(self.pushButton_Bi, 7, 15, 1, 1)

        self.pushButton_Pr = QPushButton(self.nature_tab)
        self.pushButton_Pr.setObjectName(u"pushButton_Pr")
        self.pushButton_Pr.setMinimumSize(QSize(70, 80))
        self.pushButton_Pr.setMaximumSize(QSize(70, 80))

        self.gridLayout.addWidget(self.pushButton_Pr, 9, 6, 1, 1)

        self.pushButton_Ne = QPushButton(self.nature_tab)
        self.pushButton_Ne.setObjectName(u"pushButton_Ne")
        self.pushButton_Ne.setMinimumSize(QSize(70, 80))
        self.pushButton_Ne.setMaximumSize(QSize(70, 80))
        self.pushButton_Ne.setProperty("name", u"\u6c16")

        self.gridLayout.addWidget(self.pushButton_Ne, 3, 18, 1, 1)

        self.pushButton_Xe = QPushButton(self.nature_tab)
        self.pushButton_Xe.setObjectName(u"pushButton_Xe")
        self.pushButton_Xe.setMinimumSize(QSize(70, 80))
        self.pushButton_Xe.setMaximumSize(QSize(70, 80))
        self.pushButton_Xe.setProperty("name", u"\u6c19")

        self.gridLayout.addWidget(self.pushButton_Xe, 6, 18, 1, 1)

        self.pushButton_In = QPushButton(self.nature_tab)
        self.pushButton_In.setObjectName(u"pushButton_In")
        self.pushButton_In.setMinimumSize(QSize(70, 80))
        self.pushButton_In.setMaximumSize(QSize(70, 80))
        self.pushButton_In.setProperty("name", u"\u94df")

        self.gridLayout.addWidget(self.pushButton_In, 6, 13, 1, 1)

        self.pushButton_Se = QPushButton(self.nature_tab)
        self.pushButton_Se.setObjectName(u"pushButton_Se")
        self.pushButton_Se.setMinimumSize(QSize(70, 80))
        self.pushButton_Se.setMaximumSize(QSize(70, 80))
        self.pushButton_Se.setProperty("name", u"\u7852")

        self.gridLayout.addWidget(self.pushButton_Se, 5, 16, 1, 1)

        self.pushButton_Y = QPushButton(self.nature_tab)
        self.pushButton_Y.setObjectName(u"pushButton_Y")
        self.pushButton_Y.setMinimumSize(QSize(70, 80))
        self.pushButton_Y.setMaximumSize(QSize(70, 80))
        self.pushButton_Y.setProperty("name", u"\u9487")

        self.gridLayout.addWidget(self.pushButton_Y, 6, 3, 1, 1)

        self.pushButton_Fe = QPushButton(self.nature_tab)
        self.pushButton_Fe.setObjectName(u"pushButton_Fe")
        self.pushButton_Fe.setMinimumSize(QSize(70, 80))
        self.pushButton_Fe.setMaximumSize(QSize(70, 80))
        self.pushButton_Fe.setProperty("name", u"\u94c1")

        self.gridLayout.addWidget(self.pushButton_Fe, 5, 8, 1, 1)

        self.pushButton_Db = QPushButton(self.nature_tab)
        self.pushButton_Db.setObjectName(u"pushButton_Db")
        self.pushButton_Db.setMinimumSize(QSize(70, 80))
        self.pushButton_Db.setMaximumSize(QSize(70, 80))
        self.pushButton_Db.setProperty("name", u"\ud872\udf4a")

        self.gridLayout.addWidget(self.pushButton_Db, 8, 5, 1, 1)

        self.pushButton_Nh = QPushButton(self.nature_tab)
        self.pushButton_Nh.setObjectName(u"pushButton_Nh")
        self.pushButton_Nh.setMinimumSize(QSize(70, 80))
        self.pushButton_Nh.setMaximumSize(QSize(70, 80))
        self.pushButton_Nh.setProperty("name", u"\u9fed")

        self.gridLayout.addWidget(self.pushButton_Nh, 8, 13, 1, 1)

        self.pushButton_Lv = QPushButton(self.nature_tab)
        self.pushButton_Lv.setObjectName(u"pushButton_Lv")
        self.pushButton_Lv.setMinimumSize(QSize(70, 80))
        self.pushButton_Lv.setMaximumSize(QSize(70, 80))
        self.pushButton_Lv.setProperty("name", u"\ud86d\udff7")

        self.gridLayout.addWidget(self.pushButton_Lv, 8, 16, 1, 1)

        self.pushButton_Ta = QPushButton(self.nature_tab)
        self.pushButton_Ta.setObjectName(u"pushButton_Ta")
        self.pushButton_Ta.setMinimumSize(QSize(70, 80))
        self.pushButton_Ta.setMaximumSize(QSize(70, 80))
        self.pushButton_Ta.setProperty("name", u"\u94bd")

        self.gridLayout.addWidget(self.pushButton_Ta, 7, 5, 1, 1)

        self.pushButton_Ce = QPushButton(self.nature_tab)
        self.pushButton_Ce.setObjectName(u"pushButton_Ce")
        self.pushButton_Ce.setMinimumSize(QSize(70, 80))
        self.pushButton_Ce.setMaximumSize(QSize(70, 80))
        self.pushButton_Ce.setProperty("name", u"\u94c8")

        self.gridLayout.addWidget(self.pushButton_Ce, 9, 5, 1, 1)

        self.group_18 = QLabel(self.nature_tab)
        self.group_18.setObjectName(u"group_18")
        self.group_18.setMinimumSize(QSize(0, 15))
        self.group_18.setMaximumSize(QSize(16777215, 15))
        self.group_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_18, 0, 18, 1, 1)

        self.pushButton_Cl = QPushButton(self.nature_tab)
        self.pushButton_Cl.setObjectName(u"pushButton_Cl")
        self.pushButton_Cl.setMinimumSize(QSize(70, 80))
        self.pushButton_Cl.setMaximumSize(QSize(70, 80))
        self.pushButton_Cl.setProperty("name", u"\u6c2f")

        self.gridLayout.addWidget(self.pushButton_Cl, 4, 17, 1, 1)

        self.pushButton_C = QPushButton(self.nature_tab)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setMinimumSize(QSize(70, 80))
        self.pushButton_C.setMaximumSize(QSize(70, 80))
        self.pushButton_C.setProperty("name", u"\u78b3")

        self.gridLayout.addWidget(self.pushButton_C, 3, 14, 1, 1)

        self.pushButton_Nd = QPushButton(self.nature_tab)
        self.pushButton_Nd.setObjectName(u"pushButton_Nd")
        self.pushButton_Nd.setMinimumSize(QSize(70, 80))
        self.pushButton_Nd.setMaximumSize(QSize(70, 80))
        self.pushButton_Nd.setProperty("name", u"\u9495")

        self.gridLayout.addWidget(self.pushButton_Nd, 9, 7, 1, 1)

        self.pushButton_Pt = QPushButton(self.nature_tab)
        self.pushButton_Pt.setObjectName(u"pushButton_Pt")
        self.pushButton_Pt.setMinimumSize(QSize(70, 80))
        self.pushButton_Pt.setMaximumSize(QSize(70, 80))
        self.pushButton_Pt.setProperty("name", u"\u94c2")

        self.gridLayout.addWidget(self.pushButton_Pt, 7, 10, 1, 1)

        self.pushButton_actinicles = QPushButton(self.nature_tab)
        self.pushButton_actinicles.setObjectName(u"pushButton_actinicles")
        self.pushButton_actinicles.setMinimumSize(QSize(70, 80))
        self.pushButton_actinicles.setMaximumSize(QSize(70, 80))
        self.pushButton_actinicles.setProperty("name", u"\u9515\u7cfb\u5143\u7d20")
        self.pushButton_actinicles.setProperty("range", u"89~103")

        self.gridLayout.addWidget(self.pushButton_actinicles, 8, 3, 1, 1)

        self.pushButton_Os = QPushButton(self.nature_tab)
        self.pushButton_Os.setObjectName(u"pushButton_Os")
        self.pushButton_Os.setMinimumSize(QSize(70, 80))
        self.pushButton_Os.setMaximumSize(QSize(70, 80))
        self.pushButton_Os.setProperty("name", u"\u9507")

        self.gridLayout.addWidget(self.pushButton_Os, 7, 8, 1, 1)

        self.pushButton_Mn = QPushButton(self.nature_tab)
        self.pushButton_Mn.setObjectName(u"pushButton_Mn")
        self.pushButton_Mn.setMinimumSize(QSize(70, 80))
        self.pushButton_Mn.setMaximumSize(QSize(70, 80))
        self.pushButton_Mn.setProperty("name", u"\u9530")

        self.gridLayout.addWidget(self.pushButton_Mn, 5, 7, 1, 1)

        self.pushButton_N = QPushButton(self.nature_tab)
        self.pushButton_N.setObjectName(u"pushButton_N")
        self.pushButton_N.setMinimumSize(QSize(70, 80))
        self.pushButton_N.setMaximumSize(QSize(70, 80))
        self.pushButton_N.setProperty("name", u"\u6c2e")

        self.gridLayout.addWidget(self.pushButton_N, 3, 15, 1, 1)

        self.group_14 = QLabel(self.nature_tab)
        self.group_14.setObjectName(u"group_14")
        self.group_14.setMinimumSize(QSize(0, 15))
        self.group_14.setMaximumSize(QSize(16777215, 15))
        self.group_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_14, 0, 14, 1, 1)

        self.pushButton_Zn = QPushButton(self.nature_tab)
        self.pushButton_Zn.setObjectName(u"pushButton_Zn")
        self.pushButton_Zn.setMinimumSize(QSize(70, 80))
        self.pushButton_Zn.setMaximumSize(QSize(70, 80))
        self.pushButton_Zn.setProperty("name", u"\u950c")

        self.gridLayout.addWidget(self.pushButton_Zn, 5, 12, 1, 1)

        self.pushButton_Sg = QPushButton(self.nature_tab)
        self.pushButton_Sg.setObjectName(u"pushButton_Sg")
        self.pushButton_Sg.setMinimumSize(QSize(70, 80))
        self.pushButton_Sg.setMaximumSize(QSize(70, 80))
        self.pushButton_Sg.setProperty("name", u"\ud872\udf73")

        self.gridLayout.addWidget(self.pushButton_Sg, 8, 6, 1, 1)

        self.pushButton_Tm = QPushButton(self.nature_tab)
        self.pushButton_Tm.setObjectName(u"pushButton_Tm")
        self.pushButton_Tm.setMinimumSize(QSize(70, 80))
        self.pushButton_Tm.setMaximumSize(QSize(70, 80))
        self.pushButton_Tm.setProperty("name", u"\u94e5")

        self.gridLayout.addWidget(self.pushButton_Tm, 9, 16, 1, 1)

        self.pushButton_He = QPushButton(self.nature_tab)
        self.pushButton_He.setObjectName(u"pushButton_He")
        self.pushButton_He.setMinimumSize(QSize(70, 80))
        self.pushButton_He.setMaximumSize(QSize(70, 80))
        self.pushButton_He.setProperty("name", u"\u6c26")

        self.gridLayout.addWidget(self.pushButton_He, 2, 18, 1, 1)

        self.pushButton_Na = QPushButton(self.nature_tab)
        self.pushButton_Na.setObjectName(u"pushButton_Na")
        self.pushButton_Na.setMinimumSize(QSize(70, 80))
        self.pushButton_Na.setMaximumSize(QSize(70, 80))
        self.pushButton_Na.setProperty("name", u"\u94a0")

        self.gridLayout.addWidget(self.pushButton_Na, 4, 1, 1, 1)

        self.pushButton_Sb = QPushButton(self.nature_tab)
        self.pushButton_Sb.setObjectName(u"pushButton_Sb")
        self.pushButton_Sb.setMinimumSize(QSize(70, 80))
        self.pushButton_Sb.setMaximumSize(QSize(70, 80))
        self.pushButton_Sb.setProperty("name", u"\u9511")

        self.gridLayout.addWidget(self.pushButton_Sb, 6, 15, 1, 1)

        self.pushButton_FI = QPushButton(self.nature_tab)
        self.pushButton_FI.setObjectName(u"pushButton_FI")
        self.pushButton_FI.setMinimumSize(QSize(70, 80))
        self.pushButton_FI.setMaximumSize(QSize(70, 80))
        self.pushButton_FI.setProperty("name", u"\ud86d\udce7")

        self.gridLayout.addWidget(self.pushButton_FI, 8, 14, 1, 1)

        self.group_6 = QLabel(self.nature_tab)
        self.group_6.setObjectName(u"group_6")
        self.group_6.setMinimumSize(QSize(0, 15))
        self.group_6.setMaximumSize(QSize(16777215, 15))
        self.group_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_6, 0, 7, 1, 1)

        self.group_1 = QLabel(self.nature_tab)
        self.group_1.setObjectName(u"group_1")
        self.group_1.setMinimumSize(QSize(0, 15))
        self.group_1.setMaximumSize(QSize(16777215, 15))
        self.group_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_1, 0, 1, 1, 1)

        self.pushButton_Ts = QPushButton(self.nature_tab)
        self.pushButton_Ts.setObjectName(u"pushButton_Ts")
        self.pushButton_Ts.setMinimumSize(QSize(70, 80))
        self.pushButton_Ts.setMaximumSize(QSize(70, 80))
        self.pushButton_Ts.setProperty("name", u"\u9fec")

        self.gridLayout.addWidget(self.pushButton_Ts, 8, 17, 1, 1)

        self.pushButton_F = QPushButton(self.nature_tab)
        self.pushButton_F.setObjectName(u"pushButton_F")
        self.pushButton_F.setMinimumSize(QSize(70, 80))
        self.pushButton_F.setMaximumSize(QSize(70, 80))
        self.pushButton_F.setProperty("name", u"\u6c1f")

        self.gridLayout.addWidget(self.pushButton_F, 3, 17, 1, 1)

        self.pushButton_Rb = QPushButton(self.nature_tab)
        self.pushButton_Rb.setObjectName(u"pushButton_Rb")
        self.pushButton_Rb.setMinimumSize(QSize(70, 80))
        self.pushButton_Rb.setMaximumSize(QSize(70, 80))
        self.pushButton_Rb.setProperty("name", u"\u94f7")

        self.gridLayout.addWidget(self.pushButton_Rb, 6, 1, 1, 1)

        self.group_16 = QLabel(self.nature_tab)
        self.group_16.setObjectName(u"group_16")
        self.group_16.setMinimumSize(QSize(0, 15))
        self.group_16.setMaximumSize(QSize(16777215, 15))
        self.group_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_16, 0, 16, 1, 1)

        self.pushButton_Sn = QPushButton(self.nature_tab)
        self.pushButton_Sn.setObjectName(u"pushButton_Sn")
        self.pushButton_Sn.setMinimumSize(QSize(70, 80))
        self.pushButton_Sn.setMaximumSize(QSize(70, 80))
        self.pushButton_Sn.setProperty("name", u"\u9521")

        self.gridLayout.addWidget(self.pushButton_Sn, 6, 14, 1, 1)

        self.pushButton_Rg = QPushButton(self.nature_tab)
        self.pushButton_Rg.setObjectName(u"pushButton_Rg")
        self.pushButton_Rg.setMinimumSize(QSize(70, 80))
        self.pushButton_Rg.setMaximumSize(QSize(70, 80))
        self.pushButton_Rg.setProperty("name", u"\ud872\udf2d")

        self.gridLayout.addWidget(self.pushButton_Rg, 8, 11, 1, 1)

        self.pushButton_Gd = QPushButton(self.nature_tab)
        self.pushButton_Gd.setObjectName(u"pushButton_Gd")
        self.pushButton_Gd.setMinimumSize(QSize(70, 80))
        self.pushButton_Gd.setMaximumSize(QSize(70, 80))
        self.pushButton_Gd.setProperty("name", u"\u9486")

        self.gridLayout.addWidget(self.pushButton_Gd, 9, 11, 1, 1)

        self.group_9 = QLabel(self.nature_tab)
        self.group_9.setObjectName(u"group_9")
        self.group_9.setMinimumSize(QSize(0, 15))
        self.group_9.setMaximumSize(QSize(16777215, 15))
        self.group_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_9, 0, 9, 1, 1)

        self.pushButton_Eu = QPushButton(self.nature_tab)
        self.pushButton_Eu.setObjectName(u"pushButton_Eu")
        self.pushButton_Eu.setMinimumSize(QSize(70, 80))
        self.pushButton_Eu.setMaximumSize(QSize(70, 80))
        self.pushButton_Eu.setProperty("name", u"\u94d5")

        self.gridLayout.addWidget(self.pushButton_Eu, 9, 10, 1, 1)

        self.pushButton_Cu = QPushButton(self.nature_tab)
        self.pushButton_Cu.setObjectName(u"pushButton_Cu")
        self.pushButton_Cu.setMinimumSize(QSize(70, 80))
        self.pushButton_Cu.setMaximumSize(QSize(70, 80))
        self.pushButton_Cu.setProperty("name", u"\u94dc")

        self.gridLayout.addWidget(self.pushButton_Cu, 5, 11, 1, 1)

        self.pushButton_Sm = QPushButton(self.nature_tab)
        self.pushButton_Sm.setObjectName(u"pushButton_Sm")
        self.pushButton_Sm.setMinimumSize(QSize(70, 80))
        self.pushButton_Sm.setMaximumSize(QSize(70, 80))
        self.pushButton_Sm.setProperty("name", u"\u9490")

        self.gridLayout.addWidget(self.pushButton_Sm, 9, 9, 1, 1)

        self.pushButton_Pd = QPushButton(self.nature_tab)
        self.pushButton_Pd.setObjectName(u"pushButton_Pd")
        self.pushButton_Pd.setMinimumSize(QSize(70, 80))
        self.pushButton_Pd.setMaximumSize(QSize(70, 80))
        self.pushButton_Pd.setProperty("name", u"\u94af")

        self.gridLayout.addWidget(self.pushButton_Pd, 6, 10, 1, 1)

        self.group_8 = QLabel(self.nature_tab)
        self.group_8.setObjectName(u"group_8")
        self.group_8.setMinimumSize(QSize(0, 15))
        self.group_8.setMaximumSize(QSize(16777215, 15))
        self.group_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_8, 0, 6, 1, 1)

        self.pushButton_La = QPushButton(self.nature_tab)
        self.pushButton_La.setObjectName(u"pushButton_La")
        self.pushButton_La.setMinimumSize(QSize(70, 80))
        self.pushButton_La.setMaximumSize(QSize(70, 80))
        self.pushButton_La.setProperty("name", u"\u9567")

        self.gridLayout.addWidget(self.pushButton_La, 9, 4, 1, 1)

        self.chalcogen_label = QLabel(self.nature_tab)
        self.chalcogen_label.setObjectName(u"chalcogen_label")
        self.chalcogen_label.setMinimumSize(QSize(0, 15))
        self.chalcogen_label.setMaximumSize(QSize(16777215, 20))
        self.chalcogen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.chalcogen_label, 1, 16, 1, 1)

        self.pushButton_H = QPushButton(self.nature_tab)
        self.pushButton_H.setObjectName(u"pushButton_H")
        self.pushButton_H.setMinimumSize(QSize(70, 80))
        self.pushButton_H.setMaximumSize(QSize(70, 80))
        self.pushButton_H.setProperty("name", u"\u6c22")

        self.gridLayout.addWidget(self.pushButton_H, 2, 1, 1, 1)

        self.pushButton_Mg = QPushButton(self.nature_tab)
        self.pushButton_Mg.setObjectName(u"pushButton_Mg")
        self.pushButton_Mg.setMinimumSize(QSize(70, 80))
        self.pushButton_Mg.setMaximumSize(QSize(70, 80))
        self.pushButton_Mg.setProperty("name", u"\u9541")

        self.gridLayout.addWidget(self.pushButton_Mg, 4, 2, 1, 1)

        self.pushButton_Fr = QPushButton(self.nature_tab)
        self.pushButton_Fr.setObjectName(u"pushButton_Fr")
        self.pushButton_Fr.setMinimumSize(QSize(70, 80))
        self.pushButton_Fr.setMaximumSize(QSize(70, 80))
        self.pushButton_Fr.setProperty("name", u"\u94ab")

        self.gridLayout.addWidget(self.pushButton_Fr, 8, 1, 1, 1)

        self.pushButton_W = QPushButton(self.nature_tab)
        self.pushButton_W.setObjectName(u"pushButton_W")
        self.pushButton_W.setMinimumSize(QSize(70, 80))
        self.pushButton_W.setMaximumSize(QSize(70, 80))
        self.pushButton_W.setProperty("name", u"\u94a8")

        self.gridLayout.addWidget(self.pushButton_W, 7, 6, 1, 1)

        self.pushButton_Cr = QPushButton(self.nature_tab)
        self.pushButton_Cr.setObjectName(u"pushButton_Cr")
        self.pushButton_Cr.setMinimumSize(QSize(70, 80))
        self.pushButton_Cr.setMaximumSize(QSize(70, 80))
        self.pushButton_Cr.setProperty("name", u"\u94ec")

        self.gridLayout.addWidget(self.pushButton_Cr, 5, 6, 1, 1)

        self.pushButton_Te = QPushButton(self.nature_tab)
        self.pushButton_Te.setObjectName(u"pushButton_Te")
        self.pushButton_Te.setMinimumSize(QSize(70, 80))
        self.pushButton_Te.setMaximumSize(QSize(70, 80))
        self.pushButton_Te.setProperty("name", u"\u78b2")

        self.gridLayout.addWidget(self.pushButton_Te, 6, 16, 1, 1)

        self.pushButton_Cd = QPushButton(self.nature_tab)
        self.pushButton_Cd.setObjectName(u"pushButton_Cd")
        self.pushButton_Cd.setMinimumSize(QSize(70, 80))
        self.pushButton_Cd.setMaximumSize(QSize(70, 80))
        self.pushButton_Cd.setProperty("name", u"\u9549")

        self.gridLayout.addWidget(self.pushButton_Cd, 6, 12, 1, 1)

        self.pushButton_Tb = QPushButton(self.nature_tab)
        self.pushButton_Tb.setObjectName(u"pushButton_Tb")
        self.pushButton_Tb.setMinimumSize(QSize(70, 80))
        self.pushButton_Tb.setMaximumSize(QSize(70, 80))
        self.pushButton_Tb.setProperty("name", u"\u94fd")

        self.gridLayout.addWidget(self.pushButton_Tb, 9, 12, 1, 1)

        self.group_5 = QLabel(self.nature_tab)
        self.group_5.setObjectName(u"group_5")
        self.group_5.setMinimumSize(QSize(0, 15))
        self.group_5.setMaximumSize(QSize(16777215, 15))
        self.group_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_5, 0, 5, 1, 1)

        self.pushButton_Mt = QPushButton(self.nature_tab)
        self.pushButton_Mt.setObjectName(u"pushButton_Mt")
        self.pushButton_Mt.setMinimumSize(QSize(70, 80))
        self.pushButton_Mt.setMaximumSize(QSize(70, 80))
        self.pushButton_Mt.setProperty("name", u"\u9fcf")

        self.gridLayout.addWidget(self.pushButton_Mt, 8, 9, 1, 1)

        self.pushButton_Ar = QPushButton(self.nature_tab)
        self.pushButton_Ar.setObjectName(u"pushButton_Ar")
        self.pushButton_Ar.setMinimumSize(QSize(70, 80))
        self.pushButton_Ar.setMaximumSize(QSize(70, 80))
        self.pushButton_Ar.setProperty("name", u"\u6c29")

        self.gridLayout.addWidget(self.pushButton_Ar, 4, 18, 1, 1)

        self.pushButton_Mo = QPushButton(self.nature_tab)
        self.pushButton_Mo.setObjectName(u"pushButton_Mo")
        self.pushButton_Mo.setMinimumSize(QSize(70, 80))
        self.pushButton_Mo.setMaximumSize(QSize(70, 80))
        self.pushButton_Mo.setProperty("name", u"\u94bc")

        self.gridLayout.addWidget(self.pushButton_Mo, 6, 6, 1, 1)

        self.pushButton_Mc = QPushButton(self.nature_tab)
        self.pushButton_Mc.setObjectName(u"pushButton_Mc")
        self.pushButton_Mc.setMinimumSize(QSize(70, 80))
        self.pushButton_Mc.setMaximumSize(QSize(70, 80))
        self.pushButton_Mc.setProperty("name", u"\u9546")

        self.gridLayout.addWidget(self.pushButton_Mc, 8, 15, 1, 1)

        self.pushButton_Yb = QPushButton(self.nature_tab)
        self.pushButton_Yb.setObjectName(u"pushButton_Yb")
        self.pushButton_Yb.setMinimumSize(QSize(70, 80))
        self.pushButton_Yb.setMaximumSize(QSize(70, 80))
        self.pushButton_Yb.setProperty("name", u"\u9571")

        self.gridLayout.addWidget(self.pushButton_Yb, 9, 17, 1, 1)

        self.pushButton_Pb = QPushButton(self.nature_tab)
        self.pushButton_Pb.setObjectName(u"pushButton_Pb")
        self.pushButton_Pb.setMinimumSize(QSize(70, 80))
        self.pushButton_Pb.setMaximumSize(QSize(70, 80))
        self.pushButton_Pb.setProperty("name", u"\u94c5")

        self.gridLayout.addWidget(self.pushButton_Pb, 7, 14, 1, 1)

        self.pushButton_Dy = QPushButton(self.nature_tab)
        self.pushButton_Dy.setObjectName(u"pushButton_Dy")
        self.pushButton_Dy.setMinimumSize(QSize(70, 80))
        self.pushButton_Dy.setMaximumSize(QSize(70, 80))
        self.pushButton_Dy.setProperty("name", u"\u955d")

        self.gridLayout.addWidget(self.pushButton_Dy, 9, 13, 1, 1)

        self.group_17 = QLabel(self.nature_tab)
        self.group_17.setObjectName(u"group_17")
        self.group_17.setMinimumSize(QSize(0, 15))
        self.group_17.setMaximumSize(QSize(16777215, 15))
        self.group_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_17, 0, 17, 1, 1)

        self.pushButton_Sc = QPushButton(self.nature_tab)
        self.pushButton_Sc.setObjectName(u"pushButton_Sc")
        self.pushButton_Sc.setMinimumSize(QSize(70, 80))
        self.pushButton_Sc.setMaximumSize(QSize(70, 80))
        self.pushButton_Sc.setProperty("name", u"\u94aa")

        self.gridLayout.addWidget(self.pushButton_Sc, 5, 3, 1, 1)

        self.group_10 = QLabel(self.nature_tab)
        self.group_10.setObjectName(u"group_10")
        self.group_10.setMinimumSize(QSize(0, 15))
        self.group_10.setMaximumSize(QSize(16777215, 15))
        self.group_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_10, 0, 10, 1, 1)

        self.group_13 = QLabel(self.nature_tab)
        self.group_13.setObjectName(u"group_13")
        self.group_13.setMinimumSize(QSize(0, 15))
        self.group_13.setMaximumSize(QSize(16777215, 15))
        self.group_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_13, 0, 13, 1, 1)

        self.pushButton_Ti = QPushButton(self.nature_tab)
        self.pushButton_Ti.setObjectName(u"pushButton_Ti")
        self.pushButton_Ti.setMinimumSize(QSize(70, 80))
        self.pushButton_Ti.setMaximumSize(QSize(70, 80))
        self.pushButton_Ti.setProperty("name", u"\u949b")

        self.gridLayout.addWidget(self.pushButton_Ti, 5, 4, 1, 1)

        self.pushButton_Ni = QPushButton(self.nature_tab)
        self.pushButton_Ni.setObjectName(u"pushButton_Ni")
        self.pushButton_Ni.setMinimumSize(QSize(70, 80))
        self.pushButton_Ni.setMaximumSize(QSize(70, 80))
        self.pushButton_Ni.setProperty("name", u"\u954d")

        self.gridLayout.addWidget(self.pushButton_Ni, 5, 10, 1, 1)

        self.pushButton_Be = QPushButton(self.nature_tab)
        self.pushButton_Be.setObjectName(u"pushButton_Be")
        self.pushButton_Be.setMinimumSize(QSize(70, 80))
        self.pushButton_Be.setMaximumSize(QSize(70, 80))
        self.pushButton_Be.setProperty("name", u"\u94cd")

        self.gridLayout.addWidget(self.pushButton_Be, 3, 2, 1, 1)

        self.periodic_6 = QLabel(self.nature_tab)
        self.periodic_6.setObjectName(u"periodic_6")
        self.periodic_6.setMinimumSize(QSize(15, 0))
        self.periodic_6.setMaximumSize(QSize(15, 16777215))
        self.periodic_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_6, 7, 0, 1, 1)

        self.pushButton_Hf = QPushButton(self.nature_tab)
        self.pushButton_Hf.setObjectName(u"pushButton_Hf")
        self.pushButton_Hf.setMinimumSize(QSize(70, 80))
        self.pushButton_Hf.setMaximumSize(QSize(70, 80))
        self.pushButton_Hf.setProperty("name", u"\u94ea")

        self.gridLayout.addWidget(self.pushButton_Hf, 7, 4, 1, 1)

        self.pushButton_Cs = QPushButton(self.nature_tab)
        self.pushButton_Cs.setObjectName(u"pushButton_Cs")
        self.pushButton_Cs.setMinimumSize(QSize(70, 80))
        self.pushButton_Cs.setMaximumSize(QSize(70, 80))
        self.pushButton_Cs.setProperty("name", u"\u94ef")

        self.gridLayout.addWidget(self.pushButton_Cs, 7, 1, 1, 1)

        self.pushButton_Er = QPushButton(self.nature_tab)
        self.pushButton_Er.setObjectName(u"pushButton_Er")
        self.pushButton_Er.setMinimumSize(QSize(70, 80))
        self.pushButton_Er.setMaximumSize(QSize(70, 80))
        self.pushButton_Er.setProperty("name", u"\u94d2")

        self.gridLayout.addWidget(self.pushButton_Er, 9, 15, 1, 1)

        self.pushButton_B = QPushButton(self.nature_tab)
        self.pushButton_B.setObjectName(u"pushButton_B")
        self.pushButton_B.setMinimumSize(QSize(70, 80))
        self.pushButton_B.setMaximumSize(QSize(70, 80))
        self.pushButton_B.setProperty("name", u"\u787c")

        self.gridLayout.addWidget(self.pushButton_B, 3, 13, 1, 1)

        self.pushButton_Al = QPushButton(self.nature_tab)
        self.pushButton_Al.setObjectName(u"pushButton_Al")
        self.pushButton_Al.setMinimumSize(QSize(70, 80))
        self.pushButton_Al.setMaximumSize(QSize(70, 80))
        self.pushButton_Al.setProperty("name", u"\u94dd")

        self.gridLayout.addWidget(self.pushButton_Al, 4, 13, 1, 1)

        self.group_15 = QLabel(self.nature_tab)
        self.group_15.setObjectName(u"group_15")
        self.group_15.setMinimumSize(QSize(0, 15))
        self.group_15.setMaximumSize(QSize(16777215, 15))
        self.group_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_15, 0, 15, 1, 1)

        self.pushButton_Ds = QPushButton(self.nature_tab)
        self.pushButton_Ds.setObjectName(u"pushButton_Ds")
        self.pushButton_Ds.setMinimumSize(QSize(70, 80))
        self.pushButton_Ds.setMaximumSize(QSize(70, 80))
        self.pushButton_Ds.setProperty("name", u"\ud86d\udffc")

        self.gridLayout.addWidget(self.pushButton_Ds, 8, 10, 1, 1)

        self.pushButton_Rh = QPushButton(self.nature_tab)
        self.pushButton_Rh.setObjectName(u"pushButton_Rh")
        self.pushButton_Rh.setMinimumSize(QSize(70, 80))
        self.pushButton_Rh.setMaximumSize(QSize(70, 80))
        self.pushButton_Rh.setProperty("name", u"\u94d1")

        self.gridLayout.addWidget(self.pushButton_Rh, 6, 9, 1, 1)

        self.pushButton_V = QPushButton(self.nature_tab)
        self.pushButton_V.setObjectName(u"pushButton_V")
        self.pushButton_V.setMinimumSize(QSize(70, 80))
        self.pushButton_V.setMaximumSize(QSize(70, 80))
        self.pushButton_V.setProperty("name", u"\u9492")

        self.gridLayout.addWidget(self.pushButton_V, 5, 5, 1, 1)

        self.pushButton_Ga = QPushButton(self.nature_tab)
        self.pushButton_Ga.setObjectName(u"pushButton_Ga")
        self.pushButton_Ga.setMinimumSize(QSize(70, 80))
        self.pushButton_Ga.setMaximumSize(QSize(70, 80))
        self.pushButton_Ga.setProperty("name", u"\u9553")

        self.gridLayout.addWidget(self.pushButton_Ga, 5, 13, 1, 1)

        self.pushButton_Zr = QPushButton(self.nature_tab)
        self.pushButton_Zr.setObjectName(u"pushButton_Zr")
        self.pushButton_Zr.setMinimumSize(QSize(70, 80))
        self.pushButton_Zr.setMaximumSize(QSize(70, 80))
        self.pushButton_Zr.setProperty("name", u"\u9506")

        self.gridLayout.addWidget(self.pushButton_Zr, 6, 4, 1, 1)

        self.pushButton_Re = QPushButton(self.nature_tab)
        self.pushButton_Re.setObjectName(u"pushButton_Re")
        self.pushButton_Re.setMinimumSize(QSize(70, 80))
        self.pushButton_Re.setMaximumSize(QSize(70, 80))
        self.pushButton_Re.setProperty("name", u"\u94fc")

        self.gridLayout.addWidget(self.pushButton_Re, 7, 7, 1, 1)

        self.pushButton_P = QPushButton(self.nature_tab)
        self.pushButton_P.setObjectName(u"pushButton_P")
        self.pushButton_P.setMinimumSize(QSize(70, 80))
        self.pushButton_P.setMaximumSize(QSize(70, 80))
        self.pushButton_P.setProperty("name", u"\u78f7")

        self.gridLayout.addWidget(self.pushButton_P, 4, 15, 1, 1)

        self.pushButton_lanthanide = QPushButton(self.nature_tab)
        self.pushButton_lanthanide.setObjectName(u"pushButton_lanthanide")
        self.pushButton_lanthanide.setMinimumSize(QSize(70, 80))
        self.pushButton_lanthanide.setMaximumSize(QSize(70, 80))
        self.pushButton_lanthanide.setProperty("name", u"\u9567\u7cfb\u5143\u7d20")
        self.pushButton_lanthanide.setProperty("range", u"57~71")

        self.gridLayout.addWidget(self.pushButton_lanthanide, 7, 3, 1, 1)

        self.group_11 = QLabel(self.nature_tab)
        self.group_11.setObjectName(u"group_11")
        self.group_11.setMinimumSize(QSize(0, 15))
        self.group_11.setMaximumSize(QSize(16777215, 15))
        self.group_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_11, 0, 11, 1, 1)

        self.pushButton_Ge = QPushButton(self.nature_tab)
        self.pushButton_Ge.setObjectName(u"pushButton_Ge")
        self.pushButton_Ge.setMinimumSize(QSize(70, 80))
        self.pushButton_Ge.setMaximumSize(QSize(70, 80))
        self.pushButton_Ge.setProperty("name", u"\u9517")

        self.gridLayout.addWidget(self.pushButton_Ge, 5, 14, 1, 1)

        self.label_18 = QLabel(self.nature_tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 15))
        self.label_18.setMaximumSize(QSize(16777215, 15))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 0, 12, 1, 1)

        self.pushButton_Ca = QPushButton(self.nature_tab)
        self.pushButton_Ca.setObjectName(u"pushButton_Ca")
        self.pushButton_Ca.setMinimumSize(QSize(70, 80))
        self.pushButton_Ca.setMaximumSize(QSize(70, 80))
        self.pushButton_Ca.setProperty("name", u"\u9499")

        self.gridLayout.addWidget(self.pushButton_Ca, 5, 2, 1, 1)

        self.group_3 = QLabel(self.nature_tab)
        self.group_3.setObjectName(u"group_3")
        self.group_3.setMinimumSize(QSize(0, 15))
        self.group_3.setMaximumSize(QSize(16777215, 15))
        self.group_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_3, 0, 3, 1, 1)

        self.pushButton_Si = QPushButton(self.nature_tab)
        self.pushButton_Si.setObjectName(u"pushButton_Si")
        self.pushButton_Si.setMinimumSize(QSize(70, 80))
        self.pushButton_Si.setMaximumSize(QSize(70, 80))
        self.pushButton_Si.setProperty("name", u"\u7845")

        self.gridLayout.addWidget(self.pushButton_Si, 4, 14, 1, 1)

        self.pushButton_At = QPushButton(self.nature_tab)
        self.pushButton_At.setObjectName(u"pushButton_At")
        self.pushButton_At.setMinimumSize(QSize(70, 80))
        self.pushButton_At.setMaximumSize(QSize(70, 80))
        self.pushButton_At.setProperty("name", u"\u7839")

        self.gridLayout.addWidget(self.pushButton_At, 7, 17, 1, 1)

        self.pushButton_O = QPushButton(self.nature_tab)
        self.pushButton_O.setObjectName(u"pushButton_O")
        self.pushButton_O.setMinimumSize(QSize(70, 80))
        self.pushButton_O.setMaximumSize(QSize(70, 80))
        self.pushButton_O.setProperty("name", u"\u6c27")

        self.gridLayout.addWidget(self.pushButton_O, 3, 16, 1, 1)

        self.pushButton_Og = QPushButton(self.nature_tab)
        self.pushButton_Og.setObjectName(u"pushButton_Og")
        self.pushButton_Og.setMinimumSize(QSize(70, 80))
        self.pushButton_Og.setMaximumSize(QSize(70, 80))
        self.pushButton_Og.setProperty("name", u"\u9feb")

        self.gridLayout.addWidget(self.pushButton_Og, 8, 18, 1, 1)

        self.periodic_1 = QLabel(self.nature_tab)
        self.periodic_1.setObjectName(u"periodic_1")
        self.periodic_1.setMinimumSize(QSize(15, 0))
        self.periodic_1.setMaximumSize(QSize(15, 16777215))
        self.periodic_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_1, 2, 0, 1, 1)

        self.periodic_3 = QLabel(self.nature_tab)
        self.periodic_3.setObjectName(u"periodic_3")
        self.periodic_3.setMinimumSize(QSize(15, 0))
        self.periodic_3.setMaximumSize(QSize(15, 16777215))
        self.periodic_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_3, 4, 0, 1, 1)

        self.pushButton_Ir = QPushButton(self.nature_tab)
        self.pushButton_Ir.setObjectName(u"pushButton_Ir")
        self.pushButton_Ir.setMinimumSize(QSize(70, 80))
        self.pushButton_Ir.setMaximumSize(QSize(70, 80))
        self.pushButton_Ir.setProperty("name", u"\u94f1")

        self.gridLayout.addWidget(self.pushButton_Ir, 7, 9, 1, 1)

        self.pushButton_Cn = QPushButton(self.nature_tab)
        self.pushButton_Cn.setObjectName(u"pushButton_Cn")
        self.pushButton_Cn.setMinimumSize(QSize(70, 80))
        self.pushButton_Cn.setMaximumSize(QSize(70, 80))
        self.pushButton_Cn.setProperty("name", u"\u9fd4")

        self.gridLayout.addWidget(self.pushButton_Cn, 8, 12, 1, 1)

        self.pushButton_Co = QPushButton(self.nature_tab)
        self.pushButton_Co.setObjectName(u"pushButton_Co")
        self.pushButton_Co.setMinimumSize(QSize(70, 80))
        self.pushButton_Co.setMaximumSize(QSize(70, 80))
        self.pushButton_Co.setProperty("name", u"\u94b4")

        self.gridLayout.addWidget(self.pushButton_Co, 5, 9, 1, 1)

        self.pushButton_Au = QPushButton(self.nature_tab)
        self.pushButton_Au.setObjectName(u"pushButton_Au")
        self.pushButton_Au.setMinimumSize(QSize(70, 80))
        self.pushButton_Au.setMaximumSize(QSize(70, 80))
        self.pushButton_Au.setProperty("name", u"\u91d1")

        self.gridLayout.addWidget(self.pushButton_Au, 7, 11, 1, 1)

        self.periodic_5 = QLabel(self.nature_tab)
        self.periodic_5.setObjectName(u"periodic_5")
        self.periodic_5.setMinimumSize(QSize(15, 0))
        self.periodic_5.setMaximumSize(QSize(15, 16777215))
        self.periodic_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_5, 6, 0, 1, 1)

        self.pushButton_Ag = QPushButton(self.nature_tab)
        self.pushButton_Ag.setObjectName(u"pushButton_Ag")
        self.pushButton_Ag.setMinimumSize(QSize(70, 80))
        self.pushButton_Ag.setMaximumSize(QSize(70, 80))
        self.pushButton_Ag.setProperty("name", u"\u94f6")

        self.gridLayout.addWidget(self.pushButton_Ag, 6, 11, 1, 1)

        self.pushButton_Rn = QPushButton(self.nature_tab)
        self.pushButton_Rn.setObjectName(u"pushButton_Rn")
        self.pushButton_Rn.setMinimumSize(QSize(70, 80))
        self.pushButton_Rn.setMaximumSize(QSize(70, 80))
        self.pushButton_Rn.setProperty("name", u"\u6c21")

        self.gridLayout.addWidget(self.pushButton_Rn, 7, 18, 1, 1)

        self.pushButton_I = QPushButton(self.nature_tab)
        self.pushButton_I.setObjectName(u"pushButton_I")
        self.pushButton_I.setMinimumSize(QSize(70, 80))
        self.pushButton_I.setMaximumSize(QSize(70, 80))
        self.pushButton_I.setProperty("name", u"\u7898")

        self.gridLayout.addWidget(self.pushButton_I, 6, 17, 1, 1)

        self.pushButton_Tc = QPushButton(self.nature_tab)
        self.pushButton_Tc.setObjectName(u"pushButton_Tc")
        self.pushButton_Tc.setMinimumSize(QSize(70, 80))
        self.pushButton_Tc.setMaximumSize(QSize(70, 80))
        self.pushButton_Tc.setProperty("name", u"\u951d")

        self.gridLayout.addWidget(self.pushButton_Tc, 6, 7, 1, 1)

        self.pushButton_Bh = QPushButton(self.nature_tab)
        self.pushButton_Bh.setObjectName(u"pushButton_Bh")
        self.pushButton_Bh.setMinimumSize(QSize(70, 80))
        self.pushButton_Bh.setMaximumSize(QSize(70, 80))
        self.pushButton_Bh.setProperty("name", u"\ud872\udf5b")

        self.gridLayout.addWidget(self.pushButton_Bh, 8, 7, 1, 1)

        self.nitrogen_group_label = QLabel(self.nature_tab)
        self.nitrogen_group_label.setObjectName(u"nitrogen_group_label")
        self.nitrogen_group_label.setMinimumSize(QSize(0, 15))
        self.nitrogen_group_label.setMaximumSize(QSize(16777215, 20))
        self.nitrogen_group_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.nitrogen_group_label, 1, 15, 1, 1)

        self.pushButton_Ho = QPushButton(self.nature_tab)
        self.pushButton_Ho.setObjectName(u"pushButton_Ho")
        self.pushButton_Ho.setMinimumSize(QSize(70, 80))
        self.pushButton_Ho.setMaximumSize(QSize(70, 80))
        self.pushButton_Ho.setProperty("name", u"\u94ac")

        self.gridLayout.addWidget(self.pushButton_Ho, 9, 14, 1, 1)

        self.pushButton_Ru = QPushButton(self.nature_tab)
        self.pushButton_Ru.setObjectName(u"pushButton_Ru")
        self.pushButton_Ru.setMinimumSize(QSize(70, 80))
        self.pushButton_Ru.setMaximumSize(QSize(70, 80))
        self.pushButton_Ru.setProperty("name", u"\u948c")

        self.gridLayout.addWidget(self.pushButton_Ru, 6, 8, 1, 1)

        self.pushButton_Hs = QPushButton(self.nature_tab)
        self.pushButton_Hs.setObjectName(u"pushButton_Hs")
        self.pushButton_Hs.setMinimumSize(QSize(70, 80))
        self.pushButton_Hs.setMaximumSize(QSize(70, 80))
        self.pushButton_Hs.setProperty("name", u"\ud872\udf76")

        self.gridLayout.addWidget(self.pushButton_Hs, 8, 8, 1, 1)

        self.pushButton_Br = QPushButton(self.nature_tab)
        self.pushButton_Br.setObjectName(u"pushButton_Br")
        self.pushButton_Br.setMinimumSize(QSize(70, 80))
        self.pushButton_Br.setMaximumSize(QSize(70, 80))
        self.pushButton_Br.setProperty("name", u"\u6eb4")

        self.gridLayout.addWidget(self.pushButton_Br, 5, 17, 1, 1)

        self.pushButton_Nb = QPushButton(self.nature_tab)
        self.pushButton_Nb.setObjectName(u"pushButton_Nb")
        self.pushButton_Nb.setMinimumSize(QSize(70, 80))
        self.pushButton_Nb.setMaximumSize(QSize(70, 80))
        self.pushButton_Nb.setProperty("name", u"\u94cc")

        self.gridLayout.addWidget(self.pushButton_Nb, 6, 5, 1, 1)

        self.pushButton_Rf = QPushButton(self.nature_tab)
        self.pushButton_Rf.setObjectName(u"pushButton_Rf")
        self.pushButton_Rf.setMinimumSize(QSize(70, 80))
        self.pushButton_Rf.setMaximumSize(QSize(70, 80))
        self.pushButton_Rf.setProperty("name", u"\ud872\udf3b")

        self.gridLayout.addWidget(self.pushButton_Rf, 8, 4, 1, 1)

        self.group_4 = QLabel(self.nature_tab)
        self.group_4.setObjectName(u"group_4")
        self.group_4.setMinimumSize(QSize(0, 15))
        self.group_4.setMaximumSize(QSize(16777215, 15))
        self.group_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_4, 0, 4, 1, 1)

        self.pushButton_TI = QPushButton(self.nature_tab)
        self.pushButton_TI.setObjectName(u"pushButton_TI")
        self.pushButton_TI.setMinimumSize(QSize(70, 80))
        self.pushButton_TI.setMaximumSize(QSize(70, 80))
        self.pushButton_TI.setProperty("name", u"\u94ca")

        self.gridLayout.addWidget(self.pushButton_TI, 7, 13, 1, 1)

        self.halogen_label = QLabel(self.nature_tab)
        self.halogen_label.setObjectName(u"halogen_label")
        self.halogen_label.setMinimumSize(QSize(0, 15))
        self.halogen_label.setMaximumSize(QSize(16777215, 20))
        self.halogen_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.halogen_label, 1, 17, 1, 1)

        self.periodic_2 = QLabel(self.nature_tab)
        self.periodic_2.setObjectName(u"periodic_2")
        self.periodic_2.setMinimumSize(QSize(15, 0))
        self.periodic_2.setMaximumSize(QSize(15, 16777215))
        self.periodic_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_2, 3, 0, 1, 1)

        self.pushButton_Po = QPushButton(self.nature_tab)
        self.pushButton_Po.setObjectName(u"pushButton_Po")
        self.pushButton_Po.setMinimumSize(QSize(70, 80))
        self.pushButton_Po.setMaximumSize(QSize(70, 80))
        self.pushButton_Po.setProperty("name", u"\u948b")

        self.gridLayout.addWidget(self.pushButton_Po, 7, 16, 1, 1)

        self.pushButton_Ra = QPushButton(self.nature_tab)
        self.pushButton_Ra.setObjectName(u"pushButton_Ra")
        self.pushButton_Ra.setMinimumSize(QSize(70, 80))
        self.pushButton_Ra.setMaximumSize(QSize(70, 80))
        self.pushButton_Ra.setProperty("name", u"\u956d")

        self.gridLayout.addWidget(self.pushButton_Ra, 8, 2, 1, 1)

        self.periodic_7 = QLabel(self.nature_tab)
        self.periodic_7.setObjectName(u"periodic_7")
        self.periodic_7.setMinimumSize(QSize(15, 0))
        self.periodic_7.setMaximumSize(QSize(15, 16777215))
        self.periodic_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_7, 8, 0, 1, 1)

        self.pushButton_S = QPushButton(self.nature_tab)
        self.pushButton_S.setObjectName(u"pushButton_S")
        self.pushButton_S.setMinimumSize(QSize(70, 80))
        self.pushButton_S.setMaximumSize(QSize(70, 80))
        self.pushButton_S.setProperty("name", u"\u786b")

        self.gridLayout.addWidget(self.pushButton_S, 4, 16, 1, 1)

        self.group_7 = QLabel(self.nature_tab)
        self.group_7.setObjectName(u"group_7")
        self.group_7.setMinimumSize(QSize(0, 15))
        self.group_7.setMaximumSize(QSize(16777215, 15))
        self.group_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.group_7, 0, 8, 1, 1)

        self.pushButton_Kr = QPushButton(self.nature_tab)
        self.pushButton_Kr.setObjectName(u"pushButton_Kr")
        self.pushButton_Kr.setMinimumSize(QSize(70, 80))
        self.pushButton_Kr.setMaximumSize(QSize(70, 80))
        self.pushButton_Kr.setProperty("name", u"\u6c2a")

        self.gridLayout.addWidget(self.pushButton_Kr, 5, 18, 1, 1)

        self.pushButton_Lu = QPushButton(self.nature_tab)
        self.pushButton_Lu.setObjectName(u"pushButton_Lu")
        self.pushButton_Lu.setMinimumSize(QSize(70, 80))
        self.pushButton_Lu.setMaximumSize(QSize(70, 80))
        self.pushButton_Lu.setProperty("name", u"\u9565")

        self.gridLayout.addWidget(self.pushButton_Lu, 9, 18, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 9, 1, 1, 3)

        self.pushButton_Sr = QPushButton(self.nature_tab)
        self.pushButton_Sr.setObjectName(u"pushButton_Sr")
        self.pushButton_Sr.setMinimumSize(QSize(70, 80))
        self.pushButton_Sr.setMaximumSize(QSize(70, 80))
        self.pushButton_Sr.setProperty("name", u"\u9536")

        self.gridLayout.addWidget(self.pushButton_Sr, 6, 2, 1, 1)

        self.pushButton_Hg = QPushButton(self.nature_tab)
        self.pushButton_Hg.setObjectName(u"pushButton_Hg")
        self.pushButton_Hg.setMinimumSize(QSize(70, 80))
        self.pushButton_Hg.setMaximumSize(QSize(70, 80))
        self.pushButton_Hg.setProperty("name", u"\u6c5e")

        self.gridLayout.addWidget(self.pushButton_Hg, 7, 12, 1, 1)

        self.pushButton_As = QPushButton(self.nature_tab)
        self.pushButton_As.setObjectName(u"pushButton_As")
        self.pushButton_As.setMinimumSize(QSize(70, 80))
        self.pushButton_As.setMaximumSize(QSize(70, 80))
        self.pushButton_As.setProperty("name", u"\u7837")

        self.gridLayout.addWidget(self.pushButton_As, 5, 15, 1, 1)

        self.periodic_4 = QLabel(self.nature_tab)
        self.periodic_4.setObjectName(u"periodic_4")
        self.periodic_4.setMinimumSize(QSize(15, 0))
        self.periodic_4.setMaximumSize(QSize(15, 16777215))
        self.periodic_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.periodic_4, 5, 0, 1, 1)

        self.pushButton_Ba = QPushButton(self.nature_tab)
        self.pushButton_Ba.setObjectName(u"pushButton_Ba")
        self.pushButton_Ba.setMinimumSize(QSize(70, 80))
        self.pushButton_Ba.setMaximumSize(QSize(70, 80))
        self.pushButton_Ba.setProperty("name", u"\u94a1")

        self.gridLayout.addWidget(self.pushButton_Ba, 7, 2, 1, 1)

        self.pushButton_K = QPushButton(self.nature_tab)
        self.pushButton_K.setObjectName(u"pushButton_K")
        self.pushButton_K.setMinimumSize(QSize(70, 80))
        self.pushButton_K.setMaximumSize(QSize(70, 80))
        self.pushButton_K.setProperty("name", u"\u94be")

        self.gridLayout.addWidget(self.pushButton_K, 5, 1, 1, 1)

        self.pushButton_Lr = QPushButton(self.nature_tab)
        self.pushButton_Lr.setObjectName(u"pushButton_Lr")
        self.pushButton_Lr.setMinimumSize(QSize(70, 80))
        self.pushButton_Lr.setMaximumSize(QSize(70, 80))
        self.pushButton_Lr.setProperty("name", u"\u94f9")

        self.gridLayout.addWidget(self.pushButton_Lr, 10, 18, 1, 1)

        self.pushButton_No = QPushButton(self.nature_tab)
        self.pushButton_No.setObjectName(u"pushButton_No")
        self.pushButton_No.setMinimumSize(QSize(70, 80))
        self.pushButton_No.setMaximumSize(QSize(70, 80))
        self.pushButton_No.setProperty("name", u"\u9518")

        self.gridLayout.addWidget(self.pushButton_No, 10, 17, 1, 1)

        self.pushButton_Md = QPushButton(self.nature_tab)
        self.pushButton_Md.setObjectName(u"pushButton_Md")
        self.pushButton_Md.setMinimumSize(QSize(70, 80))
        self.pushButton_Md.setMaximumSize(QSize(70, 80))
        self.pushButton_Md.setProperty("name", u"\u9494")

        self.gridLayout.addWidget(self.pushButton_Md, 10, 16, 1, 1)

        self.pushButton_Fm = QPushButton(self.nature_tab)
        self.pushButton_Fm.setObjectName(u"pushButton_Fm")
        self.pushButton_Fm.setMinimumSize(QSize(70, 80))
        self.pushButton_Fm.setMaximumSize(QSize(70, 80))
        self.pushButton_Fm.setProperty("name", u"\u9544")

        self.gridLayout.addWidget(self.pushButton_Fm, 10, 15, 1, 1)

        self.pushButton_Es = QPushButton(self.nature_tab)
        self.pushButton_Es.setObjectName(u"pushButton_Es")
        self.pushButton_Es.setMinimumSize(QSize(70, 80))
        self.pushButton_Es.setMaximumSize(QSize(70, 80))
        self.pushButton_Es.setProperty("name", u"\u953f")

        self.gridLayout.addWidget(self.pushButton_Es, 10, 14, 1, 1)

        self.pushButton_Cf = QPushButton(self.nature_tab)
        self.pushButton_Cf.setObjectName(u"pushButton_Cf")
        self.pushButton_Cf.setMinimumSize(QSize(70, 80))
        self.pushButton_Cf.setMaximumSize(QSize(70, 80))
        self.pushButton_Cf.setProperty("name", u"\u950e")

        self.gridLayout.addWidget(self.pushButton_Cf, 10, 13, 1, 1)

        self.pushButton_Bk = QPushButton(self.nature_tab)
        self.pushButton_Bk.setObjectName(u"pushButton_Bk")
        self.pushButton_Bk.setMinimumSize(QSize(70, 80))
        self.pushButton_Bk.setMaximumSize(QSize(70, 80))
        self.pushButton_Bk.setProperty("name", u"\u952b")

        self.gridLayout.addWidget(self.pushButton_Bk, 10, 12, 1, 1)

        self.pushButton_Cm = QPushButton(self.nature_tab)
        self.pushButton_Cm.setObjectName(u"pushButton_Cm")
        self.pushButton_Cm.setMinimumSize(QSize(70, 80))
        self.pushButton_Cm.setMaximumSize(QSize(70, 80))
        self.pushButton_Cm.setProperty("name", u"\u9514")

        self.gridLayout.addWidget(self.pushButton_Cm, 10, 11, 1, 1)

        self.pushButton_Am = QPushButton(self.nature_tab)
        self.pushButton_Am.setObjectName(u"pushButton_Am")
        self.pushButton_Am.setMinimumSize(QSize(70, 80))
        self.pushButton_Am.setMaximumSize(QSize(70, 80))
        self.pushButton_Am.setProperty("name", u"\u9545")

        self.gridLayout.addWidget(self.pushButton_Am, 10, 10, 1, 1)

        self.pushButton_Pu = QPushButton(self.nature_tab)
        self.pushButton_Pu.setObjectName(u"pushButton_Pu")
        self.pushButton_Pu.setMinimumSize(QSize(70, 80))
        self.pushButton_Pu.setMaximumSize(QSize(70, 80))
        self.pushButton_Pu.setProperty("name", u"\u949a")

        self.gridLayout.addWidget(self.pushButton_Pu, 10, 9, 1, 1)

        self.pushButton_Np = QPushButton(self.nature_tab)
        self.pushButton_Np.setObjectName(u"pushButton_Np")
        self.pushButton_Np.setMinimumSize(QSize(70, 80))
        self.pushButton_Np.setMaximumSize(QSize(70, 80))
        self.pushButton_Np.setProperty("name", u"\u954e")

        self.gridLayout.addWidget(self.pushButton_Np, 10, 8, 1, 1)

        self.pushButton_U = QPushButton(self.nature_tab)
        self.pushButton_U.setObjectName(u"pushButton_U")
        self.pushButton_U.setMinimumSize(QSize(70, 80))
        self.pushButton_U.setMaximumSize(QSize(70, 80))
        self.pushButton_U.setProperty("name", u"\u94c0")

        self.gridLayout.addWidget(self.pushButton_U, 10, 7, 1, 1)

        self.pushButton_Pa = QPushButton(self.nature_tab)
        self.pushButton_Pa.setObjectName(u"pushButton_Pa")
        self.pushButton_Pa.setMinimumSize(QSize(70, 80))
        self.pushButton_Pa.setMaximumSize(QSize(70, 80))
        self.pushButton_Pa.setProperty("name", u"\u9564")

        self.gridLayout.addWidget(self.pushButton_Pa, 10, 6, 1, 1)

        self.pushButton_Th = QPushButton(self.nature_tab)
        self.pushButton_Th.setObjectName(u"pushButton_Th")
        self.pushButton_Th.setMinimumSize(QSize(70, 80))
        self.pushButton_Th.setMaximumSize(QSize(70, 80))
        self.pushButton_Th.setProperty("name", u"\u948d")

        self.gridLayout.addWidget(self.pushButton_Th, 10, 5, 1, 1)

        self.pushButton_Ac = QPushButton(self.nature_tab)
        self.pushButton_Ac.setObjectName(u"pushButton_Ac")
        self.pushButton_Ac.setMinimumSize(QSize(70, 80))
        self.pushButton_Ac.setMaximumSize(QSize(70, 80))
        self.pushButton_Ac.setProperty("name", u"\u9515")

        self.gridLayout.addWidget(self.pushButton_Ac, 10, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 10, 1, 1, 3)

        self.periodic_6_1 = QLabel(self.nature_tab)
        self.periodic_6_1.setObjectName(u"periodic_6_1")
        self.periodic_6_1.setMinimumSize(QSize(15, 0))
        self.periodic_6_1.setMaximumSize(QSize(15, 16777215))

        self.gridLayout.addWidget(self.periodic_6_1, 9, 0, 1, 1)

        self.periodic_7_1 = QLabel(self.nature_tab)
        self.periodic_7_1.setObjectName(u"periodic_7_1")
        self.periodic_7_1.setMinimumSize(QSize(15, 0))
        self.periodic_7_1.setMaximumSize(QSize(15, 16777215))

        self.gridLayout.addWidget(self.periodic_7_1, 10, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout.setRowStretch(9, 1)
        self.gridLayout.setRowStretch(10, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.gridLayout.setColumnStretch(7, 1)
        self.gridLayout.setColumnStretch(8, 1)
        self.gridLayout.setColumnStretch(9, 1)
        self.gridLayout.setColumnStretch(10, 1)
        self.gridLayout.setColumnStretch(11, 1)
        self.gridLayout.setColumnStretch(12, 1)
        self.gridLayout.setColumnStretch(13, 1)
        self.gridLayout.setColumnStretch(14, 1)
        self.gridLayout.setColumnStretch(15, 1)
        self.gridLayout.setColumnStretch(16, 1)
        self.gridLayout.setColumnStretch(17, 1)
        self.gridLayout.setColumnStretch(18, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 1)
        self.gridLayout.setColumnMinimumWidth(3, 1)
        self.gridLayout.setColumnMinimumWidth(4, 1)
        self.gridLayout.setColumnMinimumWidth(5, 1)
        self.gridLayout.setColumnMinimumWidth(6, 1)
        self.gridLayout.setColumnMinimumWidth(7, 1)
        self.gridLayout.setColumnMinimumWidth(8, 1)
        self.gridLayout.setColumnMinimumWidth(9, 1)
        self.gridLayout.setColumnMinimumWidth(10, 1)
        self.gridLayout.setColumnMinimumWidth(11, 1)
        self.gridLayout.setColumnMinimumWidth(12, 1)
        self.gridLayout.setColumnMinimumWidth(13, 1)
        self.gridLayout.setColumnMinimumWidth(14, 1)
        self.gridLayout.setColumnMinimumWidth(15, 1)
        self.gridLayout.setColumnMinimumWidth(16, 1)
        self.gridLayout.setColumnMinimumWidth(17, 1)
        self.gridLayout.setColumnMinimumWidth(18, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 1)
        self.gridLayout.setRowMinimumHeight(3, 1)
        self.gridLayout.setRowMinimumHeight(4, 1)
        self.gridLayout.setRowMinimumHeight(5, 1)
        self.gridLayout.setRowMinimumHeight(6, 1)
        self.gridLayout.setRowMinimumHeight(7, 1)
        self.gridLayout.setRowMinimumHeight(8, 1)
        self.gridLayout.setRowMinimumHeight(9, 1)
        self.gridLayout.setRowMinimumHeight(10, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.nature_tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nature_tab), u"\u6027\u8d28")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1329, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5143\u7d20\u5468\u671f\u8868", None))
        self.group_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_Pm.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Li.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Bi.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pr.setProperty("name", QCoreApplication.translate("MainWindow", u"\u9568", None))
        self.pushButton_Ne.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Xe.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_In.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Se.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Y.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Fe.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Db.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Nh.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Lv.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ta.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ce.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.pushButton_Cl.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Nd.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pt.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_actinicles.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Os.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Mn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_N.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_Zn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Sg.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Tm.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_He.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Na.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Sb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_FI.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_6.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.group_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_Ts.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_F.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Rb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.pushButton_Sn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Rg.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Gd.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_Eu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Sm.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pd.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_8.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_La.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.chalcogen_label.setText(QCoreApplication.translate("MainWindow", u"\u6c27\u65cf", None))
        self.pushButton_H.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Mg.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Fr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_W.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Te.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cd.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Tb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_Mt.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ar.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Mo.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Mc.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Yb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Dy.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_Sc.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.group_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_Ti.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ni.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Be.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.periodic_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_Hf.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cs.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Er.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_B.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Al.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_Ds.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Rh.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_V.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ga.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Zr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Re.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_P.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_lanthanide.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_Ge.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_Ca.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_Si.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_At.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_O.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Og.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.periodic_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.periodic_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_Ir.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Co.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Au.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.periodic_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_Ag.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Rn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_I.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Tc.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Bh.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.nitrogen_group_label.setText(QCoreApplication.translate("MainWindow", u"\u6c2e\u65cf", None))
        self.pushButton_Ho.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ru.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Hs.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Br.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Nb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Rf.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_TI.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.halogen_label.setText(QCoreApplication.translate("MainWindow", u"\u5364\u65cf", None))
        self.periodic_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_Po.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ra.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.periodic_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_S.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.group_7.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_Kr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Lu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Sr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Hg.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_As.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.periodic_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_Ba.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_K.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Lr.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_No.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Md.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Fm.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Es.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cf.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Bk.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Cm.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Am.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pu.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Np.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_U.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Pa.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Th.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_Ac.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.periodic_6_1.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.periodic_7_1.setText(QCoreApplication.translate("MainWindow", u"7", None))
    # retranslateUi

