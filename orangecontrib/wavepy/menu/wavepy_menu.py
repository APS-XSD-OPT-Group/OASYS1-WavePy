# #########################################################################
# Copyright (c) 2020, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2020. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings

from oasys.menus.menu import OMenu
from wavepy2.util.plot.plotter import PlotterMode
from wavepy2.util.log.logger import LoggerMode

class WavePyMenu(OMenu):

    def __init__(self):
        super().__init__(name="WavePy")

        self.openContainer()
        self.addContainer("Plotter Options")
        self.addSubMenu("Set Plotter Mode: FULL")
        self.addSubMenu("Set Plotter Mode: DISPLAY ONLY")
        self.closeContainer()

        self.openContainer()
        self.addContainer("Logger Options")
        self.addSubMenu("Set Logger Mode: FULL")
        self.addSubMenu("Set Logger Mode: WARNING")
        self.addSubMenu("Set Logger Mode: ERROR")
        self.addSubMenu("Set Logger Mode: NONE")
        self.closeContainer()

    def executeAction_1(self, action):
        QSettings().setValue("wavepy/plotter_mode", PlotterMode.FULL)
        showInfoMessage("Plotter Mode set to: FULL\nReload the workspace to make it effective")

    def executeAction_2(self, action):
        QSettings().setValue("wavepy/plotter_mode", PlotterMode.DISPLAY_ONLY)
        showInfoMessage("Plotter Mode set to: DISPLAY ONLY\nReload the workspace to make it effective")

    def executeAction_3(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.FULL)
        showInfoMessage("Logger Mode set to: FULL\nReload the workspace to make it effective")

    def executeAction_4(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.WARNING)
        showInfoMessage("Logger Mode set to: WARNING\nReload the workspace to make it effective")

    def executeAction_5(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.ERROR)
        showInfoMessage("Logger Mode set to: ERROR\nReload the workspace to make it effective")

    def executeAction_6(self, action):
        QSettings().setValue("wavepy/logger_mode", LoggerMode.NONE)
        showInfoMessage("Logger Mode set to: NONE\nReload the workspace to make it effective")

def showInfoMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def showConfirmMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Question)
    msgBox.setText(message)
    msgBox.setInformativeText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
    ret = msgBox.exec_()
    return ret

def showWarningMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def showCriticalMessage(message):
    msgBox = QtWidgets.QMessageBox()
    msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    msgBox.setText(message)
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()
