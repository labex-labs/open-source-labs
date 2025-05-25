# 주요 및 보조 로케이터와 포맷터 설정

눈금 사이의 레이블을 가운데 정렬하려면 x 축에 대한 주요 및 보조 로케이터와 포맷터를 설정해야 합니다. `dates.MonthLocator()` 함수를 사용하여 주요 및 보조 로케이터를 월로 설정하고, `dates.DateFormatter()` 함수를 사용하여 보조 눈금 레이블을 월 약어로 포맷합니다.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 is a slight approximation since months differ in number of days.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
