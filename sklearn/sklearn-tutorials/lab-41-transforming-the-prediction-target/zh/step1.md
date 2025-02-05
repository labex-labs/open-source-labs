# 标签二值化

标签二值化是将多类标签转换为二元指示矩阵的过程。可以使用 `LabelBinarizer` 类来实现。

```python
from sklearn import preprocessing

# 创建一个 LabelBinarizer 实例
lb = preprocessing.LabelBinarizer()

# 在多类标签列表上拟合 LabelBinarizer
lb.fit([1, 2, 6, 4, 2])

# 获取 LabelBinarizer 学习到的类别
lb.classes_

# 将多类标签列表转换为二元指示矩阵
lb.transform([1, 6])
```
