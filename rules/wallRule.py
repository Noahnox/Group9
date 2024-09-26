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

import ifcopenshell
import ifcopenshell.util.element

def calculate_wall_area(ifc_file_path):
    # Load the IFC file
    ifc_file = ifcopenshell.open(ifc_file_path)

    wall_area = 0.0

    # Find all walls in the IFC file
    walls = ifc_file.by_type('IfcWall')

    for wall in walls:
        # Extract the geometry of the wall (using IfcOpenShell utility functions)
        shape = ifcopenshell.util.element.get_geometry(ifc_file, wall)

        # If the geometry exists and contains a valid shape
        if shape:
            for face in shape['faces']:
                # Normal vector and area calculation for each face
                normal = face.normal
                if normal[2] == 0:  # Check if the face normal is aligned with the Z-axis (horizontal)
                    wall_area += face.calc_area()

    return wall_area

# Example usage: Calculate the total wall area
ifc_file_path = "path_to_your_ifc_file.ifc"
total_wall_area = calculate_wall_area(ifc_file_path)
print(f"Total wall area: {total_wall_area:.2f} square meters")
