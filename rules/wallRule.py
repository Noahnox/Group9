import ifcopenshell
#model = ifcopenshell.open('C:\Users\noahw\OneDrive\Skrivbord\model')

def num_walls_flors(model):
  wall = model.by_type('Ifcwall') 
print("Number of walls:",len(wall))

floor = model.by_type('IfcBuildingstorey')
print("Number of floors:",len(floor))
