# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'support@sogelink.com'
__date__ = '2025-03-24'
__copyright__ = 'Copyright 2025, Sogelink'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from marvin_dockwidget import MarvinDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class MarvinDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = MarvinDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(MarvinDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

