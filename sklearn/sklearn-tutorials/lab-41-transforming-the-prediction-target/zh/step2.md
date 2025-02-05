# 多标签二值化

多标签二值化是将标签集合的集合转换为指示格式的过程。这可以使用 `MultiLabelBinarizer` 类来实现。

```python
from sklearn.preprocessing import MultiLabelBinarizer

# 定义一个标签集合的列表
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# 创建一个 MultiLabelBinarizer 实例并对标签集合列表进行拟合和转换
MultiLabelBinarizer().fit_transform(y)
```
