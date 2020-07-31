import os
from qgis.PyQt.QtWidgets import QAction,QMainWindow
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QColor
from qgis.core import (
    QgsProject,
    QgsApplication,
    QgsPoint,
    QgsPointXY,
    QgsGeometry,
    QgsRectangle,
    QgsMessageLog,
    Qgis
)
from qgis.gui import(
    QgsMapCanvas,
    QgsRubberBand,
    QgsVertexMarker,
    QgsMessageLogViewer,
    QgsDockWidget
)
os.environ['GDAL_DATA'] = r'C:\OSGeo4W\share\gdal'
os.environ['PROJ_LIB'] = r'C:\OSGeo4W\share\proj'
# Supply path to qgis install location
QgsApplication.setPrefixPath(r"C:\OSGeo4W\apps\qgis-ltr", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], True)

# Load providers
qgs.initQgis()
# win
mainWindow=QMainWindow()
# gui
canvas = QgsMapCanvas()
mainWindow.setCentralWidget(canvas)
logView = QgsMessageLogViewer()
dWidget = QgsDockWidget()
dWidget.setWidget(logView)
mainWindow.addDockWidget(Qt.RightDockWidgetArea, dWidget)
mainWindow.show()
# log
QgsMessageLog.logMessage("message 101.", level=Qgis.Info)
QgsMessageLog.logMessage("message 101.", level=Qgis.Info)
QgsMessageLog.logMessage("message 102.", level=Qgis.Warning)
QgsMessageLog.logMessage("message 103.", level=Qgis.Critical)
# draw line
r = QgsRubberBand(canvas, False)  # False = not a polygon
r.setWidth(2)
r.setColor(QColor(255,0,0))
points = [QgsPoint(-100, 45), QgsPoint(10, 60), QgsPoint(120, 45)]
r.setToGeometry(QgsGeometry.fromPolyline(points), None)
QgsMessageLog.logMessage("draw red line", level=Qgis.Info)
# draw polygon
r = QgsRubberBand(canvas, True)
r.setColor(QColor(255,255,0))
points = [[QgsPointXY(110, 30), QgsPointXY(130, 45), QgsPointXY(130, 20)]]
r.setToGeometry(QgsGeometry.fromPolygonXY(points), None)
QgsMessageLog.logMessage("draw yellow polygon", level=Qgis.Info)
# draw marker
m = QgsVertexMarker(canvas)
m.setCenter(QgsPointXY(129.5, 39.0))
m.setColor(QColor(0, 255, 0))
m.setIconSize(5)
m.setIconType(QgsVertexMarker.ICON_BOX)
m.setPenWidth(3)
QgsMessageLog.logMessage("draw green marker", level=Qgis.Info)
# refresh
canvas.setExtent(QgsRectangle(-200,0, 200,100))
exitCode = qgs.exec()
qgs.exitQgis()