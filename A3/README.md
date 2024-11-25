# About the tool 
## State the problem / claim that your tool is solving.
The claim we are checking with the help of our tool is if building 11 needs a pressurized staircase, and if the building needs a fire fighter lift according to the Icelandic regulations and guidelines.
Our tool is also made for checking what fire safety regulations and guidelines the building needs to have according to the Icelandic building laws. If for example what safety standard it should follow EI60 or more also if there is a requirement for a door lock (sluss) on the different floors. 
## State where you found that problem.
This tool will help fire engineers during the early stage of the planning of the building. If they use our tool they will directly get the requirements guidelines for the specific height and number of floors the building has. Which lowers the chance of making a mistake in the planning of the stairwells and makes the job as a fire engineer more efficient. 
## Description of the tool
The tool finds out the building height from the ground floor up to the roof and the number of floors. With this information the tool will go over the requirements and can give out what kind of staircases are needed and if there should be a fire fighter lift.
## Instructions to run the tool.

step 1: Get your hands on the IFC model file and add it to your model folder

step 2: Name the IFC model a specific name you will remember and know 

step 3:  Open the tool and add the path to your IFC model where it says [model = ifcopenshell.open(“your path hear”) ]

step 4: Modify lines 61 & 64 so it follows your countries building regulations and guidelines for fire safety with respect to the height of the building over ground and the number of floors over ground. 

step 5: When you are set to run the tool press on the button run python file and sit back and enjoy, the tool can take some time it really depends on the size of the IFC file. 

step 6: When the tool is done running you will see the total height of the building over ground and the total number of floors over ground in your IFC file, and lastly the requirements and guidelines for your IFC file according to your countries. 

# Advanced Building Design feedback for next year 
## What Advanced Building Design Stage (A, B, C or D) would your tool be useful?
Our tool is useful in A or B, the early stage of the building modeling, where the model has the amount of floors and the height of the building. The fire exits are normally in the core of the building and the core is one of the first modeled parts of a building. And to be able to model it you have to know the wall thickness and how the floor plan should look around the core regarding the requirements seas about the if we need a door sluss. 

## Which subjects might use it?
The fire safety engineers, architects
## What information is required in the model for your tool to work?
The tool requires the model to have defined what floor the ground level is located with any of the names "Ground Floor", "Level 0", "Ground". After the tool can define what floor is the ground floor it can begin counting the number of floors above ground as well as the height of the building from the ground floor.


