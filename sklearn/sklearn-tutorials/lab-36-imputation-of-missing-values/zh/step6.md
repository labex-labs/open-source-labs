# 使用 MissingIndicator 标记插补值

`MissingIndicator`转换器对于指示数据集中缺失值的存在很有用。它可以与插补结合使用，以保留有关哪些值被插补的信息。此转换器返回一个二进制矩阵，指示数据集中缺失值的存在情况。

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
