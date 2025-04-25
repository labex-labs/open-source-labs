# 计算验证分数

我们将使用 scikit-learn 中的`validation_curve`函数来计算具有不同 gamma 值的支持向量机（SVM）分类器的训练分数和验证分数。

```python
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve

train_scores, test_scores = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    scoring="accuracy",
    n_jobs=2,
)
```
