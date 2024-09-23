import ifcopenshell

from .rules import windowRule
from .rules import doorRule

model = ifcopenshell.open("C:\Users\noahw\OneDrive\Skrivbord\ifc file")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
