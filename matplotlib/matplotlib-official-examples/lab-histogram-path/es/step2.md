# Establecer la semilla aleatoria y generar datos

Usaremos numpy para generar datos aleatorios. Para que nuestros resultados sean reproducibles, estableceremos una semilla aleatoria. Agrega el siguiente código a tu archivo:

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```
