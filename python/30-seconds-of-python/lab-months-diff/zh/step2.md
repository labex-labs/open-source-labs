# 创建计算月数差的函数

既然我们已经了解了如何处理日期对象并计算日期之间的天数差，那么让我们来创建一个函数以计算日期之间的月数差。

在许多应用程序中，一个月通常近似为 30 天。虽然这并不总是准确的（月份的天数可以从 28 天到 31 天不等），但这是一种常见的简化方法，适用于许多商业计算。

打开你的 `month_difference.py` 文件，并在现有代码下方添加以下函数：

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

让我们来理解这个函数的功能：

1. 它接受两个参数：`start` 和 `end`，它们都是日期对象。
2. 它计算这两个日期之间的天数差。
3. 它将天数除以 30 以将其转换为月数。
4. 它使用 `ceil()` 函数将结果向上舍入到最接近的整数。
5. 它将结果作为整数返回。

使用 `ceil()` 函数是因为在许多商业场景中，出于计费目的，即使是不足一个月的部分也会被算作一个整月。

为了测试我们的函数，请在文件末尾添加以下代码：

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

保存文件并再次运行：

```bash
python3 ~/project/month_difference.py
```

你应该会看到类似以下的输出：

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

请注意：

- 2023 年 1 月 15 日和 2023 年 3 月 20 日之间的 64 天被计算为 3 个月（64 / 30 = 2.13，向上舍入为 3）。
- 10 月 28 日和 11 月 25 日之间的差值被计算为 1 个月。
- 12 月 15 日和 1 月 10 日（跨年度）之间的差值也被计算为 1 个月。
