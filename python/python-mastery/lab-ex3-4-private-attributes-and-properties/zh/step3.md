# 实现属性验证

属性还允许你控制如何检索、设置和删除属性值。这对于向你的属性添加验证非常有用，确保这些值满足特定标准。

在我们的 `Stock` 类中，我们希望确保 `shares` 是一个非负整数，而 `price` 是一个非负浮点数。我们将使用属性装饰器以及 getter 和 setter 来实现这一点。

**说明：**

1.  在编辑器中打开 `stock.py` 文件。

2.  将私有属性 `_shares` 和 `_price` 添加到 `Stock` 类，并修改构造函数以使用它们：

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  为 `shares` 和 `price` 定义具有验证的属性：

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  更新构造函数以使用属性 setter 进行验证：

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  保存 `stock.py` 文件。

6.  创建一个名为 `test_validation.py` 的测试脚本：

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  将以下代码添加到 `test_validation.py` 文件：

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  运行测试脚本：

    ```bash
    python /home/labex/project/test_validation.py
    ```

    你应该看到输出显示成功的有效更新以及无效更新的相应错误消息。

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
