# 编码分类特征

分类特征在用于机器学习算法之前需要被编码为数值。我们可以使用 scikit-learn 中的`OrdinalEncoder`和`OneHotEncoder`来编码分类特征。

```python
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

# 创建一个示例数据集
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

# 初始化 OrdinalEncoder
ordinal_encoder = OrdinalEncoder()

# 拟合并转换训练数据
X_encoded = ordinal_encoder.fit_transform(X)

# 打印转换后的数据
print(X_encoded)

# 初始化 OneHotEncoder
onehot_encoder = OneHotEncoder()

# 拟合并转换训练数据
X_onehot = onehot_encoder.fit_transform(X)

# 打印转换后的数据
print(X_onehot.toarray())
```
