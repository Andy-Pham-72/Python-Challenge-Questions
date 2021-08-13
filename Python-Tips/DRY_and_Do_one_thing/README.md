# DRY (Don't Repeat Yourself) and "Do One Thing"

When we write some scripts we usually have to copy and paste repeatedly a few times during the exploratory process. Therefore, we can accidentally make some typo or mistakes along the process.

Please see some examples below to illustrate some possible situations could arise:



```python
# Example 1

train = pd.read_csv('train.csv')
train_y = train['labels'].values  ### We keep repeating the exact code ###
train_X = train[col for col in train.columns if col != 'labels'].values
train_pca = PCA(n_components = 2).fit_transform(train_X)
plt.scatter(train_pca[:,0], train_pca[:,1])
```


```python
# Example 2

val = pd.read_csv('validation.csv')
val_y = val['labels'].values ### We keep repeating the exact code ###
val_X = val[col for col in train.columns if col != 'labels'].values
val_pca = PCA(n_components = 2).fit_transform(val_X)
plt.scatter(val_pca[:,0], val_pca[:,1])
```


```python
# Example 3

test = pd.read_csv('test.csv')
test_y = test['labels'].values  ### We keep repeating the exact code ###
test_X = test[col for col in train.columns if col != 'labels'].values
test_pca = PCA(n_components = 2).fit_transform(train)  ### Typo issue arises! ###
plt.scatter(test_pca[:,0], test_pca[:,1])
```

Throughout 3 examples above, we could see the chance of making error is very high since we keep repeating similar code for different output. Therefore, it's a good sign to create a function to automate the repeated code as below:


```python
def load_and_plot(path):
    """ Load a data set and plot the first two principal components.
    
    Agrs:
        path (str): The location of a CSV file.
        
    Returns:
        tuple of ndarray: (features, labels)
    
    """
    
    data = pd. read_csv(path)
    y = data['label'].values
    X = data[col for col in train.columns if col != 'label'].values
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])
    return X, y
```


```python
train_X, train_y = load_and_plot('train.csv')
val_X, val_y = load_and_plot('train.csv')
test_X, test_y = load_and_plot('train.csv')
```

# NOTE: 
- This function above seems to be good! But it also violates a principle that every function should have **a single responsibility**!

- Let's split the `load_and_plot()` function up into 2 functions:


```python
def load_data(path):
    """ Load a data set and plot the first two principal components.
    
    Agrs:
        path (str): The location of a CSV file.
        
    Returns:
        tuple of ndarray: (features, labels)
    
    """
    data = pd.read_csv(path)
    y = data['label'].values
    X = data[col for col in train.columns if col != 'label'].values
    return X, y
```


```python
def plot_data(X):
    """ Plot the first two principal components of a matrix
    
    Args:
        X (numpy.ndarray): The data to plot.
    """
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])
```

After splitting our code into 2 functions, our code has become more flexible. For example, if you just want to load the data and not to plot it, we can just use the `load_data()` function.

**Advantages of doing one thing:**
The code beomes:
- More flexible
- More easily understood
- Simpler to test
- Simpler to debug
- Easier to change

END.
