# Classification with SVM

- Start by importing the necessary libraries:

```python
from sklearn import svm
```

- Define the training samples `X` and class labels `y`:

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- Create an instance of the `SVC` classifier and fit the data:

```python
clf = svm.SVC()
clf.fit(X, y)
```

- Use the trained model to predict new values:

```python
clf.predict([[2., 2.]])
```
