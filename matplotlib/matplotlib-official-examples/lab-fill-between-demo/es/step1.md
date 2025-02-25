# Uso básico

La función `fill_between` se puede utilizar para rellenar el área entre dos líneas. Los parámetros _y1_ y _y2_ pueden ser escalares, lo que indica un límite horizontal en los valores de y dados. Si solo se da _y1_, _y2_ por defecto es 0.

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('rellenar entre y1 y 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('rellenar entre y1 y 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('rellenar entre y1 y y2')
ax3.set_xlabel('x')
fig.tight_layout()
```
