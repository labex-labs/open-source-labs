# Set the x-axis and format the dates

To make the graph more readable, we will set the x-axis limits to the first and last dates in the range. We will also set the major and minor locators to DayLocator and HourLocator, respectively. Finally, we will format the dates using the DateFormatter function. Copy and paste the following code:

```
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
