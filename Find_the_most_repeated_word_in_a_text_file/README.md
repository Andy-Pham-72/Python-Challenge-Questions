# Find the most repeated word in a text file

### Challenge

Create a python script to parse a text file and return the most repeated word and the frequency of it.

For exampple:

- We have a `you were there.txt` file with the content as below:

```
You Were There

When tears fell from my eyes,
you were there to brush them away.
When I was lost in confusion,
you were there to say that everything would be okay.
When I stood before you falling apart,
you were there to lend your heart.
When I felt like no one could understand,
you were there to take my hand.
When no one else was left to care,
you were there.

```

### Approach:

- We will take the content of the file as input.
- We will save each word in a list after removing spaces and punctuations from the input string.
- Find the frequency of each word.
- Print the word which has a maximum frequency.



```python
 def most_repeated_word_txt(text):
    # assign the string from the txt file into a variable
    file = open(text, "r")

    # assign an empty string into a variable
    frequent_word = ""

    frequency = 0

    words = []

    # traverse file line by line

    for line in file:

        # splits each line into words and removing spaces + punctations from the input
        line_word = line.lower().replace(',','').replace('.','').replace('\n','').split(" ")

        # adding the a list
        for word in line_word:
            words.append(word)

    # find the max occured word
    for a in range(0, len(words)):

        # declare count
        count = 1

        # count each word in the txt
        for b in range(a+1, len(words)): 
            if (words[a] == words[b]): # check whether the next word is the same or not.
                count = count + 1 # if the statement is True, add 1 into variable count

        # if the count value is more than highest frequency then
        if (count > frequency): 
            frequency = count 
            frequent_word = words[a] # assign the most repeated word into the variable

    print("most repeated word: " , frequent_word)

    print("frequency: " , str(frequency))

    # close the file
    file.close()
```


```python
most_repeated_word_txt("you_were_there.txt")
```

    most repeated word:  you
    frequency:  7


END
