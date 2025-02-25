# Crear círculos

Vamos a crear círculos con los colores del ciclo de colores predeterminado.

```python
# Create circles
fig, ax = plt.subplots()
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy = np.random.normal(size=2)
    ax.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
ax.axis('equal')
ax.margins(0)
plt.show()
```
