When your script is run by passing it as a command to the Python interpreter,
```
python myscript.py
```
All of the code that is at indentation level 0 gets executed. 

Functions and classes that are defined are, well, defined, but none of their code gets run. 

Unlike other languages, there's no `main()` function that gets run automatically - the `main()` function is implicitly all the code at the top level.

In this case, the top-level code is an if block. __name__ is a built-in variable which **evaluates** to the name of the current module. 
However, if a module is being run directly (as in myscript.py above), then __name__ instead is set to the string "__main__". Thus, you can test whether your script is being run directly or being imported by something else by testing as below:



```python
# file one.py

def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
```


```python
# file two.py

import foo 
print("top-level in two.py")
foo.func()

if __name__ == "__main__":
    print("two.py is being run directly")

else:
    print("two.py is being imported into another module")
```
    

if we run `one.py`:

```python
python one.py

top-level in one.py
one.py is being run directly

```


if we run `two.py`:

```python
top-level in one.py
one.py is being imported into another module
top-level in two.py
func() in one.py
two.py is being run directly

```
