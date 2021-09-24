## Iterables and Iterators.

The **itertools** module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and effectively in pure Python. [Documentation](https://docs.python.org/2/library/itertools.html)

**Problem:** You are given:
- A list of **N** lowercase English letters. 
- For a given integer **K**, you can select any **K** indices (assume 1-based indexing) with an uniform probability from the list.

Find the probability that at least one of the **K** indices selected will contain the letter **`a`**.

**Input Format**
- The input consists of three lines:
    * The first line contains the integers `N`, denoting the length of the list.
    * The next line consists of `N` spaced-separated lowercase English letters, denoting the elements of the list.
    * The third and the last line of input contains the integer `K`, denoting the number of indices to be selected.

**Output Format**
Output a single line consisting of the probability that at least one of the `K` indices selected contains the letter: **`a`** .

**NOTE:** the answer must be correct up to 3 decimal places.

**Constraints**
1 =< N =< 10

1 =< K =< 10
All the letters in the list are lowercase English letters.

**Sample Input**
```
4
a a c d
2
```

**Sample Output**
```
0.8333
```

**Explanation:**
All possible unordered tuples of length 2 comprising of indices from `1` to `4` are:
(1 , 2), (1 , 3), (1 , 4), (2 , 3), (2 , 4), (3 , 4)

=> Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter `a`.

Hence, the answer is `5 / 6 = 0.8333`

**Please note that this is a combination problem since the order does not matter!**

**Supplemental materials about permutation and combination (if you are not familiar with the topic)**:
- [What is a Permutation? Learn the Permutation Formula](https://www.youtube.com/watch?v=oT64b5euTfs)
- [Permutations and Combinations Tutorial](https://www.youtube.com/watch?v=XJnIdRXUi7A)

# SOLUTION 1


```python
from itertools import combinations

# Read input from STDIN. Print output to STDOUT

# Assign the len of list
N = int(input())

# Denote the element of list
L = input().split()

# Denote the number of indices to be selected
K = int(input())

# Create combination from L & K
C = list(combinations(L , K))

# Use lambda function within filter() 
F = filter(lambda c: 'a' in c, C)

# print the output
print("{:.3}".format(len( list(F))/ len(C) ))
```

     4
     a a c d
     2


    0.833


Let unpack the variables `L`, `K`, `C` in order to understand the explanation :


```python
# We have a list:
L = input().split()

print(L)
```

     a a c d


    ['a', 'a', 'c', 'd']



```python
# We have combinations of L and K
C = list(combinations(L , K))

print(C)
```




    [('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')]



Here we have 6 combinations of the list ["a", "a", "c", "d"].


```python
# Filter only the combinations that contain letter `a`:
F = filter(lambda c: 'a' in c, C)

print(list(F))
```

    [('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd')]


Here we have **5 possibilities** that have letter `a` in the combinations.
And with the **6 combinations** from the above list so we can easily calculate the probability of having letter `a` in the total combinations of **given 4 letters**.

6 / 5 = 0.8333 (number up to 3 decimal places)

In this case we don't really need the variable `N` but the question requires that for the input.


# SOLUTION 2 
(without using itertools)


```python
from functools import reduce

# Assign the len of list
N = int(input())

# Denote the element of list
L = input().split()

# Denote the number of indices to be selected
K = int(input())

# Count the numbers of letter "a" in the list
M = "".join(L).count("a")

# Calculates the probability of not having letter "a" in the combinations
P = reduce(lambda x,y: x*y, [(1.0 - M * 1.0/ (N-i)) for i in range(K)])

# print the output
print(1.0 - P)
```

     4
     a a c d
     2


    0.8333333333333333


Let's unpack the variable `M` and `P`


```python
# We have M is the numbers of letter "a" in the list L as below
print(M)
```

    2


In order to unpack P, we can have a small example of applying reduce with the annonymous function.


```python
# Example
numbers = [1, 2, 3, 4]

print(reduce(lambda a, b: a + b, numbers))
```




    10



The `reduce()` implements the addition as `(((1 + 2) + 3) + 4) = 10`. [How to use reduce()](https://realpython.com/python-reduce-function/)

We have a sequence of N characters and M number(which is 2) of them are `a`. We perform K selection of random elements from the sequence. The goal is to calculate the probability of at least one character in the selected K elements is `a`. But first let do some steps:
- Let's calculate the probability (P) of an event where none of the selected elements is `a`. 
    * If K = 1, then the probability of selecting anything but `a` is P = (1 - M) / N
    * If K = 2, we are selecting 2 elements. The probability of none of the 2 being `a` is the probability of the first element is not `a`: (1 - M/N) times the probability of the second element is not `a`: (1 - M / (N - 1)).
        * The Denominator is (N - 1) because the length of the sequence is (N-1) after taking out the first element while the number of `a`s remain the same.

P = (1 - M/N) * (1 - M/(N-1))

If K = 3 then

P = (1 - M/N) * (1 - M/(N-1)) * (1 - M/(N-2))
and so one

The problem statement of this challenge is to calculate the probability of at least one `a` selected. Then the result is:
**`1 - p`**

P/s: Using `reduce()` in this problem to compute their cumulative multiplication.


END.
