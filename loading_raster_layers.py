import os
from qgis.core import (
    QgsRasterLayer,
    QgsProject,
    QgsApplication
)
from qgis.gui import(
    QgsMapCanvas
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
# gui
canvas = QgsMapCanvas()
canvas.show()
# get the path to a tif file
path_to_tif = "./data/landuse.tif"
rlayer = QgsRasterLayer(path_to_tif, "landuse")
if not rlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(rlayer)

canvas.setExtent(rlayer.extent())
canvas.setLayers([rlayer])
exitCode = qgs.exec()
qgs.exitQgis()