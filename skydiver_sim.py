import sys
import time
from matplotlib import pyplot as plt
import math
import numpy as np
from decimal import Decimal
import skydive
skydive.__dict__


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 110, 361, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.xAxis = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.xAxis.setObjectName("xAxis")
        self.xAxis.addItem("")
        self.xAxis.addItem("")
        self.xAxis.addItem("")
        self.xAxis.addItem("")
        self.xAxis.addItem("")
        self.xAxis.addItem("")
        self.xAxis.addItem("")
        self.gridLayout.addWidget(self.xAxis, 13, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.BottomTempValue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.BottomTempValue.setObjectName("BottomTempValue")
        self.gridLayout.addWidget(self.BottomTempValue, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TopTempValue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TopTempValue.setObjectName("TopTempValue")
        self.gridLayout.addWidget(self.TopTempValue, 2, 1, 1, 1)
        self.DiverCoef = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DiverCoef.setObjectName("DiverCoef")
        self.gridLayout.addWidget(self.DiverCoef, 6, 1, 1, 1)
        self.CustomGravity = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.CustomGravity.setObjectName("CustomGravity")
        self.gridLayout.addWidget(self.CustomGravity, 10, 2, 1, 1)
        self.ChuteOpenUnit = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.ChuteOpenUnit.setObjectName("ChuteOpenUnit")
        self.ChuteOpenUnit.addItem("")
        self.ChuteOpenUnit.addItem("")
        self.ChuteOpenUnit.addItem("")
        self.ChuteOpenUnit.addItem("")
        self.ChuteOpenUnit.addItem("")
        self.gridLayout.addWidget(self.ChuteOpenUnit, 12, 2, 1, 1)
        self.HumiditySlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.HumiditySlider.setOrientation(QtCore.Qt.Horizontal)
        self.HumiditySlider.setObjectName("HumiditySlider")
        self.HumiditySlider.setRange(0, 100)
        self.HumiditySlider.setValue(20)
        self.HumiditySlider.setSingleStep(5)
        self.HumiditySlider.setTickInterval(10)
        self.HumiditySlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.gridLayout.addWidget(self.HumiditySlider, 4, 1, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.MassValue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.MassValue.setObjectName("MassValue")
        self.gridLayout.addWidget(self.MassValue, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DropheightValue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DropheightValue.setObjectName("DropheightValue")
        self.gridLayout.addWidget(self.DropheightValue, 1, 1, 1, 1)
        self.ChuteCoef = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ChuteCoef.setObjectName("ChuteCoef")
        self.gridLayout.addWidget(self.ChuteCoef, 7, 1, 1, 1)
        self.MassUnit = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.MassUnit.setObjectName("MassUnit")
        self.MassUnit.addItem("")
        self.MassUnit.addItem("")
        self.MassUnit.setItemText(2, "")
        self.gridLayout.addWidget(self.MassUnit, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ChuteOpenValue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ChuteOpenValue.setObjectName("ChuteOpenValue")
        self.gridLayout.addWidget(self.ChuteOpenValue, 12, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TempUnit = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.TempUnit.setObjectName("TempUnit")
        self.TempUnit.addItem("")
        self.TempUnit.addItem("")
        self.TempUnit.addItem("")
        self.gridLayout.addWidget(self.TempUnit, 2, 2, 2, 1)
        self.Planet = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.Planet.setObjectName("Planet")
        self.Planet.addItem("")
        self.Planet.addItem("")
        self.Planet.addItem("")
        self.Planet.addItem("")
        self.Planet.addItem("")
        self.Planet.addItem("")
        self.gridLayout.addWidget(self.Planet, 10, 1, 1, 1)
        self.TimestepValue = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.TimestepValue.setObjectName("TimestepValue")
        self.gridLayout.addWidget(self.TimestepValue, 11, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 13, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DropheightUnit = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.DropheightUnit.setObjectName("DropheightUnit")
        self.DropheightUnit.addItem("")
        self.DropheightUnit.addItem("")
        self.DropheightUnit.addItem("")
        self.gridLayout.addWidget(self.DropheightUnit, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout, 11, 0, 1, 1)
        self.yAxis = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.yAxis.setObjectName("yAxis")
        self.yAxis.addItem("")
        self.yAxis.addItem("")
        self.yAxis.addItem("")
        self.yAxis.addItem("")
        self.yAxis.addItem("")
        self.yAxis.addItem("")
        self.yAxis.addItem("")
        self.gridLayout.addWidget(self.yAxis, 13, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DiverCA = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.DiverCA.setObjectName("DiverCA")
        self.gridLayout.addWidget(self.DiverCA, 8, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)
        self.ChuteCA = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ChuteCA.setObjectName("ChuteCA")
        self.gridLayout.addWidget(self.ChuteCA, 9, 1, 1, 1)
        self.CAUnit = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.CAUnit.setObjectName("CAUnit")
        self.CAUnit.addItem("")
        self.CAUnit.addItem("")
        self.CAUnit.addItem("")
        self.gridLayout.addWidget(self.CAUnit, 8, 2, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 241, 16))
        self.label_6.setObjectName("label_6")
        self.CalculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateButton.setGeometry(QtCore.QRect(270, 530, 75, 23))
        self.CalculateButton.setObjectName("CalculateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.CalculateButton.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Specify Parameters"))
        self.label_2.setText(_translate("MainWindow", "Varun Latthe\'s Skydiver Simulator"))
        self.xAxis.setItemText(0, _translate("MainWindow", "Time"))
        self.xAxis.setItemText(1, _translate("MainWindow", "Air Pressure"))
        self.xAxis.setItemText(2, _translate("MainWindow", "Air Density"))
        self.xAxis.setItemText(3, _translate("MainWindow", "Speed"))
        self.xAxis.setItemText(4, _translate("MainWindow", "Distance"))
        self.xAxis.setItemText(5, _translate("MainWindow", "Altitude"))
        self.xAxis.setItemText(6, _translate("MainWindow", "Acceleration"))
        self.label_4.setText(_translate("MainWindow", "Temperature at Drop Height"))
        self.label_13.setText(_translate("MainWindow", "What Altitude/Time Chute Opens"))
        self.CustomGravity.setText(_translate("MainWindow", "(CustomValue)"))
        self.ChuteOpenUnit.setItemText(0, _translate("MainWindow", "km"))
        self.ChuteOpenUnit.setItemText(1, _translate("MainWindow", "m"))
        self.ChuteOpenUnit.setItemText(2, _translate("MainWindow", "miles"))
        self.ChuteOpenUnit.setItemText(3, _translate("MainWindow", "s"))
        self.ChuteOpenUnit.setItemText(4, _translate("MainWindow", "min"))
        self.label_14.setText(_translate("MainWindow", "Humidity (%)"))
        self.label_3.setText(_translate("MainWindow", "Drop Height"))
        self.label_5.setText(_translate("MainWindow", "Temperature at Sea Level"))
        self.MassUnit.setItemText(0, _translate("MainWindow", "kg"))
        self.MassUnit.setItemText(1, _translate("MainWindow", "lb"))
        self.label_7.setText(_translate("MainWindow", "Mass (of diver and chute combined)"))
        self.label_8.setText(_translate("MainWindow", "Drag Coefficient of Diver"))
        self.label_9.setText(_translate("MainWindow", "Drag Coefficient of Parachute"))
        self.TempUnit.setItemText(0, _translate("MainWindow", "Celcius"))
        self.TempUnit.setItemText(1, _translate("MainWindow", "Fahrenheit"))
        self.TempUnit.setItemText(2, _translate("MainWindow", "Kelvin"))
        self.Planet.setItemText(0, _translate("MainWindow", "Earth"))
        self.Planet.setItemText(1, _translate("MainWindow", "Moon"))
        self.Planet.setItemText(2, _translate("MainWindow", "Mars"))
        self.Planet.setItemText(3, _translate("MainWindow", "Jupiter"))
        self.Planet.setItemText(4, _translate("MainWindow", "Neptune"))
        self.Planet.setItemText(5, _translate("MainWindow", "Custom(m/s)"))
        self.label_10.setText(_translate("MainWindow", "Gravity Strength (by Planet)"))
        self.label_15.setText(_translate("MainWindow", "X-axis - Y Axis on graph"))
        self.DropheightUnit.setItemText(0, _translate("MainWindow", "km"))
        self.DropheightUnit.setItemText(1, _translate("MainWindow", "miles"))
        self.DropheightUnit.setItemText(2, _translate("MainWindow", "m"))
        self.label_11.setText(_translate("MainWindow", "Timestep (s)"))
        self.label_12.setText(_translate("MainWindow", "( lower = more accurate but slower)"))
        self.yAxis.setItemText(0, _translate("MainWindow", "Time"))
        self.yAxis.setItemText(1, _translate("MainWindow", "Air Pressure"))
        self.yAxis.setItemText(2, _translate("MainWindow", "Air Density"))
        self.yAxis.setItemText(3, _translate("MainWindow", "Speed"))
        self.yAxis.setItemText(4, _translate("MainWindow", "Distance"))
        self.yAxis.setItemText(5, _translate("MainWindow", "Altitude"))
        self.yAxis.setItemText(6, _translate("MainWindow", "Acceleration"))
        self.label_16.setText(_translate("MainWindow", "Cross-Sectional Area of Diver"))
        self.label_17.setText(_translate("MainWindow", "Cross Sectional Area of Parachute"))
        self.CAUnit.setItemText(0, _translate("MainWindow", "m^2"))
        self.CAUnit.setItemText(1, _translate("MainWindow", "inch^2"))
        self.CAUnit.setItemText(2, _translate("MainWindow", "feet^2"))
        self.label_6.setText(_translate("MainWindow", "Leave Blank for Default Value (if you are unsure)"))
        self.CalculateButton.setText(_translate("MainWindow", "Calculate"))

    def getdropheight(self):
        value = self.DropheightValue.text()
        unit = self.DropheightUnit.currentText()    
        if value == "":
            value = 5000
        else:
            value = float(self.DropheightValue.text())
            if unit == "km":
                value = value*1000
            elif unit == "miles":
                value = value*1609.34
        return value
    
    def gettemps(self):
        unit = self.TempUnit.currentText()
        t1 = self.TopTempValue.text()
        t2 = self.BottomTempValue.text()
        if t1 == "":
            t1 = 263.15
        else:
            t1 = float(self.TopTempValue.text())
            if unit == "Celcius":
                t1 = t1 + 273.15
            elif unit == "Fahrenheit":
                t1 = (t1 - 32)*(5/9) + 273.15    
        if t2 == "":
            t2 = 293.15
        else:
            t2 = float(self.BottomTempValue.text())
            if unit == "Celcius":
                t2 = t2 + 273.15
            elif unit == "Fahrenheit":
                t2 = (t2 - 32)*(5/9) + 273.15
        return (t1,t2)
            
    def getareas(self):
        unit = self.CAUnit.currentText()
        divervalue = self.DiverCA.text()
        chutevalue = self.ChuteCA.text()
        if divervalue == "":
            divervalue = 0.7
        else:
            divervalue = float(self.DiverCA.text())
            if unit == "feet^2":
                divervalue = divervalue/10.7639
            elif unit == "inch ^2":
                divervalue = divervalue/1550
        if chutevalue == "":
            chutevalue = 5
        else:
            chutevalue = float(self.ChuteCA.text())
            if unit == "feet^2":
                chutevalue = chutevalue/10.7639
            elif unit == "inch ^2":
                chutevalue = chutevalue/1550
        return divervalue, chutevalue

    def getcoefs(self):
        divercoef = self.DiverCoef.text()
        chutecoef = self.ChuteCoef.text()
        if divercoef == "":
            divercoef = 0.7
        else:
            divercoef = float(self.DiverCoef.text())
        if chutecoef == "":
            chutecoef = 2
        else:
            chutecoef = float(self.ChuteCoef.text())
        return divercoef, chutecoef
            
        

    
    def getgravity(self):
        p = self.Planet.currentText()
        if p == "Custom(m/s)":
            gravity = float(self.CustomGravity.text())
        elif p == "Earth":
            gravity = 9.81
        elif p == "Moon":
            gravity = 1.62
        elif p == "Mars":
            gravity = 3.711
        elif p == "Jupiter":
            gravity = 24.79
        else:
            gravity = 11.15
        return gravity

    def gethumidity(self):
        humidity = self.HumiditySlider.value()
        humidity = humidity/100
        return humidity

    def getmass(self):
        unit = self.MassUnit.currentText()
        value = self.MassValue.text()

        if value == "":
            value = 90
        else:
            value = float(self.MassValue.text())
            if unit == "lb":
                value = value/2.205
        return value

    def gettimestep(self):
        t = self.TimestepValue.text()
        if t == "":
            t= 0.1
        else:
            t = float(self.TimestepValue.text())
        return t

    def getchuteopen(self):
        value = self.ChuteOpenValue.text()
        unit = self.ChuteOpenUnit.currentText()
        if unit == "s":
            chutetimeoralt = "time"
            if value == "":
                value =  45
            else:
                value = float(self.ChuteOpenValue.text())
        elif unit == "min":
            chutetimeoralt = "time"
            if value == "":
                value = 45
            else:
                value = float(self.ChuteOpenValue.text())
                value = value*60
        elif unit == "miles":
            chutetimeoralt = "altitude"
            if value == "":
                value = 1000
            else:
                value = float(self.ChuteOpenValue.text())
                value = value*1609
        elif unit == "m":
            chutetimeoralt = "altitude"
            if value == "":
                value = 1000
            else:
                value = float(self.ChuteOpenValue.text())
        elif unit == "km":
            chutetimeoralt = "altitude"
            if value == "":
                value = 1000
            else:
                value = float(self.ChuteOpenValue.text())
                value = value*1000
        return value, chutetimeoralt

    def getaxis(self):
        x = self.xAxis.currentText()
        y = self.yAxis.currentText()
        return x,y
            

    def calculate(self):
        dropheight = self.getdropheight()
        toptemp, bottomtemp = self.gettemps()
        gravity = self.getgravity()
        cabefore, caafter = self.getareas()
        divercoef, chutecoef = self.getcoefs()
        timestep = self.gettimestep()
        mass = self.getmass()
        humidity = self.gethumidity()
        chuteopen, chutetimeoralt = self.getchuteopen()
        x,y = self.getaxis()
        execute(dropheight, toptemp, bottomtemp, gravity, cabefore,caafter, divercoef, chutecoef, timestep, mass, humidity, chuteopen, chutetimeoralt, x, y)


# def getaltitude(dropheight, distance):
#     return dropheight - distance

# def getairpressure(altitude, gravity, temp):
#     return 101325*math.exp(-gravity*0.0289644*((altitude)/(8.31432*temp)))

# def getvapourpressure(humidity, pressure):
#     return pressure*humidity

# def getdrypressure(vapourpressure, pressure):
#     return pressure - vapourpressure

# def getdensity(vapourpressure, drypressure, temp):
#     return ((drypressure/(287.058*temp))+(vapourpressure/(461.495*temp)))

# def getweight(mass, gravity):
#     return mass*gravity

# def getforce(gravity, density, velocity, cabefore, caafter, divercoef, chutecoef, mass, chuteopen, chutetimeoralt, time, altitude):
#     weight = getweight(mass, gravity)
#     drag = getdrag(density, velocity, cabefore, caafter, divercoef, chutecoef, chuteopen, chutetimeoralt, time, altitude)
#     return weight - drag
    

# def getdrag(density, velocity, cabefore, caafter, divercoef, chutecoef, chuteopen, chutetimeoralt, time, altitude):
#     if chutetimeoralt == "time":
#         if chuteopen < time:
#             coef = chutecoef
#             area = caafter
#             return 0.5*coef*density*(velocity**2)*area
#         else:
#             coef = divercoef
#             area = cabefore
#             return 0.5*coef*density*(velocity**2)*area
#     elif chutetimeoralt == "altitude":
#         if chuteopen < altitude:
#             coef = divercoef
#             area = cabefore
#             return 0.5*coef*density*(velocity**2)*area
#         else:
#             coef = chutecoef
#             area = caafter
#             return 0.5*coef*density*(velocity**2)*area
    
    



# def getacceleration(gravity, density, velocity, cabefore, caafter, divercoef, chutecoef, mass, chuteopen, chutetimeoralt, time, altitude):
#     if altitude > 0:
#         return getforce(gravity, density, velocity, cabefore, caafter, divercoef, chutecoef, mass, chuteopen, chutetimeoralt, time, altitude)/mass
#     else:
#         return 0
    
# def getvelocity(velocity, acceleration, timestep, altitude):
#     if altitude > 0:
#         return velocity + (acceleration*timestep)
#     else:
#         return 0

def execute(dropheight, toptemp, bottomtemp, gravity, cabefore, caafter, divercoef, chutecoef, timestep, mass, humidity, chuteopen, chutetimeoralt, x, y):
    # timefinished = float("inf")
    # currentdistance = 0
    # currentvelocity = 0
    # currentacceleration = 0
    # currenttime = 0
    # currentpressure = 123
    # currentdensity = 0
    # currentaltitude = 0
    # currenttemp = 0
    # currentvapourpressure = 0
    # currentdrypressure = 0
    # time = []
    # velocity = []
    # acceleration = []
    # distance = []
    # pressure = []
    # density = []
    # temp = []
    # altitude = []
    # vapourpressure = []
    # drypressure = []
    # while currenttime-10 < timefinished:
    #     currentaltitude = getaltitude(dropheight, currentdistance)
    #     altitude.append(currentaltitude)
    #     currenttemp = gettemp(toptemp, bottomtemp, dropheight, currentaltitude)
    #     temp.append(currenttemp)
    #     currentpressure = getairpressure(currentaltitude, gravity, currenttemp)
    #     pressure.append(currentpressure)
    #     currentvapourpressure = getvapourpressure(humidity, currentpressure)
    #     vapourpressure.append(currentvapourpressure)
    #     currentdrypressure = getdrypressure(currentvapourpressure, currentpressure)
    #     drypressure.append(currentdrypressure)
    #     currentdensity = getdensity(currentvapourpressure, currentdrypressure, currenttemp)
    #     density.append(currentdensity)
    #     currentacceleration = getacceleration(gravity, currentdensity, currentvelocity, cabefore, caafter, divercoef, chutecoef, mass, chuteopen, chutetimeoralt, currenttime, currentaltitude)
    #     acceleration.append(currentacceleration)
    #     currenttime = currenttime+timestep
    #     time.append(currenttime)
    #     currentvelocity = getvelocity(currentvelocity, currentacceleration, timestep, currentaltitude)
    #     velocity.append(currentvelocity)
    #     currentdistance = currentdistance + (currentvelocity*timestep)
    #     distance.append(currentdistance)
    #     if currentvelocity == 0:
    #         currenttime = timefinished
    out = skydive.process_data(dropheight, toptemp, bottomtemp, gravity, cabefore, caafter, divercoef, chutecoef, timestep, mass, humidity, chuteopen, chutetimeoralt,)
    time = out[0]
    velocity = out[1]
    acceleration = out[2]
    distance = out[3]                   
    pressure = out[4]
    density = out[5]
    temp = out[6]
    altitude = out[7]
    vapourpressure = out[8]
    drypressure = out[9]
    plot(time, velocity, acceleration, distance, pressure, density, temp, altitude, vapourpressure, drypressure, x, y)



        
# def gettemp(toptemp, bottomtemp, dropheight, altitude):
#     percentage = altitude/dropheight
#     dif = toptemp - bottomtemp
#     toadd = percentage*dif
#     return bottomtemp + toadd

def plot(time, velocity, acceleration, distance, pressure, density, temp, altitude, vapourpressure, drypressure, x, y):
    if x.lower() == "time":
        x = time
        xlabel = "Time (s)"
    elif x.lower() == "speed":
        x = velocity
        xlabel = "Velocity (m/s)"
    elif x.lower() == "acceleration":
        x = acceleration
        xlabel = "Acceleration (m/s^2)"
    elif x.lower() == "distance":
        x = distance
        xlabel = "Distance Travelled (m)"
    elif x.lower() == "air pressure":
        x = pressure
        xlabel = "Air Pressure (kPa)"
    elif x.lower() == "air density":
        x = density
        xlabel = "Air Density (kg/m^3)"
    elif x.lower() == "temperature":
        x = temp
        xlabel = "Temperature (K)"
    elif x.lower() == "altitude":
        x = altitude
        xlabel = "Altitude (m)"
    else: xlabel = "undefined"
    if y.lower() == "time":
        y = time
        ylabel = "Time (s)"
    elif y.lower() == "speed":
        y = velocity
        ylabel = "Velocity (m/s)"
    elif y.lower() == "acceleration":
        y = acceleration
        ylabel = "Acceleration (m/s^2)"
    elif y.lower() == "distance":
        y = distance
        ylabel = "Distance Travelled (m)"
    elif y.lower() == "air pressure":
        y = pressure
        ylabel = "Air Pressure (kPa)"
    elif y.lower() == "air density":
        y = density
        ylabel = "Air Density (kg/m^3)"
    elif y.lower() == "temperature":
        y = temp
        ylabel = "Temperature (K)"
    elif y.lower() == "altitude":
        y = altitude
        ylabel = "Altitude (m)"
    else: ylabel = "undefined"
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title("Your Skydive")
    plt.style.use("ggplot")
    plt.tight_layout()
    plt.show()

    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())