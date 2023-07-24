# Split the Dataset

Before training the Decision Tree classifier, we need to split the dataset into training and testing sets. We will use 70% of the data for training and 30% for testing.

```python
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
