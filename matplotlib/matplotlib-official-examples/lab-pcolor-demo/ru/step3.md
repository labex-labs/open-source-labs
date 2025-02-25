# Pcolor с логарифмической шкалой

Третий шаг - создать график pcolor с логарифмической шкалой. Это полезно, когда у вас есть данные с широким диапазоном значений.

```python
N = 100
X, Y = np.meshgrid(np.linspace(-3, 3, N), np.linspace(-2, 2, N))

# Низкий горб с выступом.
# Потребуется, чтобы ось z/цветов была в логарифмической шкале, чтобы мы увидели как горб, так и выступ.
# Линейная шкала показывает только выступ.
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(X, Y, Z, shading='auto',
               norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap='PuBu_r')
fig.colorbar(c, ax=ax0)

c = ax1.pcolor(X, Y, Z, cmap='PuBu_r', shading='auto')
fig.colorbar(c, ax=ax1)

plt.show()
```
