# Generando datos

Generaremos algunos datos de muestra para aplicar nuestras penas. Para este ejemplo, generaremos dos clases de datos con 100 muestras cada una.

```python
np.random.seed(42)

# Generate two classes of data
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
