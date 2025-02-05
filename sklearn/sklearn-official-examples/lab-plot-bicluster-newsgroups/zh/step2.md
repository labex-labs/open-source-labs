# 定义数字归一化器

我们将定义一个函数 `number_normalizer()`，用于将所有数字标记映射到一个占位符。这用于降维。

```python
def number_normalizer(tokens):
    """将所有数字标记映射到一个占位符。

    对于许多应用来说，以数字开头的标记并不直接有用，但这样的标记存在这一事实可能是相关的。通过应用这种形式的降维，一些方法可能会表现得更好。
    """
    return ("#NUMBER" if token[0].isdigit() else token for token in tokens)
```
