# 绘制数据并设置x轴刻度

最后，你可以使用 `plot` 函数绘制数据，并使用之前设置的刻度定位器和格式化器函数来设置x轴刻度。

```python
fig, ax = plt.subplots()
plt.plot(dates, s, 'o')
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.show()
```
