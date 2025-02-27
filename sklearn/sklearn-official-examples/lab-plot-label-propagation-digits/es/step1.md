# Cargar y barajar los datos

Primero cargamos el conjunto de datos de dígitos y barajamos los datos aleatoriamente.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
