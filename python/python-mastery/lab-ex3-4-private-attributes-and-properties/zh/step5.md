# 协调类型验证与类变量

目前，我们的 `Stock` 类同时使用 `_types` 类变量和属性 setter 来处理类型。为了提高一致性和可维护性，我们将协调这些机制，以便它们使用相同的类型信息。

**说明：**

1.  在编辑器中打开 `stock.py` 文件。

2.  修改属性 setter 以使用 `_types` 类变量中定义的类型：

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

3.  保存 `stock.py` 文件。

4.  创建一个名为 `test_subclass.py` 的测试脚本：

    ```bash
    touch /home/labex/project/test_subclass.py
    ```

5.  将以下代码添加到 `test_subclass.py` 文件：

    ```python
    from stock import Stock
    from decimal import Decimal

    # Create a subclass with different types
    class DStock(Stock):
        _types = (str, int, Decimal)

    # Test the base class
    s = Stock('GOOG', 100, 490.10)
    print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

    # Test valid update with float
    try:
        s.price = 500.25
        print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
    except Exception as e:
        print(f"Error updating Stock price: {e}")

    # Test the subclass with Decimal
    ds = DStock('AAPL', 50, Decimal('142.50'))
    print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

    # Test invalid update with float (should require Decimal)
    try:
        ds.price = 150.75
        print(f"Updated DStock price: {ds.price}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")

    # Test valid update with Decimal
    try:
        ds.price = Decimal('155.25')
        print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")
    ```

6.  运行测试脚本：

    ```bash
    python /home/labex/project/test_subclass.py
    ```

    你应该看到基类 `Stock` 接受价格的浮点数值（float values），而子类 `DStock` 需要 `Decimal` 值。

    ```plaintext
    Stock: GOOG, Shares: 100, Price: 490.1, Cost: 49010.0
    Updated Stock price: 500.25, Cost: 50025.0
    DStock: AAPL, Shares: 50, Price: 142.50, Cost: 7125.00
    Error updating DStock price: Expected Decimal
    Updated DStock price: 155.25, Cost: 7762.50
    ```
