# Definir Rótulos e Zticks

Defina os rótulos e zticks usando o método `set`. Definiremos os rótulos para as coordenadas X, Y e Z, e definiremos os zticks para mostrar a profundidade da caixa.

```python
# Set labels and zticks
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
