# -*- coding:utf-8 -*-
#
# Copyright © 2015 Gonzalo Peña-Castellanos (@goanpeca)
#
# Licensed under the terms of the MIT License
# (see example/__init__.py for details)

"""Spyder Plugin Example Widget."""

# Standard library imports
import sys

# Third party imports
from spyderlib.qt.QtGui import (QMessageBox, QPushButton, QTableWidget,
                                QVBoxLayout, QWidget)
from spyderlib.utils import icon_manager as ima

# Local imports
from spyderlib.config.base import get_translation


_ = get_translation("example", "spyplugins.ui.example")


class ExampleWidget(QWidget):
    """
    Example widget.

    Methods defined here should not be aware of spyder, but of the function
    required by the widget only.
    """

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)

        self.setWindowTitle("Example")

        # Widgets
        self.button = QPushButton('Current editor')
        self.table = QTableWidget(self)

        # Widget setup
        self.button.setIcon(ima.icon('spyder'))

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def msgbox(self, msg=None):
        """Message box."""
        QMessageBox.information(self, 'Title', msg)
