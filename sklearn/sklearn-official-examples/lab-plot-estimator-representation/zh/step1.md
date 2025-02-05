# 紧凑文本表示

我们可以通过紧凑文本表示来显示估计器。当估计器作为字符串显示时，只会显示已设置为非默认值的参数。这减少了视觉干扰，便于在比较实例时更容易发现差异。

```python
from sklearn.linear_model import LogisticRegression

# 创建一个使用 l1 正则化的逻辑回归实例
lr = LogisticRegression(penalty="l1")

# 显示估计器
print(lr)
```
