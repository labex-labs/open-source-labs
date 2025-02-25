# Crear subgráficos

Crearemos tres subgráficos para demostrar diferentes personalizaciones de las espinas. Usaremos el diseño restringido para asegurarnos de que las etiquetas no se solapen con los ejes.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
