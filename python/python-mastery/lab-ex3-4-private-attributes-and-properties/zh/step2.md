# 将方法转换为属性

Python 中的属性（Properties）允许你像访问属性一样访问计算值。这消除了调用方法时使用括号的需要，使你的代码更简洁和一致。

目前，我们的 `Stock` 类有一个 `cost()` 方法，用于计算股票的总成本。

```python
def cost(self):
    return self.shares * self.price
```

要获取成本值，我们必须使用括号调用它：

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

我们可以通过将 `cost()` 方法转换为属性来改进这一点，从而允许我们在没有括号的情况下访问成本值：

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**说明：**

1.  在编辑器中打开 `stock.py` 文件。

2.  使用 `@property` 装饰器将 `cost()` 方法替换为属性：

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  保存 `stock.py` 文件。

4.  在编辑器中创建一个名为 `test_property.py` 的新文件：

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  将以下代码添加到 `test_property.py` 文件，以创建一个 `Stock` 实例并访问 `cost` 属性：

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  运行测试脚本：

    ```bash
    python /home/labex/project/test_property.py
    ```

    你应该看到类似于以下的输出：

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
