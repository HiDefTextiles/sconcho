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

from PyQt4.QtCore import (Qt, SIGNAL, QString)
from PyQt4.QtGui import (QDialog, QMessageBox)
from gui.ui_insertDeleteRowColumnWidget import Ui_InsertDeleteRowColumnWidget
import util.helpers.messages as msg


##########################################################################
#
# This widget provides a dialog for inserting and deleting rows
# of the main pattern grid.
#
##########################################################################
class InsertDeleteRowColumnWidget(QDialog, Ui_InsertDeleteRowColumnWidget):


    def __init__(self, numRows, numCols, row, col, parent = None):
        """
        Initialize the dialog.
        """

        super(InsertDeleteRowColumnWidget, self).__init__(parent)
        self.setupUi(self)

        # set the maximum of the spinbox
        self.set_upper_row_limit(numRows)
        self.set_upper_column_limit(numCols)

        # set the current values for row/column to be changed
        self.set_row_col(row, col)

        # install some connections
        self.connect(self.closeButton, SIGNAL("clicked()"), self.close)
        self.connect(self.insertRowButton, SIGNAL("clicked()"),
                     self.insert_row_button_pressed)
        self.connect(self.deleteRowButton, SIGNAL("clicked()"),
                     self.delete_row_button_pressed)
        self.connect(self.insertColumnButton, SIGNAL("clicked()"),
                     self.insert_column_button_pressed)
        self.connect(self.deleteColumnButton, SIGNAL("clicked()"),
                     self.delete_column_button_pressed)



    def insert_row_button_pressed(self):
        """ This method forwards clicks on the insertRowButton.

        NOTE: Row addition always succeeds (short of a bug) and
        we can directly update the widget limits.
        """

        addRows    = self.numInsertRows.value()
        pivot      = self.insertRowPivot.value()
        insertMode = self.insertRowMode.currentText()

        if pivot <= 0:
            return

        self.set_upper_row_limit(self.__numRows + addRows)
        self.emit(SIGNAL("insert_row"), addRows, insertMode, pivot)
        
        
        
    def delete_row_button_pressed(self):
        """ This method forwards clicks on the deleteRowButton.

        NOTE: Row deletion always succeeds (short of a bug) and
        we can directly update the widget limits.

        We make sure that there is at least one row left.
        """

        if self.__numRows <= 1:
            QMessageBox.warning(self, msg.numRowTooSmallTitle,
                                msg.numRowTooSmallText,
                                QMessageBox.Close)
            return


        deadRowID = self.deleteRowID.value()
        self.set_upper_row_limit(self.__numRows - 1)
        self.emit(SIGNAL("delete_row"), deadRowID)



    def insert_column_button_pressed(self):
        """ This method forwards clicks on the insertColumnButton.

        NOTE: For column addition we can not simpy update the
        limits of the spin boxes since addition may fail due
        to the layout. Thus, we have to wait for the success
        signal from the PatternCanvas before we can update
        widgets.
        """
        
        addColumns = self.numInsertColumns.value()
        pivot      = self.insertColumnPivot.value()
        insertMode = self.insertColumnMode.currentText()

        if pivot <= 0:
            return

        self.emit(SIGNAL("insert_column"), addColumns, insertMode, pivot)



    def delete_column_button_pressed(self):
        """ This method forwards clicks on the deleteColumnButton.

        NOTE: For column deletion we can not simpy update the
        limits of the spin boxes since addition may fail due
        to the layout. Thus, we have to wait for the success
        signal from the PatternCanvas before we can update
        widgets.
        """

        if self.__numCols <= 1:
            QMessageBox.warning(self, msg.numColTooSmallTitle,
                                msg.numColTooSmallText,
                                QMessageBox.Close)

            return

        deadColumnID = self.deleteColumnID.value()
        self.emit(SIGNAL("delete_column"), deadColumnID)
        


    def set_upper_row_limit(self, numRows):
        """ Sets the upper limit of the row selectors based
        on the number of available rows.
        """

        self.insertRowPivot.setMinimum(1)
        self.insertRowPivot.setMaximum(numRows)
        self.deleteRowID.setMinimum(1)
        self.deleteRowID.setMaximum(numRows)
        self.__numRows = numRows
        


    def set_upper_column_limit(self, numCols):
        """
        Sets the upper limit of the column selectors based
        on the number of available columns.
        """

        self.insertColumnPivot.setMinimum(1)
        self.insertColumnPivot.setMaximum(numCols)
        self.deleteColumnID.setMinimum(1)
        self.deleteColumnID.setMaximum(numCols)
        self.__numCols = numCols



    def set_row_col(self, row, col):
        """ Set the current value of row/column entry to
        be changed.
        """

        self.insertRowPivot.setValue(self.__numRows - row + 1)
        self.insertColumnPivot.setValue(self.__numCols - col + 1)
