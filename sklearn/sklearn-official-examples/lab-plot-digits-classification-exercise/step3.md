# Split the dataset into training and testing sets

Next, we will split the dataset into training and testing sets using scikit-learn's `train_test_split` function. We will use 90% of the data for training and 10% for testing.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```


