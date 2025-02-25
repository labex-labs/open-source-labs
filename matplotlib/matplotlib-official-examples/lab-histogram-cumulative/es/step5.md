# Etiquetar la figura

En este paso, etiquetaremos la figura. Agregaremos un título, líneas de cuadrícula y etiquetas para los ejes x e y.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```
