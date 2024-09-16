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

# Here are some code about amount of floors, walls and walls area
import ifcopenshell
from bonsai.bim.ifc import IfcStore
file=IfcStore.get_file()
wall = file.by_type('IfcWall')
print("Number of walls:",len(wall))

floor = file.by_type('IfcBuildingStorey')
print("Number of floors:",len(floor))

import bpy
import bmesh

def calculate_wall_area():
    wall_area = 0.0
    
    # Iterate through all mesh objects in the scene
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            # Ensure we are dealing with a mesh
            mesh = obj.data
            
            # Create a BMesh from the mesh
            bm = bmesh.new()
            bm.from_mesh(mesh)
            
            # Iterate through all faces in the BMesh
            for face in bm.faces:
                # Check if the face normal is aligned with the Z axis (walls)
                if face.normal.z != 0:  # You can adjust the condition as needed
                    wall_area += face.calc_area()
            
            # Free the BMesh
            bm.free()
    
    return wall_area

# Calculate wall area and print it
total_wall_area = calculate_wall_area()
print(f"Total wall area: {total_wall_area:.2f} square meters")
