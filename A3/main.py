# pip install ifcopenshell 

from importlib.metadata import files
import ifcopenshell

model = ifcopenshell.open("C:/Users/noahw/OneDrive/Skrivbord/model/.ifc") 

# Find all IfcBuildingStorey entities
storeys = model.by_type('IfcBuildingStorey')

# Initialize variables for the ground floor and topmost floor
ground_floor = None
topmost_floor = None

# Initialize variables for the ground floor
ground_floor = None
floor_count = 0

# Define a tolerance for what is considered "close to 0.0"
tolerance = 0.01

# Loop through each storey to identify ground floor and topmost floor
for storey in storeys:
    elevation = storey.Elevation  # Get the elevation attribute
   
    # Check if elevation exists
    if elevation is None:
        continue  # Skip if there's no elevation attribute

    # Identify the ground floor (try different names and check for near-zero elevation)
    if ground_floor is None and (storey.Name in ["Ground Floor", "Level 0", "Ground"] or abs(elevation) < tolerance):
        ground_floor = storey

    # Update the topmost floor by finding the storey with the highest elevation
    if topmost_floor is None or elevation > topmost_floor.Elevation:
        topmost_floor = storey

# Calculate building height if both floors are found
if ground_floor and topmost_floor:
    building_height = topmost_floor.Elevation - ground_floor.Elevation
    
    if building_height > 1000:
        building_height /= 1000

    print(f"The building height from the ground floor is: {building_height} meters.")
else:
    print("Ground floor or topmost floor not identified.")

# If ground floor is identified, count floors above it
if ground_floor:
    ground_floor_elevation = ground_floor.Elevation

    # Count all floors above the ground floor elevation
    for storey in storeys:
        if storey.Elevation is not None and storey.Elevation > ground_floor_elevation:
            floor_count += 1

    print(f"The number of floors above the ground floor is: {floor_count}")
else:
    print("Ground floor not identified.")


# if the total building height is under or 12 meters or if the toatal number of floors are les then 4. 
if building_height < 12 or floor_count < 4:
    print("Staircase 1 in the building must be an independent fire compartment with a minimum fire resistance rating of EI 60.")
# if the total building height is more than 12 meters and less than or equal to 23 meters or if the total number of floors is more than 4 and less than or equal to 8.
elif 12 < building_height < 23 or 4 < floor_count < 8: 
    print("Staircase 2 in the building must be an independent fire compartment with a minimum fire-resistance rating of EI 60. It must be specially protected to prevent fire and smoke from entering the stairwell. The connection between the basement and Staircase 2 must be via an outdoor area or a sluss. Additionally, each floor should be equipped with a standpipe.")
# if the total building height is over 23 meters or if the total number of floors are more then 8. 
else: 
    print("Staircase 3 in the building must be an independent fire compartment and must be specially protected to prevent fire and smoke from entering the stairwell. The fire compartment must have the same fire resistance rating as the rest of the building’s structure, EI XX. Access to and from the stairwell must be provided through an open area or a pressurized sluss. The building must also include a firefighter lift with a dedicated sluss. Additionally, a standpipe should be installed on every floor. ")
