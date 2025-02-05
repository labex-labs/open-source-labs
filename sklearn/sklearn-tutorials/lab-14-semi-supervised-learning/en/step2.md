# Self Training

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
