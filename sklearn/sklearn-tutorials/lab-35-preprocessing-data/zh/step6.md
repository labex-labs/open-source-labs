# 生成多项式特征

有时，通过考虑输入数据的非线性特征来增加模型的复杂度是有益的。我们可以使用 scikit-learn 中的`PolynomialFeatures`来生成多项式特征。

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# 创建一个示例数据集
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# 初始化 PolynomialFeatures
poly = PolynomialFeatures(2)

# 拟合并转换训练数据
X_poly = poly.fit_transform(X)

# 打印转换后的数据
print(X_poly)
```
