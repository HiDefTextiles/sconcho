# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/manage_grid_dialog.ui'
#
# Created: Sun Feb 27 12:23:11 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManageGridDialog(object):
    def setupUi(self, ManageGridDialog):
        ManageGridDialog.setObjectName(_fromUtf8("ManageGridDialog"))
        ManageGridDialog.resize(812, 160)
        ManageGridDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(ManageGridDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(ManageGridDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.numInsertRows = QtGui.QSpinBox(self.tab)
        self.numInsertRows.setMinimum(1)
        self.numInsertRows.setMaximum(1000)
        self.numInsertRows.setObjectName(_fromUtf8("numInsertRows"))
        self.horizontalLayout.addWidget(self.numInsertRows)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.insertRowMode = QtGui.QComboBox(self.tab)
        self.insertRowMode.setObjectName(_fromUtf8("insertRowMode"))
        self.insertRowMode.addItem(_fromUtf8(""))
        self.insertRowMode.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.insertRowMode)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.insertRowPivot = QtGui.QSpinBox(self.tab)
        self.insertRowPivot.setMinimum(1)
        self.insertRowPivot.setMaximum(1000)
        self.insertRowPivot.setObjectName(_fromUtf8("insertRowPivot"))
        self.horizontalLayout.addWidget(self.insertRowPivot)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.insertRowButton = QtGui.QPushButton(self.tab)
        self.insertRowButton.setObjectName(_fromUtf8("insertRowButton"))
        self.horizontalLayout.addWidget(self.insertRowButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.numDeleteRows = QtGui.QSpinBox(self.tab_2)
        self.numDeleteRows.setMinimum(1)
        self.numDeleteRows.setMaximum(1000)
        self.numDeleteRows.setObjectName(_fromUtf8("numDeleteRows"))
        self.horizontalLayout_5.addWidget(self.numDeleteRows)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.deleteRowMode = QtGui.QComboBox(self.tab_2)
        self.deleteRowMode.setObjectName(_fromUtf8("deleteRowMode"))
        self.deleteRowMode.addItem(_fromUtf8(""))
        self.deleteRowMode.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.deleteRowMode)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.deleteRowPivot = QtGui.QSpinBox(self.tab_2)
        self.deleteRowPivot.setMinimum(1)
        self.deleteRowPivot.setMaximum(1000)
        self.deleteRowPivot.setObjectName(_fromUtf8("deleteRowPivot"))
        self.horizontalLayout_5.addWidget(self.deleteRowPivot)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.deleteRowButton = QtGui.QPushButton(self.tab_2)
        self.deleteRowButton.setObjectName(_fromUtf8("deleteRowButton"))
        self.horizontalLayout_5.addWidget(self.deleteRowButton)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.numInsertColumns = QtGui.QSpinBox(self.tab_3)
        self.numInsertColumns.setMinimum(1)
        self.numInsertColumns.setMaximum(1000)
        self.numInsertColumns.setObjectName(_fromUtf8("numInsertColumns"))
        self.horizontalLayout_3.addWidget(self.numInsertColumns)
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.insertColumnMode = QtGui.QComboBox(self.tab_3)
        self.insertColumnMode.setObjectName(_fromUtf8("insertColumnMode"))
        self.insertColumnMode.addItem(_fromUtf8(""))
        self.insertColumnMode.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.insertColumnMode)
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.insertColumnPivot = QtGui.QSpinBox(self.tab_3)
        self.insertColumnPivot.setMinimum(1)
        self.insertColumnPivot.setMaximum(1000)
        self.insertColumnPivot.setObjectName(_fromUtf8("insertColumnPivot"))
        self.horizontalLayout_3.addWidget(self.insertColumnPivot)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.insertColumnButton = QtGui.QPushButton(self.tab_3)
        self.insertColumnButton.setObjectName(_fromUtf8("insertColumnButton"))
        self.horizontalLayout_3.addWidget(self.insertColumnButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_6.addWidget(self.label_8)
        self.numDeleteColumns = QtGui.QSpinBox(self.tab_4)
        self.numDeleteColumns.setMinimum(1)
        self.numDeleteColumns.setMaximum(1000)
        self.numDeleteColumns.setObjectName(_fromUtf8("numDeleteColumns"))
        self.horizontalLayout_6.addWidget(self.numDeleteColumns)
        self.label_11 = QtGui.QLabel(self.tab_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.deleteColumnMode = QtGui.QComboBox(self.tab_4)
        self.deleteColumnMode.setObjectName(_fromUtf8("deleteColumnMode"))
        self.deleteColumnMode.addItem(_fromUtf8(""))
        self.deleteColumnMode.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.deleteColumnMode)
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.deleteColumnPivot = QtGui.QSpinBox(self.tab_4)
        self.deleteColumnPivot.setMinimum(1)
        self.deleteColumnPivot.setMaximum(1000)
        self.deleteColumnPivot.setObjectName(_fromUtf8("deleteColumnPivot"))
        self.horizontalLayout_6.addWidget(self.deleteColumnPivot)
        spacerItem3 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.deleteColumnButton = QtGui.QPushButton(self.tab_4)
        self.deleteColumnButton.setObjectName(_fromUtf8("deleteColumnButton"))
        self.horizontalLayout_6.addWidget(self.deleteColumnButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem4 = QtGui.QSpacerItem(644, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.closeButton = QtGui.QPushButton(ManageGridDialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_9.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.label.setBuddy(self.numInsertRows)
        self.label_2.setBuddy(self.insertRowMode)
        self.label_3.setBuddy(self.insertRowPivot)
        self.label_7.setBuddy(self.numDeleteRows)
        self.label_10.setBuddy(self.insertRowMode)
        self.label_9.setBuddy(self.insertRowPivot)
        self.label_4.setBuddy(self.numInsertColumns)
        self.label_5.setBuddy(self.insertColumnMode)
        self.label_6.setBuddy(self.insertColumnPivot)
        self.label_8.setBuddy(self.numDeleteColumns)
        self.label_11.setBuddy(self.insertRowMode)
        self.label_12.setBuddy(self.insertRowPivot)

        self.retranslateUi(ManageGridDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ManageGridDialog)
        ManageGridDialog.setTabOrder(self.tabWidget, self.numInsertRows)
        ManageGridDialog.setTabOrder(self.numInsertRows, self.insertRowMode)
        ManageGridDialog.setTabOrder(self.insertRowMode, self.insertRowPivot)
        ManageGridDialog.setTabOrder(self.insertRowPivot, self.insertRowButton)
        ManageGridDialog.setTabOrder(self.insertRowButton, self.numDeleteRows)
        ManageGridDialog.setTabOrder(self.numDeleteRows, self.deleteRowButton)
        ManageGridDialog.setTabOrder(self.deleteRowButton, self.numInsertColumns)
        ManageGridDialog.setTabOrder(self.numInsertColumns, self.insertColumnMode)
        ManageGridDialog.setTabOrder(self.insertColumnMode, self.insertColumnPivot)
        ManageGridDialog.setTabOrder(self.insertColumnPivot, self.insertColumnButton)
        ManageGridDialog.setTabOrder(self.insertColumnButton, self.numDeleteColumns)
        ManageGridDialog.setTabOrder(self.numDeleteColumns, self.deleteColumnButton)
        ManageGridDialog.setTabOrder(self.deleteColumnButton, self.closeButton)

    def retranslateUi(self, ManageGridDialog):
        ManageGridDialog.setWindowTitle(QtGui.QApplication.translate("ManageGridDialog", "sconcho: Manage Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageGridDialog", "&insert", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageGridDialog", "row&s", None, QtGui.QApplication.UnicodeUTF8))
        self.insertRowMode.setItemText(0, QtGui.QApplication.translate("ManageGridDialog", "below", None, QtGui.QApplication.UnicodeUTF8))
        self.insertRowMode.setItemText(1, QtGui.QApplication.translate("ManageGridDialog", "above", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageGridDialog", "&row", None, QtGui.QApplication.UnicodeUTF8))
        self.insertRowButton.setText(QtGui.QApplication.translate("ManageGridDialog", "Insert Row(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("ManageGridDialog", "insert row", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManageGridDialog", "&delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ManageGridDialog", "row&s", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteRowMode.setItemText(0, QtGui.QApplication.translate("ManageGridDialog", "at                          ", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteRowMode.setItemText(1, QtGui.QApplication.translate("ManageGridDialog", "above", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ManageGridDialog", "&row", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteRowButton.setText(QtGui.QApplication.translate("ManageGridDialog", "Delete Row(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ManageGridDialog", "delete row", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageGridDialog", "&insert", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ManageGridDialog", "column&s", None, QtGui.QApplication.UnicodeUTF8))
        self.insertColumnMode.setItemText(0, QtGui.QApplication.translate("ManageGridDialog", "left of", None, QtGui.QApplication.UnicodeUTF8))
        self.insertColumnMode.setItemText(1, QtGui.QApplication.translate("ManageGridDialog", "right of", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ManageGridDialog", "&column", None, QtGui.QApplication.UnicodeUTF8))
        self.insertColumnButton.setText(QtGui.QApplication.translate("ManageGridDialog", "Insert Column(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("ManageGridDialog", "insert column", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ManageGridDialog", "&delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ManageGridDialog", "column&s", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteColumnMode.setItemText(0, QtGui.QApplication.translate("ManageGridDialog", "at                                      ", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteColumnMode.setItemText(1, QtGui.QApplication.translate("ManageGridDialog", "left of", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManageGridDialog", "&column", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteColumnButton.setText(QtGui.QApplication.translate("ManageGridDialog", "Delete Column(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("ManageGridDialog", "delete column", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("ManageGridDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

