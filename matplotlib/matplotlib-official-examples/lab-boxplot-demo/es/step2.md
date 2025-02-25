# Generar los datos

A continuación, generaremos algunos datos de muestra para utilizar en nuestros diagramas de caja. Para este tutorial, utilizaremos los siguientes datos:

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
