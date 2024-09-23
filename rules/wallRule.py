import ifcopenshell
model = ifcopenshell.open('C:\Users\noahw\OneDrive\Skrivbord\model')

walls = model.by_type('IfcWall')
print(f"Walls in model: {len(walls)}")
