# Crear subgráficas para las gráficas de ejemplo

Crearemos una cuadrícula de subgráficas de 3 x 3 para mostrar nuestras gráficas de ejemplo.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
