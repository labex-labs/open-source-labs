# Crear la figura y los subgráficos

En este paso, crearemos una figura con dos subgráficos para las distribuciones acumulativas. También estableceremos el tamaño de la figura en 9x4.

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
