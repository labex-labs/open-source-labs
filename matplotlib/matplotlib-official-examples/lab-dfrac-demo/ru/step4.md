# Построение графика с использованием \frac

Мы построим график с использованием макроса TeX \frac и отобразим полученный график.

```python
ax.plot(x, y, label=r'$\frac{sin(x)}{x}$')
ax.legend()
plt.show()
```
