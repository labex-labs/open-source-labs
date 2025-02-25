# Форматирование графика

Теперь мы отформатируем график, добавив метки по осям x и y, настроив основной делитель и форматтер оси x, а также удалив ось y и контуры. Вот код для форматирования графика:

```python
# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
```
