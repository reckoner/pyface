#------------------------------------------------------------------------------
# Copyright (c) 2007, Riverbank Computing Limited
# All rights reserved.
#
# Copyright (c) 2017, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license.  However, when used with the GPL version of PyQt the additional
# terms described in the PyQt GPL exception also apply.
#
# Author: Riverbank Computing Limited and Enthought developers
#------------------------------------------------------------------------------


import sys

from pyface.qt import QtCore, QtGui, qt_api
from pyface.base_toolkit import Toolkit

if qt_api == 'pyqt':
    # Check the version numbers are late enough.
    if QtCore.QT_VERSION < 0x040200:
        raise RuntimeError(
            "Need Qt v4.2 or higher, but got v%s" % QtCore.QT_VERSION_STR
        )

    if QtCore.PYQT_VERSION < 0x040100:
        raise RuntimeError(
            "Need PyQt v4.1 or higher, but got v%s" % QtCore.PYQT_VERSION_STR
        )

# It's possible that it has already been initialised.
_app = QtGui.QApplication.instance()

if _app is None:
    _app = QtGui.QApplication(sys.argv)


# create the toolkit object
toolkit_object = Toolkit('qt4', 'pyface.ui.qt4')
