# Generar datos

En este paso, generaremos una matriz de Hilbert de 10x10 y estableceremos la variable objetivo y como un vector de unos.

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
