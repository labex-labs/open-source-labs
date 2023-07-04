# Split the Dataset into Training and Test Sets

Next, we will split the dataset into training and test sets using the `train_test_split` function from the `sklearn.model_selection` module. The training set will be used to train the Naive Bayes classifier, and the test set will be used to evaluate its performance.

```python
from sklearn.model_selection import train_test_split

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
