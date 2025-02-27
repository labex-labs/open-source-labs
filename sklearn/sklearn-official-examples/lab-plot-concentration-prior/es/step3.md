# Establecer parámetros para el conjunto de datos de ejemplo

En este paso, establecemos los parámetros para el conjunto de datos de ejemplo, que incluyen el estado aleatorio, el número de componentes, el número de características, los colores, las covarianzas, las muestras y las medias.

```python
random_state, n_components, n_features = 2, 3, 2
colors = np.array(["#0072B2", "#F0E442", "#D55E00"])
covars = np.array(
    [[[0.7, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]]]
)
samples = np.array([200, 500, 200])
means = np.array([[0.0, -0.70], [0.0, 0.0], [0.0, 0.70]])
```
