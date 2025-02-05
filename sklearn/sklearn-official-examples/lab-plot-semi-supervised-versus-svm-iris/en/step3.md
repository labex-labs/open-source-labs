# Set up the Self-training classifiers

We will set up two Self-training classifiers with different percentages of labeled data: 30% and 50%. Self-training is a semi-supervised learning algorithm that trains a classifier on the labeled data and then uses it to predict the labels of the unlabeled data. The most confident predictions are added to the labeled data and the process is repeated until convergence.

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Set up the Self-training classifiers
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Self-training 30% data",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Self-training 50% data",
)
```
