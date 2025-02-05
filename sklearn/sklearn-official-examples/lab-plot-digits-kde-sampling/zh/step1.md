# 加载数据

首先，我们从 scikit-learn 中加载数字数据集。这个数据集包含了从 0 到 9 的数字的 8x8 图像。我们将使用主成分分析（Principal Component Analysis，PCA）将数据集的维度降至 15。

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# 加载数字数据集
digits = load_digits()

# 使用 PCA 将数据集的维度降至 15
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
