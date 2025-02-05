# 自训练

## 自训练算法概述

自训练算法基于亚罗夫斯基（Yarowsky）算法。它通过从未标记数据中学习，使监督分类器能够充当半监督分类器。该算法的工作方式是在标记数据和未标记数据上迭代训练监督分类器，然后使用对未标记数据的预测将这些样本的一个子集添加到标记数据中。该算法持续迭代，直到所有样本都有标签，或者在一次迭代中没有选择新的样本。

## 在scikit-learn中使用自训练

在scikit-learn中，自训练算法在`SelfTrainingClassifier`类中实现。要使用此算法，你需要提供一个实现`predict_proba`方法的监督分类器。以下是使用自训练算法的示例：

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# 创建一个逻辑回归分类器
classifier = LogisticRegression()

# 使用逻辑回归分类器作为基础分类器创建一个自训练分类器
self_training_classifier = SelfTrainingClassifier(classifier)

# 在标记数据和未标记数据上训练自训练分类器
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# 预测新样本的标签
y_pred = self_training_classifier.predict(X_test)
```

在上述示例中，`X_labeled`和`y_labeled`是标记数据，`X_unlabeled`是未标记数据，`X_test`是要预测的新样本。
