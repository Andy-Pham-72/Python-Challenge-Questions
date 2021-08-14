# Functional Programming

Functional programming is a programming technique that avoids side effect in your program by performing computation mainly through evalutation of functions and it'll rely heavily on immutable data structures.

In other words, functional programming (just like Object Oriented Programming) has potential benefit that can reduce the likelihood of having bugs and make them more maintainable.


```python
scientists = [
    {'name': "Ada Lovelace", 'field': 'math', 'born': 1815, 'nobel' : False},
    {'name': "Emmy Noether", 'field': 'math', 'born': 1882, 'nobel' : False}
]

scientists
```




    [{'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
     {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False}]




```python
# We can easily change the value in the dictionary easily
scientists[0]['name'] = 'Ed Lovelace'
```


```python
scientists
```




    [{'name': 'Ed Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
     {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False}]



There is the posibility that we could make typo during the input new data process. For example, we can type `'nema'` instead of `'name'` and other fields will be the same, then the list will have different structure with the `'nema'`.

There is an alternative that can fix the issue as below:


```python
import collections

Scientist = collections.namedtuple('Scientist', [
        'name',
        'field',
        'born',
        'nobel'
])

Scientist
```




    __main__.Scientist




```python
Scientist(name = 'Ada Lovelace', field='math', born=1815, nobel= False)
```




    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False)




```python
ada = Scientist(name = 'Ada Lovelace', field='math', born=1815, nobel= False)
ada.name
```




    'Ada Lovelace'




```python
# We can't change the named tuple element because it's immutable
ada.name = 'Ed Lovelace'
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-9-a037f652916b> in <module>
          1 # We can't change the named tuple element because it's immutable
    ----> 2 ada.name = 'Ed Lovelace'
    

    AttributeError: can't set attribute


Let's make a list with the `Scientist` variable that we just created.


```python
scientists = [
    Scientist(name= "Ada Lovelace", field= 'math', born= 1815, nobel = False),
    Scientist(name= "Emmy Noether", field= 'math', born= 1882, nobel = False),
    Scientist(name= "Marie Curie", field= 'physics', born= 1867, nobel = True),
    Scientist(name= "Ada Yonath", field= 'chemistry', born= 1939, nobel = True),
    Scientist(name= "Vera Rubin", field= 'astronomy', born= 1928, nobel = False),
    Scientist(name= "Sally Ride", field= 'physics', born= 1951, nobel = False)
]

scientists
```




    [Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
     Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
     Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
     Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
     Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
     Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)]




```python
# Make it looks nicer

from pprint import pprint

pprint(scientists)
```

    [Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
     Scientist(name='Emmy Noether', field='math', born=1882, nobel=False)]



```python
# We can't change the value in scientists
scientists[0].name = 'Ed Lovelace'
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-3dfaa97c4227> in <module>
          1 # We can't change the value in scientists
    ----> 2 scientists[0].name = 'Ed Lovelace'
    

    AttributeError: can't set attribute



```python
# We can delete the value by using 'del'
del scientists[0]

scientists
```




    [Scientist(name='Emmy Noether', field='math', born=1882, nobel=False)]



From the example, we had created immutable items and then stored them all in a list which is a mutable data structure in Python. Therefore, the best way to handle it is instead of making a list, we create a tuple because tuple is an immutable data structure since you can't change item with it.

# Filter() function.

Filter() function returns an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.



```python
fs = filter(lambda x: x.nobel is True, scientists)
next(fs)
```




    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True)




```python
next(fs)
```




    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True)




```python
next(fs)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-20-cc337a681289> in <module>
    ----> 1 next(fs)
    

    StopIteration: 



```python
# wraps the filter into tuple and the print it out with pprint()
fs = tuple(filter(lambda x: x.nobel is True, scientists))

pprint(fs)
```

    (Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
     Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True))



```python
# check another filter
pprint(tuple(filter(lambda x: x.field == 'physics' and x.nobel, scientists)))
```

    (Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),)



```python
# Create a for loop to find the scientists who won Nobel

for x in scientists:
    if x.nobel is True:
        print(x)
