import sys,os
from qgis.core import QgsApplication
from qgis.gui import QgsMapCanvas

os.environ['GDAL_DATA'] = r'C:\OSGeo4W\share\gdal'
os.environ['PROJ_LIB'] = r'C:\OSGeo4W\share\proj'
def init():
  a = QgsApplication([], True)
  QgsApplication.setPrefixPath('qgis', True)
  QgsApplication.initQgis()
  return a

def show_canvas(app):
  canvas = QgsMapCanvas()
  canvas.show()
  app.exec_()
app = init()
show_canvas(app)
