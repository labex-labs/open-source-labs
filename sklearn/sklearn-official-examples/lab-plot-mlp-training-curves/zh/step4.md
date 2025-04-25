# 加载或生成小型数据集

现在，我们需要加载或生成用于此示例的小型数据集。我们将使用鸢尾花数据集、手写数字数据集，以及使用 make_circles 和 make_moons 函数生成的两个数据集。

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```
