# Split Data into Train and Test Sets

We will split our data into a train set and a test set, with 50% of the data in each set.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
