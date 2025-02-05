# 创建管道

接下来，我们创建一个管道，它由一个特征选择变换、一个缩放器和一个支持向量机（SVM）实例组成，我们将它们组合在一起以形成一个功能完备的估计器。

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = Pipeline(
    [
        ("anova", SelectPercentile(f_classif)),
        ("scaler", StandardScaler()),
        ("svc", SVC(gamma="auto")),
    ]
)
```
