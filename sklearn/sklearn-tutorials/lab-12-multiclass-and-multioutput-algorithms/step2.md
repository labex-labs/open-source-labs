# Multilabel Classification

#### Problem Description

Multilabel classification is a classification task where each sample can be assigned multiple labels. The number of labels each sample can have is greater than two.

#### Target Format

A valid representation of multilabel targets is a binary matrix, where each row represents a sample and each column represents a class. A value of 1 indicates the presence of the label in the sample, while 0 or -1 indicates the absence.

#### Example

Let's create a multilabel classification problem using the make_classification function:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate a multilabel classification problem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Fit a multioutput random forest classifier
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```
