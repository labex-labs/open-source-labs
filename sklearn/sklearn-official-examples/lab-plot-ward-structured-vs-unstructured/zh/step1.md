# 生成数据

我们首先使用 Scikit-learn 中的 `make_swiss_roll` 函数生成瑞士卷数据集。瑞士卷数据集是一个呈螺旋形状的三维数据集。

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# 使其更薄
X[:, 1] *= 0.5
```
