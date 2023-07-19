# Multiclass-Multioutput Classification

#### Problem Description

Multiclass-multioutput classification, also known as multitask classification, predicts multiple non-binary properties for each sample. Each property can have more than two classes.

#### Target Format

A valid representation of multiclass-multioutput targets is a dense matrix, where each row represents a sample and each column represents a different property or class.

#### Example

Let's create a multiclass-multioutput classification problem using the make_classification function:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Generate a multiclass-multioutput classification problem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Fit a multioutput support vector classifier
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```
