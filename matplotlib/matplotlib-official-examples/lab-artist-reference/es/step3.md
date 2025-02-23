# Dibujar formas

Ahora dibujaremos las formas utilizando Matplotlib iterando a través de la lista `shapes` y agregándolas a la gráfica.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
