# Label Binarization

Label binarization is the process of converting multiclass labels into a binary indicator matrix. It can be achieved using the `LabelBinarizer` class.

```python
from sklearn import preprocessing

# Create a LabelBinarizer instance
lb = preprocessing.LabelBinarizer()

# Fit the LabelBinarizer on a list of multiclass labels
lb.fit([1, 2, 6, 4, 2])

# Get the classes learned by the LabelBinarizer
lb.classes_

# Transform a list of multiclass labels into a binary indicator matrix
lb.transform([1, 6])
```
