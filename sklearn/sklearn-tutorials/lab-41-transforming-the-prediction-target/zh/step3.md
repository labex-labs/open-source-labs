# 标签编码

标签编码是将非数字标签转换为数字标签的过程。这可以使用 `LabelEncoder` 类来实现。

```python
from sklearn import preprocessing

# 创建一个 LabelEncoder 实例
le = preprocessing.LabelEncoder()

# 在非数字标签列表上拟合 LabelEncoder
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# 获取 LabelEncoder 学习到的类别
list(le.classes_)

# 将非数字标签列表转换为数字标签
le.transform(["tokyo", "tokyo", "paris"])

# 将数字标签反向转换回非数字标签
list(le.inverse_transform([2, 2, 1]))
```
