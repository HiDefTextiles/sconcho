# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/exportBitmapWidget.ui'
#
# Created: Fri Nov 26 16:36:32 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ExportBitmapWidget(object):
    def setupUi(self, ExportBitmapWidget):
        ExportBitmapWidget.setObjectName("ExportBitmapWidget")
        ExportBitmapWidget.resize(423, 323)
        self.verticalLayout_4 = QtGui.QVBoxLayout(ExportBitmapWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtGui.QLabel(ExportBitmapWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ExportBitmapWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.widthSpinner = QtGui.QSpinBox(ExportBitmapWidget)
        self.widthSpinner.setMaximum(10000)
        self.widthSpinner.setObjectName("widthSpinner")
        self.gridLayout.addWidget(self.widthSpinner, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ExportBitmapWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.heightSpinner = QtGui.QSpinBox(ExportBitmapWidget)
        self.heightSpinner.setMaximum(10000)
        self.heightSpinner.setObjectName("heightSpinner")
        self.gridLayout.addWidget(self.heightSpinner, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ExportBitmapWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(ExportBitmapWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtGui.QLabel(ExportBitmapWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scalingSpinner = QtGui.QSpinBox(ExportBitmapWidget)
        self.scalingSpinner.setMaximum(10000)
        self.scalingSpinner.setObjectName("scalingSpinner")
        self.horizontalLayout.addWidget(self.scalingSpinner)
        self.label_8 = QtGui.QLabel(ExportBitmapWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(ExportBitmapWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileNameEdit = QtGui.QLineEdit(ExportBitmapWidget)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.horizontalLayout_2.addWidget(self.fileNameEdit)
        self.browseButton = QtGui.QPushButton(ExportBitmapWidget)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_2.addWidget(self.browseButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.cancelButton = QtGui.QPushButton(ExportBitmapWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.exportButton = QtGui.QPushButton(ExportBitmapWidget)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_3.addWidget(self.exportButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.widthSpinner)
        self.label_2.setBuddy(self.heightSpinner)
        self.label_8.setBuddy(self.scalingSpinner)

        self.retranslateUi(ExportBitmapWidget)
        QtCore.QMetaObject.connectSlotsByName(ExportBitmapWidget)
        ExportBitmapWidget.setTabOrder(self.widthSpinner, self.heightSpinner)
        ExportBitmapWidget.setTabOrder(self.heightSpinner, self.scalingSpinner)
        ExportBitmapWidget.setTabOrder(self.scalingSpinner, self.fileNameEdit)
        ExportBitmapWidget.setTabOrder(self.fileNameEdit, self.browseButton)

    def retranslateUi(self, ExportBitmapWidget):
        ExportBitmapWidget.setWindowTitle(QtGui.QApplication.translate("ExportBitmapWidget", "sconcho: Export as Bitmap", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExportBitmapWidget", "<b>Image Size</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExportBitmapWidget", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExportBitmapWidget", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ExportBitmapWidget", "pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ExportBitmapWidget", "pixels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ExportBitmapWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Scaling</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ExportBitmapWidget", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ExportBitmapWidget", "< b>File Name</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("ExportBitmapWidget", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("ExportBitmapWidget", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.exportButton.setText(QtGui.QApplication.translate("ExportBitmapWidget", "&Export", None, QtGui.QApplication.UnicodeUTF8))

