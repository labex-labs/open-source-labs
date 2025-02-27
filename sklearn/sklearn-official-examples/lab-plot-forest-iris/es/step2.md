# Definir parámetros

En este paso, definiremos los parámetros necesarios para trazar las superficies de decisión en el conjunto de datos iris.

```python
# Parameters
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # ancho de paso fino para los contornos de la superficie de decisión
plot_step_coarser = 0.5  # anchos de paso para las adivinanzas de clasificador aproximadas
RANDOM_SEED = 13  # fija la semilla en cada iteración
```
