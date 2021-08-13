# Python Closures

In order to understand Python Closure, we have to first understand what a **nested function** and **nonlocal variable** is.

**a function** defined inside another function is called a nested function. **Nested Function** can access variables of the enclosing scope.

**non-local variables** are read-only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.

Please check below code for explanation:


```python
def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))
    return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__[0] is not None)

# Delete the return_a_func()
del return_a_func

# Check my_func
my_func()
```

    True
    arg1 was 2
    arg2 was 17


Even the function `return_a_func` was deleted, and the `new_func` was bound to `my_func`, the message was still remembered!.

This technique by which some data gets attached to the code is call **Closure in Python**.

This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

**When do we have closures?**
* We must have a nested function (function inside a function).
* The nested function must refer to a value defined in the enclosing function.
* The enclosing function must return the nested function.

END.
