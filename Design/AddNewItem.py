# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 420)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_onoff = QtWidgets.QHBoxLayout()
        self.layout_onoff.setObjectName("layout_onoff")
        self.label_onoff = QtWidgets.QLabel(Dialog)
        self.label_onoff.setObjectName("label_onoff")
        self.layout_onoff.addWidget(self.label_onoff)
        self.checkBox_onoff = QtWidgets.QCheckBox(Dialog)
        self.checkBox_onoff.setText("")
        self.checkBox_onoff.setObjectName("checkBox_onoff")
        self.layout_onoff.addWidget(self.checkBox_onoff)
        self.layout_onoff.setStretch(0, 1)
        self.layout_onoff.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_onoff)
        self.layout_unit = QtWidgets.QHBoxLayout()
        self.layout_unit.setObjectName("layout_unit")
        self.label_unit = QtWidgets.QLabel(Dialog)
        self.label_unit.setObjectName("label_unit")
        self.layout_unit.addWidget(self.label_unit)
        self.lineEdit_unit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_unit.setObjectName("lineEdit_unit")
        self.layout_unit.addWidget(self.lineEdit_unit)
        self.layout_unit.setStretch(0, 1)
        self.layout_unit.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_unit)
        self.layout_terminal = QtWidgets.QHBoxLayout()
        self.layout_terminal.setObjectName("layout_terminal")
        self.label_terminal = QtWidgets.QLabel(Dialog)
        self.label_terminal.setObjectName("label_terminal")
        self.layout_terminal.addWidget(self.label_terminal)
        self.lineEdit_terminal = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_terminal.setObjectName("lineEdit_terminal")
        self.layout_terminal.addWidget(self.lineEdit_terminal)
        self.layout_terminal.setStretch(0, 1)
        self.layout_terminal.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_terminal)
        self.layout_ip = QtWidgets.QHBoxLayout()
        self.layout_ip.setObjectName("layout_ip")
        self.label_ip = QtWidgets.QLabel(Dialog)
        self.label_ip.setObjectName("label_ip")
        self.layout_ip.addWidget(self.label_ip)
        self.lineEdit_ip = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.layout_ip.addWidget(self.lineEdit_ip)
        self.layout_ip.setStretch(0, 1)
        self.layout_ip.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_ip)
        self.layout_mac = QtWidgets.QHBoxLayout()
        self.layout_mac.setObjectName("layout_mac")
        self.label_mac = QtWidgets.QLabel(Dialog)
        self.label_mac.setObjectName("label_mac")
        self.layout_mac.addWidget(self.label_mac)
        self.lineEdit_mac = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_mac.setInputMask("")
        self.lineEdit_mac.setObjectName("lineEdit_mac")
        self.layout_mac.addWidget(self.lineEdit_mac)
        self.layout_mac.setStretch(0, 1)
        self.layout_mac.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_mac)
        self.layout_switch = QtWidgets.QHBoxLayout()
        self.layout_switch.setObjectName("layout_switch")
        self.label_switch = QtWidgets.QLabel(Dialog)
        self.label_switch.setObjectName("label_switch")
        self.layout_switch.addWidget(self.label_switch)
        self.lineEdit_switch = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_switch.setObjectName("lineEdit_switch")
        self.layout_switch.addWidget(self.lineEdit_switch)
        self.layout_switch.setStretch(0, 1)
        self.layout_switch.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_switch)
        self.layout_port = QtWidgets.QHBoxLayout()
        self.layout_port.setObjectName("layout_port")
        self.label_port = QtWidgets.QLabel(Dialog)
        self.label_port.setObjectName("label_port")
        self.layout_port.addWidget(self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_port.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.layout_port.addWidget(self.lineEdit_port)
        self.layout_port.setStretch(0, 1)
        self.layout_port.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_port)
        self.layout_power = QtWidgets.QHBoxLayout()
        self.layout_power.setObjectName("layout_power")
        self.label_power = QtWidgets.QLabel(Dialog)
        self.label_power.setObjectName("label_power")
        self.layout_power.addWidget(self.label_power)
        self.lineEdit_power = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_power.setObjectName("lineEdit_power")
        self.layout_power.addWidget(self.lineEdit_power)
        self.layout_power.setStretch(0, 1)
        self.layout_power.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_power)
        self.layout_orion = QtWidgets.QHBoxLayout()
        self.layout_orion.setObjectName("layout_orion")
        self.label_orion = QtWidgets.QLabel(Dialog)
        self.label_orion.setObjectName("label_orion")
        self.layout_orion.addWidget(self.label_orion)
        self.lineEdit_orion = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_orion.setObjectName("lineEdit_orion")
        self.layout_orion.addWidget(self.lineEdit_orion)
        self.layout_orion.setStretch(0, 1)
        self.layout_orion.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_orion)
        self.layout_zabbix = QtWidgets.QHBoxLayout()
        self.layout_zabbix.setObjectName("layout_zabbix")
        self.label_zabbix = QtWidgets.QLabel(Dialog)
        self.label_zabbix.setObjectName("label_zabbix")
        self.layout_zabbix.addWidget(self.label_zabbix)
        self.lineEdit_zabbix = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_zabbix.setObjectName("lineEdit_zabbix")
        self.layout_zabbix.addWidget(self.lineEdit_zabbix)
        self.layout_zabbix.setStretch(0, 1)
        self.layout_zabbix.setStretch(1, 3)
        self.verticalLayout.addLayout(self.layout_zabbix)
        self.layout_btnGroup = QtWidgets.QHBoxLayout()
        self.layout_btnGroup.setSpacing(10)
        self.layout_btnGroup.setObjectName("layout_btnGroup")
        self.btn_accept = QtWidgets.QPushButton(Dialog)
        self.btn_accept.setObjectName("btn_accept")
        self.layout_btnGroup.addWidget(self.btn_accept)
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.layout_btnGroup.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.layout_btnGroup)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_onoff.setText(_translate("Dialog", "Include:"))
        self.label_unit.setText(_translate("Dialog", "Unit:"))
        self.label_terminal.setText(_translate("Dialog", "Terminal:"))
        self.label_ip.setText(_translate("Dialog", "IP:"))
        self.lineEdit_ip.setInputMask(_translate("Dialog", "000.000.000.000"))
        self.label_mac.setText(_translate("Dialog", "MAC:"))
        self.label_switch.setText(_translate("Dialog", "Switch:"))
        self.label_port.setText(_translate("Dialog", "Port:"))
        self.label_power.setText(_translate("Dialog", "Power:"))
        self.label_orion.setText(_translate("Dialog", "Orion:"))
        self.label_zabbix.setText(_translate("Dialog", "Zabbix:"))
        self.btn_accept.setText(_translate("Dialog", "Accept"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))