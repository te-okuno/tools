# coding: utf-8

import maya.cmds as cmds
from PySide2 import QtWidgets
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

class WidgetItems(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetItems, self).__init__(parent)

        mainLayout = QtWidgets.QVBoxLayout(self)

        ## widget
        self.reloadBtn = QtWidgets.QPushButton('Reload')
        lab = QtWidgets.QLabel('Object Name List')
        self.cnt = QtWidgets.QLabel('Selected : ')
        self.listWidget = QtWidgets.QListWidget()
        self.selBtn = QtWidgets.QPushButton('Select')

        ## layout
        mainLayout.addWidget(self.reloadBtn)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(lab)
        layout.addWidget(self.cnt)
        mainLayout.addLayout(layout)
        mainLayout.addWidget(self.listWidget)
        mainLayout.addWidget(self.selBtn)


class ObjListWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ObjListWindow, self).__init__(maya_mainWindow())

        child_list = self.parent().children()
        for c in child_list:
            if self.__class__.__name__ == c.__class__.__name__:
                c.close()

        self.ui = WidgetItems(parent)
        self.setCentralWidget(self.ui)

        self.dict = dict()
        self.connect()
        self.setObjList()

        self.setWindowTitle('Store Selected Components')
        self.resize(300, 300)
        self.show()


    def connect(self):
        self.ui.reloadBtn.clicked.connect(self.setObjList)
        self.ui.listWidget.itemClicked.connect(self.showFaceCount)
        self.ui.listWidget.itemDoubleClicked.connect(self.selObj)
        self.ui.selBtn.clicked.connect(self.selFaces)

    def showFaceCount(self, item):
        '''Single Click'''
        faceCount = len(self.dict[item.text()])
        self.ui.cnt.setText('Selected : ' + str(faceCount))


    def selObj(self, item):
        '''Double Click'''
        cmds.select(item.text(), r=1)


    def setObjList(self):
        ## clear
        self.ui.listWidget.clear()
        self.dict = dict()
        self.ui.cnt.setText('Selected : ')

        sel = cmds.ls(sl=1, fl=1)

        for i in sel:
            name = i.split('.')

            if self.dict.get(name[0]) is None:
                self.dict[name[0]] = []
                self.dict[name[0]].append(i)
            else:
                self.dict[name[0]].append(i)

        if self.dict:
            for obj in self.dict.keys():
                self.ui.listWidget.addItem(obj)


    def selFaces(self):
        '''Select Button'''
        obj = self.ui.listWidget.currentItem()
        if obj is not None:
            cmds.select(self.dict[obj.text()], r=1)


def maya_mainWindow():
    import maya.OpenMayaUI as OpenMayaUI
    try:
        import shiboken2 as shiboken
    except:
        import shiboken

    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(ptr), QtWidgets.QWidget)