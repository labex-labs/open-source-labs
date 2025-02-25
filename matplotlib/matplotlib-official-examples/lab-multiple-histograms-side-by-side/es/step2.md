# Crear conjuntos de datos de ejemplo

A continuación, crearemos conjuntos de datos de ejemplo para usar en nuestros histogramas. Crearemos tres conjuntos de datos con 387 puntos de datos cada uno:

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```
