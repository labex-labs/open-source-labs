# Настраиваем ось x и форматируем даты

Для того, чтобы график был более читаемым, мы установим пределы оси x на первую и последнюю даты в диапазоне. Мы также установим основной и вторичный локаторы соответственно на DayLocator и HourLocator. Наконец, мы отформатируем даты с использованием функции DateFormatter. Скопируйте и вставьте следующий код:

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
