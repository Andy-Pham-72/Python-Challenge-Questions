## Problem:

Create a class to find out the cost of a rectangular field with:
- **breadth(b = 120), length(l = 160)**.

- **it costs x (2000) rupees/ square**

## Solution




```python
class Rectangle:
    def __init__(self, length, breadth, unit_cost= 0):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
        
    def get_perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def get_area(self):
        return self.length * self.breadth
    
    def calculate_cost(self):
        area = self.get_area()
        return area * self.unit_cost
```


```python
# breadth = 120 cm, 
#length = 160 cm, 
# 1 cm^2 = Ruby 2000

r = Rectangle(160, 120, 2000)

print("Area of Rectangle: {:,} cm^2 ".format(r.get_area()))

print("Perimeter of the Retangle: %s cm " % (r.get_perimeter()))

print("Cost of Rectangular field: Rs. {:,} ".format(r.calculate_cost()))
```

    Area of Rectangle: 19,200 cm^2 
    Perimeter of the Retangle: 560 cm 
    Cost of Rectangular field: Rs. 38,400,000 

### NOTE:
- **"r"** is the representation of the object outside of the class.
- **"self"** is the representation of the object inside  the class.


## Supplemental reading:

- [__init__ in Python](https://www.geeksforgeeks.org/__init__-in-python/)

