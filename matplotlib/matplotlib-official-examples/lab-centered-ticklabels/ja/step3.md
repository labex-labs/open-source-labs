# 大目盛りと小目盛りのロケータとフォーマッタを設定する

目盛りの間にラベルを中央に配置するには、x軸の大目盛りと小目盛りのロケータとフォーマッタを設定する必要があります。大目盛りと小目盛りのロケータを月に設定するために`dates.MonthLocator()`関数を、小目盛りのラベルを月の略称にフォーマットするために`dates.DateFormatter()`関数を使用します。

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16は、月の日数が異なるためわずかな近似値です。
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
