# Establecer los colores de los contornos

Podemos forzar a que todos los contornos tengan el mismo color o establecer que los contornos negativos sean sólidos en lugar de discontinuos.

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')  # Los contornos negativos por defecto son discontinuos.
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Single color - negative contours dashed')
```

```python
plt.rcParams['contour.negative_linestyle'] = 'solid'
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 6, colors='k')  # Los contornos negativos por defecto son discontinuos.
ax.clabel(CS, fontsize=9, inline=True)
ax.set_title('Single color - negative contours solid')
```
