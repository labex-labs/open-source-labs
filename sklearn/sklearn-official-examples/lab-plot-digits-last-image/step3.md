# Preparing the Dataset for Machine Learning

Before we can train a machine learning model on the dataset, we need to prepare the data by splitting it into training and testing sets. We can do this using scikit-learn's `train_test_split` function:

```python
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
