# MultiLabel Binarization

MultiLabel binarization is the process of converting a collection of collections of labels into an indicator format. This can be achieved using the `MultiLabelBinarizer` class.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Define a list of collections of labels
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Create a MultiLabelBinarizer instance and fit_transform the list of collections
MultiLabelBinarizer().fit_transform(y)
```
