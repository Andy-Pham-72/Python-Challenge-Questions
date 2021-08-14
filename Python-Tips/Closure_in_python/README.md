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

# Get the values of the variables in the closure
closure_values = [
      my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])
```

    True
    arg1 was 2
    arg2 was 17
    True


Even the function `return_a_func` was deleted, and the `new_func` was bound to `my_func`, the message was still remembered!.

This technique by which some data gets attached to the code is call **Closure in Python**.

This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

**When do we have closures?**
* We must have a nested function (function inside a function).
* The nested function must refer to a value defined in the enclosing function.
* The enclosing function must return the nested function.


```python
# Other example
def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
    # Return the nested function
    return wrapper

@print_before_and_after
def multiply(a, b):
    print(a * b)

multiply(5, 10)
```

    Before multiply
    50
    After multiply



```python
# Real world example 1

import time

def timer(func):
    """ A decorator that prints how long a function took to run"""
    
    # Define the wrapper function to return
    def wrapper (*args, **kwargs):
        t_start = time.time()
        result = func(*args,**kwargs)
        t_total = time.time() - t_start
        print(('{} took {}s'.format(func.__name__, t_total)))
        return result
    return wrapper

@timer
def sleep_n_seconds(n):
    time.sleep(n)

```


```python
sleep_n_seconds(10)
```

    sleep_n_seconds took 10.004271745681763s



```python
# Real world example 2

def print_return_type(func):
  # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
          func.__name__, type(result)
        ))
        return result
        # Return the decorated function
    return wrapper
  
@print_return_type
def foo(value):
    return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))
```

    foo() returned type <class 'int'>
    42
    foo() returned type <class 'list'>
    [1, 2, 3]
    foo() returned type <class 'dict'>
    {'a': 42}


**Counter**


You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.


```python
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func
    wrapper.count = 0
    # Return the new decorated function
    return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')

foo()
foo()

print('foo() was called {} times.'.format(foo.count))
```

    foo() was called 2 times.


**Preserving docstrings when decorating functions**

Using `wraps` from `functools` could help us to preserve the docstring of the decorated functions.


```python
# Without wraps

def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper
  
@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)
    
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)
```

    Hello
    30
    Print 'hello' and then call the decorated function.



```python
# With wraps
from functools import wraps

def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper
  
@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)
    
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)
```

    Hello
    30
    Adds two numbers and prints the sum



```python
# Calls the original function instead of the decorated one

print_sum.__wrapped__(10,20)
```

    30


**Decorators that take arguments**


```python
def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Assign the function into a variable and use it as a decorator!
run_three_times = run_n_times(3)
@run_three_times
def print_sum(a,b):
    print(a + b)
print_sum(3,5)

print('##########')

@run_n_times(3)
def print_sum(a,b):
    print(a + b)
print_sum(3,5)
```

    8
    8
    8
    ##########
    8
    8
    8



```python
# Modify the print() function to always run 5 times
print = run_n_times(5)(print)

print('What is happening?!?!')
```

    What is happening?!?!
    What is happening?!?!
    What is happening?!?!
    What is happening?!?!
    What is happening?!?!


**HTML Generator**


```python
def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        return '<b>{}</b>'.format(msg)
    return wrapper

def italics(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        return '<i>{}</i>'.format(msg)
    return wrapper

def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)
        # Return the decorated function
        return wrapper
    # Return the decorator
    return decorator

```


```python
# Make hello() return bolded text
@html("<b>", "</b>")
def hello(name):
      return 'Hello {}!'.format(name)

print(hello('Alice'))
```

    <b>Hello Alice!</b>
    <b>Hello Alice!</b>
    <b>Hello Alice!</b>
    <b>Hello Alice!</b>
    <b>Hello Alice!</b>



```python
# Make goodbye() return italicized text
@html("<i>", "</i>")
def goodbye(name):
    return 'Goodbye {}.'.format(name)

print(goodbye('Alice'))
```

    <i>Goodbye Alice.</i>
    <i>Goodbye Alice.</i>
    <i>Goodbye Alice.</i>
    <i>Goodbye Alice.</i>
    <i>Goodbye Alice.</i>



```python
# Wrap the result of hello_goodbye() in <div> and </div>
@html("<div>","</div>")
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))
  
print(hello_goodbye('Alice'))
```

    <div>
    <b>Hello Alice!</b>
    <i>Goodbye Alice.</i>
    </div>
    <div>
    <b>Hello Alice!</b>
    <i>Goodbye Alice.</i>
    </div>
    <div>
    <b>Hello Alice!</b>
    <i>Goodbye Alice.</i>
    </div>
    <div>
    <b>Hello Alice!</b>
    <i>Goodbye Alice.</i>
    </div>
    <div>
    <b>Hello Alice!</b>
    <i>Goodbye Alice.</i>
    </div>


END.
