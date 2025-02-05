# 使用支持向量机进行分类

- 首先导入必要的库：

```python
from sklearn import svm
```

- 定义训练样本 `X` 和类别标签 `y`：

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- 创建 `SVC` 分类器的实例并拟合数据：

```python
clf = svm.SVC()
clf.fit(X, y)
```

- 使用训练好的模型预测新值：

```python
clf.predict([[2., 2.]])
```
