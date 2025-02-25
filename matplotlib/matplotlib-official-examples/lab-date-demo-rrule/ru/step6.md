# Строим график данных и настраиваем метки оси x

Наконец, вы можете построить график данных с использованием функции plot и настроить метки оси x с использованием функций локатора и форматтера меток, которые вы настроили ранее.

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
