from zope.interface import Interface, Attribute, implementer
from PyQt5 import QtWidgets,QtCore, QtGui
import math

class IMemento(Interface):
    def GetState(self):
        ''''''

@implementer(IMemento)
class ConcreteMemento(object):
    _state = ""

    def __init__(self, state):
        self._state = state

    def GetState(self):
        return self._state


class IService(Interface):
    def SetFigureType(self, type):
        ''''''
    def ChangeSize(self, size):
        ''''''
    def ChangeBorderColour(self, color):
        ''''''
    def ChangeFillColor(self, color):
        ''''''
    def ChangeBorderThickness(self, thickness):
        ''''''
    def Save(self):
        ''''''
    def Restore(self, memento):
        ''''''
    def Draw(self):
        ''''''

@implementer(IService)
class Service(object):
    _width = 400
    _height = 400
    _size = 100
    _borderThickeness = 5
    _fillColor = QtGui.QColor('white')
    _borderColor = QtGui.QColor('black')
    _type = "Circle"
    _label = None

    def __init__(self, label):
        self._label = label

    def SetFigureType(self, type):
        self._type = type
        self.Draw()

    def SetSize(self, size):
        self._size = size
        self.Draw()

    def SetBorderColor(self, borderColor):
        self._borderColor = borderColor
        self.Draw()

    def SetFillColor(self, fillColor):
        self._fillColor = fillColor
        self.Draw()

    def SetBorderThickness(self, borderThickness):
        self._borderThickeness = borderThickness
        self.Draw()

    def Save(self):
        color1 = self._fillColor.rgba()
        color2 = self._borderColor.rgba()

        memento = str(self._size) + " " + str(self._borderThickeness) + " " + str(self._type) + " " +\
                str(color1) + " " \
                + str(color2)


        return memento

    def Restore(self, memento):
        data = memento.split()
        self._size = int(data[0])
        self._borderThickeness = int(data[1])
        self._type = data[2]
        color =  QtGui.QColor()
        color.setRgba(int(data[3]))
        self._fillColor = color
        color2 = QtGui.QColor()
        color2.setRgba(int(data[4]))
        self._borderColor = color2
        self.Draw()

    def Draw(self):
        pixmap = QtGui.QPixmap(self._width, self._height)
        pixmap.fill(QtGui.QColor('white'))
        painter = QtGui.QPainter()
        painter.begin(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
        painter.fillRect(0,0,self._width, self._height, QtGui.QBrush(QtGui.QColor('white')))
        painter.setPen(QtGui.QPen(self._borderColor, self._borderThickeness))

        painter.setBrush(QtGui.QBrush(self._fillColor))

        if self._type == 'Circle':
            self.DrawCircle(painter)
        elif self._type == 'Triangle':
            self.DrawPath(painter, 3)
        elif self._type == 'Square':
            self.DrawPath(painter, 4)
        elif self._type == 'Pentagon':
            self.DrawPath(painter, 5)
        elif self._type == 'Hexagon':
            self.DrawPath(painter, 6)
        #
        painter.end()
        self._label.setPixmap(pixmap)
        self._label.setMinimumSize(self._width, self._height)

    def DrawCircle(self, painter):
        painter.drawEllipse((self._width / 2) - self._size, (self._height / 2) - self._size, self._size * 2, self._size * 2)

    def DrawPath(self, painter, pointsNumber):
        point = QtCore.QPoint(0, -self._size)
        path = QtGui.QPainterPath()

        path.moveTo((self._width / 2) + point.x(), (self._height / 2) + point.y())
        for i in range(pointsNumber):
            point = self.rotatePoint(point, (2 * math.pi) / pointsNumber)
            path.lineTo((self._width / 2) + point.x(), (self._height / 2) + point.y())

        painter.drawPath(path)

    def rotatePoint(self, point, radian):
        cos = math.cos(radian)
        sin = math.sin(radian)
        return QtCore.QPoint(point.x() * cos - point.y() * sin, point.x() * sin + point.y() * cos)

class Caretaker():
    _service = None
    _mementos = []

    def __init__(self, service):
        self._service = service

    def Undo(self):
        if len(self._mementos) == 0:
            return
        if len(self._mementos) == 1:
            self._service.Restore(self._mementos[0])
            return

        self._mementos.pop()
        self._service.Restore(self._mementos[len(self._mementos) - 1])

    def Backup(self):
        self._mementos.append(self._service.Save())


@implementer(IService)
class Proxy(object):
    _service = None
    _textEdit = None

    def __init__(self, textEdit, service):
        self._service = service
        self._textEdit = textEdit

    def SetFigureType(self,type):
        self._textEdit.insertPlainText("Update figure type\n")
        self._service.SetFigureType(type)

    def ChangeSize(self, size):
        self._textEdit.insertPlainText("Update size\n")
        self._service.SetSize(size)

    def ChangeBorderColor(self, color):
        self._textEdit.insertPlainText("Update border color\n")
        self._service.SetBorderColor(color)

    def ChangeFillColor(self, color):
        self._textEdit.insertPlainText("Update fill color\n")
        self._service.SetFillColor(color)

    def ChangeBorderThickness(self, thickness):
        self._textEdit.insertPlainText("Update border thickness\n")
        self._service.SetBorderThickness(thickness)

    def Save(self):
        return self._service.Save()

    def Restore(self, memento):
        self._service.Restore(memento)

    def Draw(self):
        self._service.Draw()


class ICommand(Interface):
    def Execute(self):
        ''''''

@implementer(ICommand)
class SetFigureTypeCommand(object):
    _service = None
    _type = ""

    def __init__(self, service, type):
        self._service = service
        self._type = type

    def Execute(self):
        self._service.SetFigureType(self._type)

@implementer(ICommand)
class ChangeSizeCommand(object):
    _service = None
    _size = 0

    def __init__(self, service, size):
        self._service = service
        self._size = size

    def Execute(self):
        self._service.ChangeSize(self._size)


@implementer(ICommand)
class ChangeBorderColorCommand(object):
    _service = None
    _color = None

    def __init__(self, service, color):
        self._service = service
        self._color = color

    def Execute(self):
        self._service.ChangeBorderColor(self._color)


@implementer(ICommand)
class ChangeFillColorCommand(object):
    _service = None
    _color = None

    def __init__(self, service, color):
        self._service = service
        self._color = color

    def Execute(self):
        self._service.ChangeFillColor(self._color)


@implementer(ICommand)
class ChangeBorderThicknessCommand(object):
    _service = None
    _thickness = 0

    def __init__(self, service, thickness):
        self._service = service
        self._thickness = thickness

    def Execute(self):
        self._service.ChangeBorderThickness(self._thickness)


@implementer(ICommand)
class MacroCommand(object):
    _commands = []

    def __init__(self, commands):
        self._commands = commands

    def Execute(self):
        for command in self._commands:
            command.Execute()


class Invoker():
    _service = None
    _macroCommands = []
    _currentMacroCommands = []
    _macroCommandBuildStarted = False

    def __init__(self, service):
        self._service = service

    def SetFigureType(self, type):
        command = SetFigureTypeCommand(self._service, type)
        if self._macroCommandBuildStarted:
            self._currentMacroCommands.append(command)

        command.Execute()

    def ChangeSize(self, size):
        command = ChangeSizeCommand(self._service, size)
        if self._macroCommandBuildStarted:
            self._currentMacroCommands.append(command)

        command.Execute()

    def ChangeBorderColor(self, color):
        command = ChangeBorderColorCommand(self._service, color)
        if self._macroCommandBuildStarted:
            self._currentMacroCommands.append(command)

        command.Execute()

    def ChangeFillColor(self, color):
        command = ChangeFillColorCommand(self._service, color)
        if self._macroCommandBuildStarted:
            self._currentMacroCommands.append(command)

        command.Execute()

    def ChangeBorderThickness(self, thickness):
        command = ChangeBorderThicknessCommand(self._service, thickness)
        if self._macroCommandBuildStarted:
            self._currentMacroCommands.append(command)

        command.Execute()

    def MacroCommandBuildStarted(self):
        return self._macroCommandBuildStarted

    def BeginMacroCommand(self):
        self._macroCommandBuildStarted = True
        self._currentMacroCommands.clear()

    def MacroCommandCount(self):
        return len(self._macroCommands)

    def ExecuteMacroCommand(self, index):
        if index >= len(self._macroCommands):
            return

        self._macroCommands[index].Execute()

    def StopMacroCommand(self):
        if len(self._currentMacroCommands) != 0:
            command = MacroCommand(self._currentMacroCommands)
            self._macroCommands.append(command)

        self._macroCommandBuildStarted = False
        self._currentMacroCommands = []