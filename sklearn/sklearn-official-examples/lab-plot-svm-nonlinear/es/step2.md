# Generar datos

En este paso, generaremos los datos para entrenar y probar el clasificador SVM. Generaremos 300 puntos de datos aleatorios con dos características. El objetivo a predecir es una operación XOR de las entradas.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
