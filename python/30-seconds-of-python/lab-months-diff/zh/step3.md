# 使用各种日期场景进行测试

为了更好地理解我们的 `months_diff` 函数在不同日期场景下的工作方式，让我们创建一个单独的测试文件。这种方法在软件开发中很常见，用于验证我们的代码是否按预期工作。

在 `/home/labex/project` 目录下创建一个名为 `month_diff_test.py` 的新文件：

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

保存此文件并运行：

```bash
python3 ~/project/month_diff_test.py
```

你应该会看到类似以下的输出：

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

让我们来分析这些结果：

1. **同月**：即使在同一个月内，我们的函数也会返回 1 个月。这是因为即使是不足一个月的部分也会被算作一个整月。
2. **连续月份**：对于连续月份的日期，函数返回 1 个月。
3. **跨年**：对于跨年的日期，函数仍然能正确计算。
4. **间隔数月**：对于间隔数月的日期，函数能计算出合适的月数。
5. **顺序颠倒**：当结束日期早于开始日期时，我们会得到一个负数结果，这在计算剩余时间等场景中是合理的。
6. **整倍数**：对于正好 30 天的情况，我们得到 1 个月；对于 60 天的情况，我们得到 2 个月。这证实了我们的函数在符合我们对月的定义的整倍数情况下能按预期工作。

根据我们将一个月定义为 30 天的规则，我们的 `months_diff` 函数能正确处理所有这些测试用例。
