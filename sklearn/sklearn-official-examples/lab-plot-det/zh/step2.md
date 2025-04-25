# 定义分类器

我们将定义两个不同的分类器，以便使用 ROC 和 DET 曲线比较它们在不同阈值下的统计性能。我们将使用 scikit-learn 的`make_pipeline`函数创建一个管道，该管道使用`StandardScaler`对数据进行缩放，并训练一个`LinearSVC`分类器。我们还将使用 scikit-learn 的`RandomForestClassifier`类来训练一个随机森林分类器，其最大深度为 5，有 10 个估计器，最多 1 个特征。

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
