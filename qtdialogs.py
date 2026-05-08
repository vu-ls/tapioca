# BEGIN LICENSE #
#
# CERT Tapioca
#
# Copyright 2018 Carnegie Mellon University. All Rights Reserved.
#
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
# ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
# CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER
# EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED
# TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY,
# OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON
# UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO
# FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#
# Released under a BSD (SEI)-style license, please see license.txt or
# contact permission@sei.cmu.edu for full terms.
#
# [DISTRIBUTION STATEMENT A] This material has been approved for
# public release and unlimited distribution.  Please see Copyright
# notice for non-US Government use and distribution.
# CERT(R) is registered in the U.S. Patent and Trademark Office by
# Carnegie Mellon University.
#
# DM18-0637
#
# END LICENSE #
try:
    from PyQt4.QtGui import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog
    from PyQt4.QtCore import pyqtSlot
except ImportError:
    try:
        from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog
        from PyQt5.QtCore import pyqtSlot
    except ImportError:
        try:
            from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog
            from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QInputDialog
        except ImportError:
            print('Be sure to run ./install_tapioca.sh before attempting to run %s' % __file__)
            sys.exit(1)



app = QApplication([])
win = QWidget()
msgBox = QMessageBox()

def YesNo(question='', caption='Tapioca'):
    try:
        # Qt6
        question_icon = QMessageBox.Icon.Question
        yes_button = QMessageBox.StandardButton.Yes
        no_button = QMessageBox.StandardButton.No
    except AttributeError:
        # Qt5 / Qt4
        question_icon = QMessageBox.Question
        yes_button = QMessageBox.Yes
        no_button = QMessageBox.No

    msgBox.setIcon(question_icon)
    msgBox.setText(question)
    msgBox.setWindowTitle(caption)
    msgBox.setStandardButtons(yes_button | no_button)
    ret = msgBox.exec()
    if ret == QMessageBox.Yes:
        return True
    else:
        return False


def Info(message='', caption='Tapioca'):
    try:
        # Qt6
        info_icon = QMessageBox.Icon.Information
        ok_button = QMessageBox.StandardButton.Ok
    except AttributeError:
        # Older Qt
        info_icon = QMessageBox.Information
        ok_button = QMessageBox.Ok

    msgBox.setIcon(info_icon)
    msgBox.setText(message)
    msgBox.setWindowTitle(caption)
    msgBox.setStandardButtons(ok_button)
    msgBox.exec()


def Warn(message='', caption='Warning!'):
    try:
        # Qt6
        warning_icon = QMessageBox.Icon.Warning
        ok_button = QMessageBox.StandardButton.Ok
    except AttributeError:
        # Older Qt
        info_icon = QMessageBox.Warning
        ok_button = QMessageBox.Ok

    msgBox.setIcon(warning_icon)
    msgBox.setText(message)
    msgBox.setWindowTitle(caption)
    msgBox.setStandardButtons(ok_button)
    msgBox.exec()


def Ask(message='', caption='Tapioca', default_value=''):
    text, ok = QInputDialog.getText(win, caption, message, text=default_value)
    return text
