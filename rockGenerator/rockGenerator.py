import hou
import os
from PySide2 import QtWidgets, QtUiTools
from PySide2.QtCore import Qt

script_path = os.path.dirname(__file__)

class RockGenerator(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(RockGenerator, self).__init__(parent)

        self.node = None

        #UI loader

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(script_path + "/rockGenerator.ui")

        #find widgets

        self.image = self.ui.findChild(QtWidgets.QLabel, "image")

        self.rangeScale = self.ui.findChild(QtWidgets.QSlider, "rangeScale")
        self.numSections = self.ui.findChild(QtWidgets.QSlider, "numSections")
        self.minRot = self.ui.findChild(QtWidgets.QSlider, "minRot")
        self.maxRot = self.ui.findChild(QtWidgets.QSlider, "maxRot")

        self.highBtn = self.ui.findChild(QtWidgets.QPushButton, "highBtn")

        self.voxelVal = self.ui.findChild(QtWidgets.QDoubleSpinBox, "voxelVal")

        #set img
        self.image.setPixmap(script_path + "/Rock.png")

        #layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)

        #Connections with widgets

        self.highBtn.clicked.connect(self.sayHello)

        self.rangeScale.valueChanged.connect(lambda: self.modifySilder("range", self.rangeScale.value()))
        self.numSections.valueChanged.connect(lambda: self.modifySilder("sections", self.numSections.value()))
        self.minRot.valueChanged.connect(lambda: self.modifySilder("minrot", self.minRot.value()))
        self.maxRot.valueChanged.connect(lambda: self.modifySilder("maxrot", self.maxRot.value()))
        self.voxelVal.valueChanged.connect(lambda: self.modifySilder("voxelval", self.voxelVal.value()))

        #set layout
        self.setLayout(self.layout)

    def sayHello(self):
        print("This is working")

    def setCurrentNode(self, node):
        self.node = node
        print("Current node is", node)

    def modifySilder(self, attr, value):
        path = self.node.path()

        if attr == "range":
            hou.parm(path + '/transform5/scale').set(value * 0.01)
        
        elif attr == "sections":
            hou.parm(path + '/scatter2/npts').set(value + 1)

        elif attr == "minrot":
            hou.parm(path + '/transform6/rotmin').set(value + 1)
        elif attr == "maxrot":
            hou.parm(path + '/transform6/rotmax').set(value + 1)
        elif attr == "voxelval":
            hou.parm(path + '/vdbfrompolygons1/newparameter').set(value)

