# Generar datos

A continuación, generaremos algunos datos bidimensionales aleatorios para utilizar en el histograma. Usaremos la función `random.rand()` de NumPy para generar 100 valores aleatorios para las variables `x` e `y`.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
