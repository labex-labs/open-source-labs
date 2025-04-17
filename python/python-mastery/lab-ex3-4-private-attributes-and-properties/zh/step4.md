# 使用 `__slots__` 进行内存优化

`__slots__` 属性限制了一个类可以拥有的属性。它阻止向实例添加新属性并减少内存使用。

在我们的 `Stock` 类中，我们将使用 `__slots__` 来：

1.  将属性创建限制为仅我们已定义的属性。
2.  提高内存效率，尤其是在创建多个实例时。

**说明：**

1.  在编辑器中打开 `stock.py` 文件。
2.  添加一个 `__slots__` 类变量，列出该类使用的所有私有属性名称：

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  保存文件。

4.  创建一个名为 `test_slots.py` 的测试脚本：

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  将以下代码添加到 `test_slots.py` 文件：

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  运行测试脚本：

    ```bash
    python /home/labex/project/test_slots.py
    ```

    你应该看到输出显示你可以访问已定义的属性，但尝试添加新属性会引发 `AttributeError`（属性错误）。

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
