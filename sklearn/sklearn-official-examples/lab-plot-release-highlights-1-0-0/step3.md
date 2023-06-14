# Split Data into Training and Testing Sets

Next, we will split the data into training and testing sets using scikit-learn's `train_test_split` function. We will use 70% of the data for training and 30% for testing.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
```


