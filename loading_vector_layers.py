import os
from qgis.core import (
    QgsVectorLayer,
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
# get the path to the shapefile 
path_to_airports_layer = "./data/cities.shp"

# The format is:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(path_to_airports_layer, "cities", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)

canvas.setExtent(vlayer.extent())
canvas.setLayers([vlayer])
exitCode = qgs.exec()
qgs.exitQgis()