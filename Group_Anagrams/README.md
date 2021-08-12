Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```


```python
def groupAnagrams(strs: []):

    d = {}
    for s in strs:
        mold = "".join(sorted(s))
        if mold not in d:
            d[mold] = [s]
        else:
            d[mold] += [s]
    return d.values()
```


```python
# Test 1
strs1 = ["eat","tea","tan","ate","nat","bat"]

# Test 2
strs2 = []

# Test 3
strs3 = ["a"]

```


```python
groupAnagrams(strs1)
```




    dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])




```python
groupAnagrams(strs2)
```




    dict_values([])




```python
groupAnagrams(strs3)
```




    dict_values([['a']])



END.
