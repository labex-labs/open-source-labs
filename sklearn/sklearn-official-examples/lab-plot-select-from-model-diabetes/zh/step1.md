# 加载数据

我们从 scikit-learn 中加载糖尿病数据集并打印其描述。

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```
