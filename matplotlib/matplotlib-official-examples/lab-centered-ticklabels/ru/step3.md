# Настройка основных и вторичных делителей и форматтеров

Для выравнивания меток посередине между делениями на шкале нам нужно настроить основные и вторичные делители и форматтеры для оси x. Мы будем использовать функцию `dates.MonthLocator()` для настройки основных и вторичных делителей на месяц и функцию `dates.DateFormatter()` для форматирования меток вторичных делений в сокращенное название месяца.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 - это небольшое приближение, так как количество дней в месяцах различается.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
