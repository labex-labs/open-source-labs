# Generar datos de muestra

En este paso, generaremos datos de muestra utilizando numpy. Generaremos datos aleatorios a partir de una distribución normal con una media de 100 y una desviación estándar de 15.

```python
np.random.seed(19680801)
mu = 100  # media de la distribución
sigma = 15  # desviación estándar de la distribución
x = mu + sigma * np.random.randn(437)
```
