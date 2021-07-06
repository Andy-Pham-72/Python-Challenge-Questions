A **leap year** is exactly **divisible by 4** except for century years (years ending with `00`). The century year is a **leap year** only if it is perfectly divisible by **`400`**.

For example,

2017 is not a leap year

1900 is not a leap year

2012 is a leap year

2000 is a leap year

Challenge: Write a function to find whether the input year is leap year or not.


```python
# Write a program to check 

year = int(input())

if (year% 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
    
```

     1991


    1991 is not a leap year



```python
def leap_year_check(num):
    '''
    The function that helps to check whether the input year is a leap year or not
    '''
    
    if (num% 4) == 0:
        if (num % 100) == 0:
            if (num % 400) == 0:
                print("{0} is a leap year".format(num))
            else:
                print("{0} is not a leap year".format(num))
        else:
            print("{0} is a leap year".format(num))
    else:
        print("{0} is not a leap year".format(num))
```


```python
leap_year_check(2019)
```

    2019 is not a leap year

