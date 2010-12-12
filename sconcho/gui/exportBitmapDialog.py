# -*- coding: utf-8 -*-
########################################################################
#
# (c) 2010 Markus Dittrich
#
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public
# License Version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License Version 3 for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
#
#######################################################################

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import math

from PyQt4.QtCore import (Qt, SIGNAL, QString, QDir, QFileInfo)
from PyQt4.QtGui import (QDialog, QMessageBox, QFileDialog,
                         QImageReader, QDialogButtonBox)

from gui.ui_exportBitmapDialog import Ui_ExportBitmapDialog

import util.messages as msg


##########################################################################
#
# This widget allows users to adjust to control exporting of the
# canvas to a bitmap
#
##########################################################################
class ExportBitmapDialog(QDialog, Ui_ExportBitmapDialog):


    def __init__(self, size, parent = None):
        """
        Initialize the dialog.
        """

        super(ExportBitmapDialog, self).__init__(parent)
        self.setupUi(self)
        self.determine_image_formats()

        self.width = math.floor(size.width())
        self.height = math.floor(size.height())
        self.__originalWidth = self.width
        self.scaling = 100.0
        self.fileName = None 
        self.fileNameEdit.setText(QDir.homePath() + "/")
        self.__aspectRatio = size.width()/size.height()
        
        self.widthSpinner.setValue(self.width)
        self.heightSpinner.setValue(self.height)
        self.scalingSpinner.setValue(self.scaling)

        # synchronize spin boxes
        self.connect(self.widthSpinner, SIGNAL("editingFinished()"),
                     self.width_update)

        self.connect(self.heightSpinner, SIGNAL("editingFinished()"),
                     self.height_update)

        self.connect(self.scalingSpinner, SIGNAL("editingFinished()"),
                     self.scaling_update)
        
        self.connect(self.browseButton, SIGNAL("pressed()"),
                     self.open_file_selector)

        self.connect(self.cancelButton, SIGNAL("pressed()"),
                     self.close)

        self.connect(self.exportButton, SIGNAL("pressed()"),
                     self.accept)


    
    def determine_image_formats(self):
        """ Determine and store all image formats we can
        support. 

        NOTE: qt-4.7 seems to offer gif format even if it
        doesn't support it always so we manually punt it.
        """

        self.formats = ["*.%s" % unicode(format).lower() for \
                            format in QImageReader.supportedImageFormats()]

        self.formats.remove("*.gif")

        # we support svg format as well
        self.formats.append("*.svg")



    def width_update(self):
        """ Update height spinner after width change.

        Update according to the correct aspect ratio.
        """

        newWidth = self.widthSpinner.value()

        self.width = newWidth
        self.height = self.width/self.__aspectRatio
        self.scaling = self.width/self.__originalWidth * 100.0

        self.heightSpinner.setValue(self.height)
        self.scalingSpinner.setValue(self.scaling)



    def height_update(self):
        """ Update width spinner after height change.

        Update according to the correct aspect ratio.
        """

        newHeight = self.heightSpinner.value()
        
        self.width = newHeight * self.__aspectRatio
        self.height = newHeight
        self.scaling = self.width/self.__originalWidth * 100.0

        self.widthSpinner.setValue(self.width)
        self.scalingSpinner.setValue(self.scaling)



    def scaling_update(self):
        """ Update scaling spinner after height change.

        Update according to the correct aspect ratio.
        """

        newScale = self.scalingSpinner.value()

        self.scaling = newScale
        self.width = self.__originalWidth * self.scaling / 100.0
        self.height = self.width/self.__aspectRatio

        self.widthSpinner.setValue(self.width)
        self.heightSpinner.setValue(self.height)


        
    def open_file_selector(self):
        """ Open a file selector and ask for the name """

        formatsString = " ".join(self.formats)
        exportFilePath = QFileDialog.getSaveFileName(self,
                                        msg.exportPatternTitle,
                                        QDir.homePath(),
                                        "Image files (%s)" % formatsString) 

        if exportFilePath:
            self.fileNameEdit.setText(exportFilePath)



    def accept(self):
        """ Checks that we have a path and reminds the user to
        enter one if not. """

        exportFilePath = self.fileNameEdit.text()

        if not exportFilePath:
            QMessageBox.warning(self, msg.noFilePathTitle,
                                msg.noFilePathText,
                                QMessageBox.Close)
            return


        # check the extension; if none is present add .spf
        extension = "*.%s" % QFileInfo(exportFilePath).completeSuffix()
        if extension not in self.formats:
            QMessageBox.warning(self, msg.unknownImageFormatTitle,
                                msg.unknownImageFormatText,
                                QMessageBox.Close)
            return


        self.filePath = exportFilePath

        QDialog.accept(self)



    def keyPressEvent(self, event):
        """ We catch the return key so we don't open
        up the browse menu. """

        if event.key() == Qt.Key_Return:
            return

        QDialog.keyPressEvent(self, event)