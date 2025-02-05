# 定义日期和时间间隔

接下来，我们将使用 datetime 库定义日期和时间间隔值。日期范围是从 2000 年 3 月 2 日到 2000 年 3 月 6 日，时间间隔为 6 小时。复制并粘贴以下代码：

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
