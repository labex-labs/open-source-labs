# 加载数据

我们将使用 scikit-learn 中的乳腺癌数据集。这个数据集有 30 个特征和一个二元目标变量，用于指示患者患的是恶性还是良性癌症。

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```
