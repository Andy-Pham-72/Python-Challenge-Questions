# Private Variables

According to [Python's official documentation](https://docs.python.org/3/tutorial/classes.html), "Private" instance variables that cannot be accessed except from inside an object don't exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. `_spam`) should be treated as **a non-public part of the API** (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to **avoid name clashes of names** with names defined by `subclasses`), there is limited support for such a mechanism, called *name mangling*.
- Any identifier of the form `__spam` (at lease two leading underscores, at most one trailing underscore) is textually replaced with `_classname__spam`, where `classname` is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definiton of a class.

**Name mangling** is helpful for letting subclasses override methods without breaking intraclass method calls. For example:


```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

The above example would work even if `MappingSubclass` were ot introduce a `__update` identifier since it is replaced wht `_Mapping``update` in the `Mapping` class an `_MappingSubclass__update` in the `MappingSubclass` class respectively.

**Note**: mangling rules are designed mostly to avoid accidents; it still is possible to access or modify a varable that is considered private. This can even be useful in special circumstances, such as in the debugger.


```python
# Assign to a varible
m = MappingSubclass(['game','boy'])

# Update 2 values
m.update('name', 'key')

# Check the added value
print(m.items_list)
```

    ['game', 'boy', ('n', 'k'), ('a', 'e'), ('m', 'y')]



```python
# Access the private variable in order to update value
m._Mapping__update('hot')

# Check the added value
print(m.items_list)
```

    ['game', 'boy', ('n', 'k'), ('a', 'e'), ('m', 'y'), 'h', 'o', 't']


END.
