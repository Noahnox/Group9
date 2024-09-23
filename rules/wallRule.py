import ifcopenshell
model = ifcopenshell.open('/path/to/your/model.ifc')

walls = model.by_type('IfcWall')
print(f"Walls in model: {len(walls)}")
