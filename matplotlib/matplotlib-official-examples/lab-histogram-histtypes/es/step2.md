# Generar datos aleatorios

Generaremos dos conjuntos de datos aleatorios utilizando la función `random.normal` de NumPy. Estos conjuntos se utilizarán para crear histogramas con diferentes estilos.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