```

    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True)
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True)



```python
# Create a function that only filter scientists with Nobel
def nobel_filter(x):
    return x.nobel is True

pprint(tuple(filter(nobel_filter, scientists)))
```

    (Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
     Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True))



```python
# Use a list comprehension to filter scientists who won Nobel
[x for x in scientists if x.nobel is True]
```




    [Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
     Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True)]




```python
# use generator expression instead of list comprehension
pprint(tuple(x for x in scientists if x.nobel is True))
```

    (Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
     Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True))


# Map() function

Like filter() function, Map() function is another built-in function in Python that makes an iterator computing the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.


```python
names_and_ages = tuple(map(
                    lambda x: {'name': x.name, 'age': 2017 - x.born},
                    scientists
                    ))

pprint(names_and_ages)
```

    ({'age': 202, 'name': 'Ada Lovelace'},
     {'age': 135, 'name': 'Emmy Noether'},
     {'age': 150, 'name': 'Marie Curie'},
     {'age': 78, 'name': 'Ada Yonath'},
     {'age': 89, 'name': 'Vera Rubin'},
     {'age': 66, 'name': 'Sally Ride'})


As we can see the map() function mapped the function into each items of the list. Now all the items in the variable `names_and_ages` are mutable items.


```python
# Use list comprehension 
[{'name': x.name, 'age': 2017 - x.born}
for x in scientists]
```




    [{'name': 'Ada Lovelace', 'age': 202},
     {'name': 'Emmy Noether', 'age': 135},
     {'name': 'Marie Curie', 'age': 150},
     {'name': 'Ada Yonath', 'age': 78},
     {'name': 'Vera Rubin', 'age': 89},
     {'name': 'Sally Ride', 'age': 66}]




```python
# Use generator expression 
tuple({'name': x.name, 'age': 2017 - x.born}
     for x in scientists)
```




    ({'name': 'Ada Lovelace', 'age': 202},
     {'name': 'Emmy Noether', 'age': 135},
     {'name': 'Marie Curie', 'age': 150},
     {'name': 'Ada Yonath', 'age': 78},
     {'name': 'Vera Rubin', 'age': 89},
     {'name': 'Sally Ride', 'age': 66})



# Reduce() function

reduce() function has to be imported from `functools` module. reduce() function can apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.

For example, reduce(lambda x,y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty.



```python
from functools import reduce

names_and_ages = tuple(map(
                    lambda x: {'name': x.name, 'age': 2017 - x.born},
                    scientists
                    ))

total_age = reduce(
            lambda acc, val: acc+ val['age'],  # start adding 'age' value 
            names_and_ages,    # use the item from `names_and_ages` variable
            0                  # set the accumulated value as 0
)

total_age
```




    720




```python
# Create a function reducer
def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc

# Use reduce() and apply reducer() into it
scientists_by_field = reduce(
                reducer,
                scientists,
                {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)

pprint(scientists_by_field)
```

    {'astronomy': ['Vera Rubin'],
     'chemistry': ['Ada Yonath'],
     'math': ['Ada Lovelace', 'Emmy Noether'],
     'physics': ['Marie Curie', 'Sally Ride']}



```python
# Use itertools

import itertools

scientists_by_field1 = {
        item[0] : list(item[1])
        for item in itertools.groupby(scientists, lambda x: x.field)
}

pprint(scientists_by_field1)
```

    {'astronomy': [Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False)],
     'chemistry': [Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True)],
     'math': [Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
              Scientist(name='Emmy Noether', field='math', born=1882, nobel=False)],
     'physics': [Scientist(name='Sally Ride', field='physics', born=1951, nobel=False)]}



```python
# Use functools

import functools

scientists_by_field2 = functools.reduce(
            lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}},  # using dictionary merging syntax
            scientists,
            {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []}
)

pprint(scientists_by_field2)
```

    {'astronomy': ['Vera Rubin'],
     'chemistry': ['Ada Yonath'],
     'math': ['Ada Lovelace', 'Emmy Noether'],
     'physics': ['Marie Curie', 'Sally Ride']}


END.
