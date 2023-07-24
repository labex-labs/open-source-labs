# Label Propagation

#### Overview of Label Propagation algorithm

Label Propagation is a type of semi-supervised graph inference algorithm. It constructs a similarity graph over all items in the input dataset and uses this graph to propagate the labels from the labeled data to the unlabeled data. Label Propagation can be used for classification tasks and supports kernel methods to project the data into alternate dimensional spaces.

#### Using Label Propagation in scikit-learn

In scikit-learn, there are two label propagation models available: `LabelPropagation` and `LabelSpreading`. Both models construct a similarity graph and propagate the labels. Here's an example of how to use Label Propagation:

```python
from sklearn.semi_supervised import LabelPropagation

# Create a label propagation model
label_propagation = LabelPropagation()

# Train the label propagation model on the labeled data
label_propagation.fit(X_labeled, y_labeled)

# Predict the labels for new samples
y_pred = label_propagation.predict(X_test)
```

In the example above, `X_labeled` and `y_labeled` are the labeled data, and `X_test` is the new samples to be predicted.
