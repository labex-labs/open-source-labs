# Cargar y preparar el conjunto de datos

Cargamos el conjunto de datos de dígitos y lo preparamos para el agrupamiento extrayendo los datos y las etiquetas de destino. También establecemos la semilla aleatoria en cero para garantizar la reproducibilidad.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
