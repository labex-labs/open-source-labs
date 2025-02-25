# Establecer la semilla aleatoria y generar los datos

En este paso, estableceremos la semilla aleatoria y generaremos los datos. Generaremos 100 puntos de datos a partir de una distribución normal con una media de 200 y una desviación estándar de 25.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
