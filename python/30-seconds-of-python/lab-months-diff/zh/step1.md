# 理解 Python 中的日期对象

在计算日期之间的月数差之前，我们需要了解如何在 Python 中处理日期对象。在这一步中，我们将学习 `datetime` 模块并创建一些日期对象。

首先，在项目目录中创建一个新的 Python 文件。打开 WebIDE，点击左侧资源管理器面板中的“新建文件”图标。将文件命名为 `month_difference.py`，并将其保存到 `/home/labex/project` 目录中。

现在，添加以下代码以导入必要的模块：

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

保存文件并使用终端运行它：

```bash
python3 ~/project/month_difference.py
```

你应该会看到类似以下的输出：

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

`datetime` 模块中的 `date` 类允许我们通过指定年、月和日来创建日期对象。当我们用一个日期减去另一个日期时，Python 会返回一个 `timedelta` 对象。我们可以使用 `.days` 属性来获取该对象中的天数。

在这个例子中，2023 年 1 月 15 日和 2023 年 3 月 20 日之间相差 64 天。
