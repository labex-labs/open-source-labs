# Semi-supervised Learning

## Introduction

In this lab, we will explore the concept of semi-supervised learning, which is a type of machine learning where some of the training data is labeled and some is unlabeled. Semi-supervised learning algorithms can leverage the unlabeled data to improve the model's performance and generalize better to new samples. This is particularly useful when we have a small amount of labeled data but a large amount of unlabeled data.

In this lab, we will focus on two semi-supervised learning algorithms: Self Training and Label Propagation. We will learn how to implement and use these algorithms using scikit-learn, a popular machine learning library in Python.

## Steps

### Step 1: Installing scikit-learn

Before we begin, let's make sure scikit-learn is installed. If you don't have it installed, you can install it using the following command:

```
pip install -U scikit-learn
```

### Step 2: Self Training

#### Overview of Self Training algorithm

The Self Training algorithm is based on Yarowsky's algorithm. It allows a supervised classifier to function as a semi-supervised classifier by learning from unlabeled data. The algorithm works by iteratively training the supervised classifier on both the labeled and unlabeled data, and then using the predictions on the unlabeled data to add a subset of these samples to the labeled data. The algorithm continues iterating until all the samples have labels or no new samples are selected in an iteration.

#### Using Self Training in scikit-learn

In scikit-learn, the Self Training algorithm is implemented in the `SelfTrainingClassifier` class. To use this algorithm, you need to provide a supervised classifier that implements the `predict_proba` method. Here's an example of how to use the Self Training algorithm:

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# Create a logistic regression classifier
classifier = LogisticRegression()

# Create a self-training classifier with the logistic regression classifier as the base classifier
self_training_classifier = SelfTrainingClassifier(classifier)

# Train the self-training classifier on the labeled and unlabeled data
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# Predict the labels for new samples
y_pred = self_training_classifier.predict(X_test)
```

In the example above, `X_labeled` and `y_labeled` are the labeled data, `X_unlabeled` is the unlabeled data, and `X_test` is the new samples to be predicted.

### Step 3: Label Propagation

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

## Summary

Semi-supervised learning is a powerful technique that allows us to leverage unlabeled data to improve the performance of our models. In this lab, we learned about two semi-supervised learning algorithms: Self Training and Label Propagation. We also learned how to implement and use these algorithms using scikit-learn. By incorporating unlabeled data into our machine learning workflows, we can make better use of the available data and achieve more accurate predictions.
