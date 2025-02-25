# Generar datos

Generaremos algunos datos aleatorios para utilizar en nuestros ejemplos. Utilizaremos la función `random.lognormal()` de NumPy para generar datos log-normales con una media de 1.5 y una desviación estándar de 1.75. Generaremos 37 muestras de 4 variables y las almacenaremos en la variable `data`. También crearemos una lista de etiquetas para cada variable.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
