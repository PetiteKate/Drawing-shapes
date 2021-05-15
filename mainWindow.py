# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import core

class Ui_MainWindow(QtWidgets.QWidget):
    _service = None
    _invoker = None
    _caretaker = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logsPlainText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logsPlainText.setObjectName("logsPlainText")
        self.figureLabel = QtWidgets.QLabel(self.centralwidget)
        self.figureLabel.setObjectName("figureLabel")
        self.horizontalLayout.addWidget(self.figureLabel)
        self.horizontalLayout.addWidget(self.logsPlainText)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.selectFigure = QtWidgets.QComboBox(self.centralwidget)
        self.selectFigure.setObjectName("selectFigure")
        self.selectFigure.addItem("")
        self.selectFigure.addItem("")
        self.selectFigure.addItem("")
        self.selectFigure.addItem("")
        self.selectFigure.addItem("")
        self.verticalLayout_3.addWidget(self.selectFigure)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.sizeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.horizontalLayout_6.addWidget(self.sizeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.borderColourButton = QtWidgets.QPushButton(self.centralwidget)
        self.borderColourButton.setObjectName("borderColourButton")
        self.horizontalLayout_5.addWidget(self.borderColourButton)
        self.figureColourButton = QtWidgets.QPushButton(self.centralwidget)
        self.figureColourButton.setObjectName("figureColourButton")
        self.horizontalLayout_5.addWidget(self.figureColourButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.borderSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.borderSpinBox.setObjectName("borderSpinBox")
        self.horizontalLayout_4.addWidget(self.borderSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.undoButton = QtWidgets.QPushButton(self.centralwidget)
        self.undoButton.setObjectName("undoButton")
        self.verticalLayout_2.addWidget(self.undoButton)
        self.useMacroButton = QtWidgets.QPushButton(self.centralwidget)
        self.useMacroButton.setObjectName("useMacroButton")
        self.verticalLayout_2.addWidget(self.useMacroButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.macroComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.macroComboBox.setObjectName("macroComboBox")
        self.horizontalLayout_3.addWidget(self.macroComboBox)
        self.executeMacroButton = QtWidgets.QPushButton(self.centralwidget)
        self.executeMacroButton.setObjectName("executeMacroButton")
        self.horizontalLayout_3.addWidget(self.executeMacroButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuJournal = QtWidgets.QMenu(self.menubar)
        self.menuJournal.setObjectName("menuJournal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSaveToFile = QtWidgets.QAction(MainWindow)
        self.actionSaveToFile.setObjectName("actionSaveToFile")
        self.menuHelp.addAction(self.actionAbout)
        self.menuJournal.addAction(self.actionClear)
        self.menuJournal.addAction(self.actionSaveToFile)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuJournal.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.init()

        self._caretaker.Backup()

        self._service.Draw()

        self.sizeSpinBox.setMinimum(5)
        self.sizeSpinBox.setMaximum(100)
        self.sizeSpinBox.setValue(100)

        self.borderSpinBox.setMinimum(1)
        self.borderSpinBox.setMaximum(30)
        self.borderSpinBox.setValue(5)

        self.selectFigure.currentIndexChanged.connect(self.onChangeFigureType)
        self.figureColourButton.clicked.connect(self.onChangeFillColor)
        self.borderColourButton.clicked.connect(self.onChangeBorderColor)
        self.sizeSpinBox.valueChanged.connect(self.onChangeSize)
        self.borderSpinBox.valueChanged.connect(self.onChangeBorderSize)
        self.undoButton.clicked.connect(self.onUndoClick)
        self.useMacroButton.clicked.connect(self.onMacroCommandButton)
        self.executeMacroButton.clicked.connect(self.onStartMacro)

        self.actionAbout.triggered.connect(lambda: self.onAboutClick())
        self.actionClear.triggered.connect(lambda: self.onClearJournal())
        self.actionSaveToFile.triggered.connect(lambda: self.onSaveJournal())

    def init(self):
        self._service = core.Proxy(self.logsPlainText, core.Service(self.figureLabel))
        self._invoker = core.Invoker(self._service)
        self._caretaker = core.Caretaker(self._service)


    def onStartMacro(self):
        i = self.macroComboBox.currentIndex()
        if i>=0 and i < self._invoker.MacroCommandCount():
            self._invoker.ExecuteMacroCommand(i)
            self._caretaker.Backup()

    def onMacroCommandButton(self):
        if self._invoker.MacroCommandBuildStarted():
            self._invoker.StopMacroCommand()
            self.useMacroButton.setText('Using macro command')
            self.macroComboBox.clear()
            for i in range(self._invoker.MacroCommandCount()):
                self.macroComboBox.addItem("Command " + str(i))
        else:
            self._invoker.BeginMacroCommand()
            self.useMacroButton.setText('Stop use macro command')

    def onUndoClick(self):
        self._caretaker.Undo()
        self._caretaker.Backup()

    def onChangeBorderSize(self, size):
        self._invoker.ChangeBorderThickness(size)
        self._caretaker.Backup()

    def onChangeSize(self,  size):
        self._invoker.ChangeSize(size)
        self._caretaker.Backup()

    def onChangeBorderColor(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self._invoker.ChangeBorderColor(color)
            self._caretaker.Backup()

    def onChangeFillColor(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self._invoker.ChangeFillColor(color)
            self._caretaker.Backup()

    def onChangeFigureType(self, newIndex):
        if newIndex == 0:
            self._invoker.SetFigureType('Circle')
        elif newIndex == 1:
            self._invoker.SetFigureType('Triangle')
        elif newIndex == 2:
            self._invoker.SetFigureType('Square')
        elif newIndex == 3:
            self._invoker.SetFigureType('Pentagon')
        elif newIndex == 4:
            self._invoker.SetFigureType('Hexagon')

        self._caretaker.Backup()

    def onSaveJournal(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save file","", "(*.txt)")
        if filename == "":
            return

        text = self.logsPlainText.toPlainText()
        file = open(filename[0], "w+")
        file.write(text)
        file.close()

    def onClearJournal(self):
        self.logsPlainText.clear()

    def onAboutClick(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Осипов Антон Александрович\n 8-T3O-402Б-16\nЛабораторная работа 2")
        msg.addButton('Ok', QtWidgets.QMessageBox.AcceptRole)
        msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.figureLabel.setText(_translate("MainWindow", "TextLabel"))
        self.selectFigure.setItemText(0, _translate("MainWindow", "Circle"))
        self.selectFigure.setItemText(1, _translate("MainWindow", "Regular triangle"))
        self.selectFigure.setItemText(2, _translate("MainWindow", "Square"))
        self.selectFigure.setItemText(3, _translate("MainWindow", "Regular pentagon"))
        self.selectFigure.setItemText(4, _translate("MainWindow", "Regular hexagon"))
        self.label_3.setText(_translate("MainWindow", "Size"))
        self.borderColourButton.setText(_translate("MainWindow", "Border color"))
        self.figureColourButton.setText(_translate("MainWindow", "Figure color"))
        self.label_2.setText(_translate("MainWindow", "Border thickness"))
        self.undoButton.setText(_translate("MainWindow", "Undo"))
        self.useMacroButton.setText(_translate("MainWindow", "Using macro command"))
        self.executeMacroButton.setText(_translate("MainWindow", "Execute macro"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuJournal.setTitle(_translate("MainWindow", "Journal"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSaveToFile.setText(_translate("MainWindow", "Save to file"))