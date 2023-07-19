# Transforming the Prediction Target

## Introduction

In machine learning, it is often necessary to transform the prediction target before training a model. This can include tasks such as converting multiclass labels into a binary indicator matrix or encoding non-numerical labels into numerical labels.

In this lab, we will explore the various techniques provided by the `sklearn.preprocessing` module in scikit-learn to transform the prediction target.

## Steps

### Step 1: Label Binarization

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

### Step 2: MultiLabel Binarization

MultiLabel binarization is the process of converting a collection of collections of labels into an indicator format. This can be achieved using the `MultiLabelBinarizer` class.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Define a list of collections of labels
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Create a MultiLabelBinarizer instance and fit_transform the list of collections
MultiLabelBinarizer().fit_transform(y)
```

### Step 3: Label Encoding

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

## Summary

In this lab, we learned how to transform the prediction target using various techniques provided by the `sklearn.preprocessing` module in scikit-learn. These techniques included label binarization, multi-label binarization, and label encoding.
