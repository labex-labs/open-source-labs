# 设置自训练分类器

我们将设置两个具有不同百分比标记数据的自训练分类器：30% 和 50%。自训练是一种半监督学习算法，它在标记数据上训练一个分类器，然后使用该分类器预测未标记数据的标签。将最有把握的预测结果添加到标记数据中，并重复此过程，直到收敛。

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# 设置自训练分类器
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
