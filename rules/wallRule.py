import ifcopenshell
model = ifcopenshell.open('C:\Users\noahw\OneDrive\Skrivbord\model')

walls = model.by_type('IfcWall')
print(f"Walls in model: {len(walls)}")

####Script#####
import os

# Clearing the Screen
os.system('cls')

import ifcopenshell
from bonsai.bim.ifc import IfcStore
file=IfcStore.get_file()
wall = file.by_type('IfcWall')
print("Number of walls:",len(wall))

floor = file.by_type('IfcBuildingStorey')
print("Number of floors:",len(floor))
