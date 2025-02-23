# Relación de aspecto del contenedor para muchos subplots

Es posible pasar la relación de aspecto del contenedor a un Eje durante la inicialización. Lo siguiente crea una cuadrícula de subplots de 2 por 3 con todos los Ejes cuadrados.

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
