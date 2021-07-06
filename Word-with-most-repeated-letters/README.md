# Word with most repeated letters

Write a function, `most_repeating_word`, that reads a string from standard input.

**The function should return the word that contains the greatest number of repeated letters.** In other word:
- For each word, find the letter that appears the most times.
- Find the word whose most-repeated letter appears more than any other.

That is when `most_repeating_word()` is call, and reads the string **"this is an elementary test example"** from standard input, then your function should return `elementary`.

That's because:

- **this** has no repeating letters.
- **is** has no repeating letters.
- **an** has no repeating letters.
- **elementary** has one repeating letter since `e` appears 3 times.
- **test** has one repeating letter since `t` which appears twice.
- **example** has one repeating letter since `e` which appears twice.

So the most common letter in *elementary* appears more often than the most common letters in any of other words. (**If it's a tie, then any of the appropriate words can be returned.**)



```python
# Complete the "most_repeating_word" function below.
# It will read inputted lines from standard input.
# The function is expected to return a STRING

def most_repeating_word(string):
    '''
    The function will return the word that contains the greatest number of repeated letters
    eg: 
    > most_repeating_word("this is an elementary test example")
    > elementary
    '''
    
    words = string.split() # split the string into a list of words
    
    max_repeat_count = 0 
    
    for word in words:
        
        dictionary = {} # create a dictionary variable
        
        for letter in word: # loop through the letters of the word
            
            if letter not in dictionary: 
                
                dictionary[letter] = 1 # assign 1 to the letter that isn't contained in 'dictionary'
            
            else:
                dictionary[letter] += 1 # add 1 if there is any repeating letter
                
            if dictionary[letter] > max_repeat_count: # it will iterate untill finding the letter that has the highest repeating number.
                
                # assign the number of repeating letter into the variable 'max_repeat_count'
                max_repeat_count = dictionary[letter] 
                
                # assign the word with highest repeating number
                result = word 
                
    return result

```


```python
# Test the function

sentence_1 = "this is an elementary test example"

most_repeating_word(sentence_1)
```




    'elementary'




```python
sentence_2 = "choose the letter like you would a good pen"

most_repeating_word(sentence_2)
```




    'choose'



END.
