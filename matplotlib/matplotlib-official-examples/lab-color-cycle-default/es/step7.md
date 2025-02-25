# Personalizar las marcas de la escala del eje y

Personalizamos las marcas de la escala del eje y para los subgráficos más a la izquierda.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
