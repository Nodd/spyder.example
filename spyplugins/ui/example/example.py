# -*- coding:utf-8 -*-
#
# Copyright © 2015 Gonzalo Peña-Castellanos (@goanpeca)
#
# Licensed under the terms of the MIT License
# (see example/__init__.py for details)

"""Spyder Plugin Example Package."""

# Standard library imports
from spyderlib.qt.QtCore import Signal, Qt
from spyderlib.qt.QtGui import QVBoxLayout, QGroupBox

# Third party imports
from spyderlib.config.base import get_translation
from spyderlib.plugins import SpyderPluginMixin, PluginConfigPage
from spyderlib.utils import icon_manager as ima

# Local imports
from .widgets.example import ExampleWidget
from .data import images


_ = get_translation("example", "spyplugins.ui.example")


class ExampleConfigPage(PluginConfigPage):
    def setup_page(self):
        results_group = QGroupBox(_("Group page"))

        lineedit = self.create_lineedit(_('Example line'),
                                        'example_line',
                                        default='default_value',
                                        alignment=Qt.Horizontal,
                                        )

        results_layout = QVBoxLayout()
        results_layout.addWidget(lineedit)
        results_group.setLayout(results_layout)

        vlayout = QVBoxLayout()
        vlayout.addWidget(results_group)
        vlayout.addStretch(1)
        self.setLayout(vlayout)


class ExamplePlugin(ExampleWidget, SpyderPluginMixin):
    """Example package widget.

    Methods defined here should be spyder aware and define the communication
    between different spyder plugins, panes and components.
    """

    # Class variables
    CONF_SECTION = 'spyplugins.ui.example'  # Settings section in spyder.ini
    CONFIGWIDGET_CLASS = ExampleConfigPage

    # Signals
    sig_example = Signal()

    def __init__(self, parent=None):
        ExampleWidget.__init__(self, parent=parent)
        SpyderPluginMixin.__init__(self, parent)

        # Initialize plugin
        self.initialize_plugin()

    # --- SpyderPluginWidget API ----------------------------------------------
    def get_plugin_title(self):
        """Return widget title."""
        return _("Example Package")

    def get_plugin_icon(self):
        """Return widget icon."""
        path = path = images.__path__[0]
        return ima.icon(self.CONF_SECTION, icon_path=path)

    def get_focus_widget(self):
        """
        Return the widget to give focus to when this plugin's dockwidget is
        raised on top-level.
        """
        return self.table

    def get_plugin_actions(self):
        """Return a list of actions related to plugin."""
        return []

    def on_first_registration(self):
        """Action to be performed on first plugin registration."""
        self.main.tabify_plugins(self.main.inspector, self)
        self.dockwidget.hide()

    def register_plugin(self):
        """Register plugin in Spyder's main window."""
        self.button.clicked.connect(self.run_example)

        main = self.main
        main.add_dockwidget(self)

    def refresh_plugin(self):
        """Refresh profiler widget."""
        # FIXME: not implemented yet

    def closing_plugin(self, cancelable=False):
        """Perform actions before parent main window is closed."""
        return True

    def apply_plugin_settings(self, options):
        """Apply configuration file's plugin settings."""
        pass

    # --- Public API ----------------------------------------------------------
    def run_example(self):
        """Run example msgbox."""
        current_editor = self.main.editor.get_current_editor()
        self.msgbox('Hello plugin world!\n\n{0}'.format(current_editor))
