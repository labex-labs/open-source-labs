# Label Encoding

Label encoding is the process of converting non-numerical labels into numerical labels. This can be achieved using the `LabelEncoder` class.

```python
from sklearn import preprocessing

# Create a LabelEncoder instance
le = preprocessing.LabelEncoder()

# Fit the LabelEncoder on a list of non-numerical labels
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# Get the classes learned by the LabelEncoder
list(le.classes_)

# Transform a list of non-numerical labels into numerical labels
le.transform(["tokyo", "tokyo", "paris"])

# Inverse transform numerical labels back to non-numerical labels
list(le.inverse_transform([2, 2, 1]))
```
