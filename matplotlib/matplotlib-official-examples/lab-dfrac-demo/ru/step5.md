# Построение графика с использованием \dfrac

Мы построим график с использованием макроса TeX \dfrac и отобразим полученный график.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
