# **str()** and **repr()** are both used to get a string representation of object.

### Goal
- `str()` is used for creating output for end user - **GOAL** is to be readable.
- `repr()` is used for debugging and development - **GOAL** is to be unambiguous.

for example:
- if we suspect a float has a small rounding error => **repr** will show us while **str** may not.



```python
# example 1

x = "Hello, Geeks."

print(str(x))
print(str(2.0/11.0))
print("===========================")

print(repr(x))
print(repr(2.0/11.0))
```

    Hello, Geeks.
    0.18181818181818182
    ===========================
    'Hello, Geeks.'
    0.18181818181818182



```python
b = repr(x)
type(b)
```




    str




```python
# example 2

import datetime

today = datetime.datetime.now()

# print readable format for date-time object
print(str(today))

print(repr(today))
```

    2021-07-07 15:42:49.841831
    datetime.datetime(2021, 7, 7, 15, 42, 49, 841831)


- `str()` displays today's date in a way that the user can understand the date and time.
- `repr()` print the "official" representation of a date-time object (the "official" string representation we can reconstruct the object).

# `__str__` vs `__repr__`
- A user defined class should also have a `__repr__` if we need detailed information for debugging.
- If we think it'd be useful to have a string version for users, we create a `__str__` function.

### example 1:


```python
# A user defined class to represent Complex numbers

class Complex:
    # constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' %(self.real, self.imag)
    
    # For call to str(). Prints readable form
    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)
    
# Driver program to test above

t = Complex(10, 20)

# print
print(str(t))

print('===============')

print(repr(t))
```

    10 + i20
    ===============
    Rational(10, 20)


### example 2:


```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
```


```python
my_car = Car('red', 34567)

# we don't want to have this result as below
print(my_car)
```

    <__main__.Car object at 0x7ff468bee730>



```python
my_car
```




    <__main__.Car at 0x7ff468bee730>



It only give us the memory address `0x7ff468bee730` or the id

=> it's not super useful!


```python
# alternate solution

print(my_car.color, my_car.mileage)
```

    red 34567



```python
# Or they can add this
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def to_string(self):
        print(self.color, self.mileage)
    
my_car2 = Car('blue', 1234)

my_car2.to_string()
```

    blue 1234


We can use the convention in Python
- `__str__` (pronounce as stir)
- `__repr__` (pronounce as reper)



```python
# with use of __str__
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return 'a {self.color} car'. format(self= self)

# test 
my_car3 = Car('red', 37281)

print(my_car3)
```

    a  red car



```python
my_car3
```




    <__main__.Car at 0x7ff468c18b50>



We can also convert the return result to string:


```python
str(my_car3)
```




    'a red car'




```python
'{}'.format(my_car3)
```




    'a red car'




```python
# with use of __repr__

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def __repr__(self):
        # 'self.__class__.__name__' gives use the name of the class
        return '{self.__class__.__name__} ({self.color},{self.mileage})'.format(self=self) 

# test
my_car4 = Car('orange', 7891)

print(my_car4)
```

    Car (orange,7891)



```python
my_car4
```




    Car (orange,7891)



END.
