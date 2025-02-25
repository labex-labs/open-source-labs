# 位置付け関数とフォーマッタの定義

使用するさまざまな位置付け関数とフォーマッタを定義します。この例では、次の位置付け関数を使用します。

- `AutoDateLocator(maxticks=8)`
- `YearLocator(month=4)`
- `MonthLocator(bymonth=[4, 8, 12])`
- `DayLocator(interval=180)`
- `WeekdayLocator(byweekday=SU, interval=4)`
- `HourLocator(byhour=range(0, 24, 6))`
- `MinuteLocator(interval=15)`
- `SecondLocator(bysecond=(0, 30))`
- `MicrosecondLocator(interval=1000)`
- `RRuleLocator(rrulewrapper(freq=MONTHLY, byweekday=(MO, TU, WE, TH, FR), bysetpos=-1))`

および次のフォーマッタ。

- `AutoDateFormatter(ax.xaxis.get_major_locator())`
- `ConciseDateFormatter(ax.xaxis.get_major_locator())`
- `DateFormatter("%b %Y")`

```python
locators = [
    ('AutoDateLocator(maxticks=8)', '2003-02-01', '%Y-%m'),
    ('YearLocator(month=4)', '2003-02-01', '%Y-%m'),
    ('MonthLocator(bymonth=[4, 8, 12])', '2003-02-01', '%Y-%m'),
    ('DayLocator(interval=180)', '2003-02-01', '%Y-%m-%d'),
    ('WeekdayLocator(byweekday=SU, interval=4)', '2000-07-01', '%a %Y-%m-%d'),
    ('HourLocator(byhour=range(0, 24, 6))', '2000-02-04', '%H h'),
    ('MinuteLocator(interval=15)', '2000-02-01 02:00', '%H:%M'),
    ('SecondLocator(bysecond=(0, 30))', '2000-02-01 00:02', '%H:%M:%S'),
    ('MicrosecondLocator(interval=1000)', '2000-02-01 00:00:00.005', '%S.%f'),
    ('RRuleLocator(rrulewrapper(freq=MONTHLY, byweekday=(MO, TU, WE, TH, FR), '
     'bysetpos=-1))', '2000-07-01', '%Y-%m-%d'),
]

formatters = [
    'AutoDateFormatter(ax.xaxis.get_major_locator())',
    'ConciseDateFormatter(ax.xaxis.get_major_locator())',
    'DateFormatter("%b %Y")',
]
```
