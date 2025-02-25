# Personalizar los límites y el aspecto de los ejes

Personalizaremos los límites y el aspecto de cada eje utilizando los métodos `set_xlim`, `set_ylim` y `tick_params`.

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```
