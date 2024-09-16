# BIManalyst group 9
# ARCHITECTURE
# We are checking how many walls thier are in the building 
# We used the pages 21, 23 and 46 
# our script
import ifcopenshell
from bonsai.bim.ifc import IfcStore
file=IfcStore.get_file()
things = file.by_type('IfcWall')
print("Number of",len(things))
