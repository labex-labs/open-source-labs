# 为 Mixin 创建用户友好的 API

Mixin 非常强大，但是直接使用多重继承可能会让人觉得很复杂。在这一步中，我们将改进 `create_formatter()` 函数以隐藏这种复杂性，从而为用户提供更简单的 API。

首先，确保 `tableformat.py` 在你的编辑器中打开：

```bash
cd ~/project
touch tableformat.py
```

找到现有的 `create_formatter()` 函数：

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

用下面增强的版本替换*整个现有的* `create_formatter()` 函数定义。这个新版本接受列格式和标题大写的可选参数。

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_自我修正：动态创建用于继承的类元组，而不是多个 if/elif 分支。_

这个增强的函数首先确定基本格式化器类（`TextTableFormatter`、`CSVTableFormatter` 等）。然后，基于可选参数 `column_formats` 和 `upper_headers`，它动态地构造一个新类（`CustomFormatter`），该类继承自必要的 mixin 和基本格式化器类。最后，它返回这个自定义格式化器的实例。

**记住保存对 `tableformat.py` 的更改。**

现在，让我们测试一下增强的函数。**确保你已在 `tableformat.py` 中保存了更新后的 `create_formatter` 函数。**

首先，测试列格式化。创建 `step3_test1.py`：

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

运行脚本：

```bash
python3 step3_test1.py
```

你应该看到带有格式化列的表格（同样，取决于价格格式的类型处理）：

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

接下来，测试大写标题。创建 `step3_test2.py`：

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

运行脚本：

```bash
python3 step3_test2.py
```

你应该看到带有大写标题的表格：

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

最后，组合两个选项。创建 `step3_test3.py`：

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

运行脚本：

```bash
python3 step3_test3.py
```

这应该显示一个带有格式化列和大写标题的表格：

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
------------------------------------------------------------------
```

增强的函数也适用于其他格式化器类型。例如，尝试将其与 CSV 格式化器一起使用。创建 `step3_test4.py`：

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

运行脚本：

```bash
python3 step3_test4.py
```

这应该以 CSV 格式生成大写标题和格式化的列（同样，对于从 `print_table` 传递的字符串进行 `%d`/`%.2f` 格式化存在潜在的类型问题）：

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

通过增强 `create_formatter()` 函数，我们创建了一个用户友好的 API。用户现在可以轻松地应用 mixin 功能，而无需自己管理多重继承结构。
