# New Self-Training Meta-Estimator

A new self-training implementation, based on Yarowski's algorithm can now be used with any classifier that implements `predict_proba`. The sub-classifier will behave as a semi-supervised classifier, allowing it to learn from unlabeled data.

```python
import numpy as np
from sklearn import datasets
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# load the iris dataset
iris = datasets.load_iris()

# add random unlabeled points
rng = np.random.RandomState(42)
random_unlabeled_points = rng.rand(iris.target.shape[0]) < 0.3
iris.target[random_unlabeled_points] = -1

# create the classifier
svc = SVC(probability=True, gamma="auto")
self_training_model = SelfTrainingClassifier(svc)

# fit the model
self_training_model.fit(iris.data, iris.target)
```


