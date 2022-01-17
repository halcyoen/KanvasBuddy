# This file is part of KanvasBuddy.

# KanvasBuddy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# KanvasBuddy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with KanvasBuddy. If not, see <https://www.gnu.org/licenses/>.

import importlib
from krita import Krita

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QEvent

from .kbtitlebar import KBTitleBar
from .kbpanelstack import KBPanelStack

from PyQt5.QtWidgets import QMessageBox
def boop(text): # Print a message to a dialog box
    msg = QMessageBox()
    msg.setText(str(text))
    msg.exec_()

class UIKanvasBuddy(QWidget):

    def __init__(self, kbuddy):
        super(UIKanvasBuddy, self).__init__(Krita.instance().activeWindow().qwindow())
        # -- FOR TESTING ONLY --
        # importlib.reload(sldbar)
        # importlib.reload(btnbar)
        # importlib.reload(title)
        # importlib.reload(pnlstk)
        
        self.kbuddy = kbuddy
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        
        self.layout().addWidget(KBTitleBar(self))

        self.panelStack = KBPanelStack(self)
        self.layout().addWidget(self.panelStack)


    def launch(self): 
        self.panelStack.currentChanged(0)
        self.show()


    def closeEvent(self, e):
        self.panelStack.dismantle() # Return borrowed widgets to previous parents or else we're doomed
        self.kbuddy.setIsActive(False)
        super().closeEvent(e)


    def mousePressEvent(self, e):
        self.setFocus()    