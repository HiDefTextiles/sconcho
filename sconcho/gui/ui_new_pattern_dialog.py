# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/new_pattern_dialog.ui'
#
# Created: Sat May 11 12:28:54 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewPatternDialog(object):
    def setupUi(self, NewPatternDialog):
        NewPatternDialog.setObjectName(_fromUtf8("NewPatternDialog"))
        NewPatternDialog.resize(353, 179)
        self.verticalLayout = QtGui.QVBoxLayout(NewPatternDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(NewPatternDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(NewPatternDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.rowSpinner = QtGui.QSpinBox(NewPatternDialog)
        self.rowSpinner.setMaximum(10000)
        self.rowSpinner.setProperty("value", 10)
        self.rowSpinner.setObjectName(_fromUtf8("rowSpinner"))
        self.gridLayout.addWidget(self.rowSpinner, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(NewPatternDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.columnSpinner = QtGui.QSpinBox(NewPatternDialog)
        self.columnSpinner.setMaximum(1000)
        self.columnSpinner.setProperty("value", 10)
        self.columnSpinner.setObjectName(_fromUtf8("columnSpinner"))
        self.gridLayout.addWidget(self.columnSpinner, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(NewPatternDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.rowSpinner)
        self.label_3.setBuddy(self.columnSpinner)

        self.retranslateUi(NewPatternDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewPatternDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewPatternDialog.close)
        QtCore.QMetaObject.connectSlotsByName(NewPatternDialog)

    def retranslateUi(self, NewPatternDialog):
        NewPatternDialog.setWindowTitle(_translate("NewPatternDialog", "sconcho: New Pattern Grid", None))
        self.label.setText(_translate("NewPatternDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Pattern Grid Dimensions</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p></body></html>", None))
        self.label_2.setText(_translate("NewPatternDialog", "number of rows", None))
        self.label_3.setText(_translate("NewPatternDialog", "number of columns", None))

