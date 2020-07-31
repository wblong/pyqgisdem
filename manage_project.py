from qgis.core import *
from qgis.core import QgsProject
import os

os.environ['GDAL_DATA'] = r'C:\OSGeo4W\share\gdal'
os.environ['PROJ_LIB'] = r'C:\OSGeo4W\share\proj'
# Supply path to qgis install location
QgsApplication.setPrefixPath(r"C:\OSGeo4W\bin", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()
# Get the project instance
project = QgsProject.instance()
# Print the current project file name (might be empty in case no projects have been loaded)
# print(project.fileName())

# Load another project
print(os.getcwd())
project.read('test.qgs')
# write 
project.write('my_new_qgis_project.qgs')
print(project.fileName())
qgs.exitQgis()