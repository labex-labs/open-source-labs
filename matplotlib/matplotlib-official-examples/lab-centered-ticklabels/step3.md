# Set the Major and Minor Locators and Formatters

To center the labels between ticks, we need to set the major and minor locators and formatters for the x-axis. We will use the `dates.MonthLocator()` function to set the major and minor locators to the month and the `dates.DateFormatter()` function to format the minor tick labels to the month abbreviation.

```python
import matplotlib.dates as dates
import matplotlib.ticker as ticker

ax.xaxis.set_major_locator(dates.MonthLocator())
# 16 is a slight approximation since months differ in number of days.
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=16))

ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
```
