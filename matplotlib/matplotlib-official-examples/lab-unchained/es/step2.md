# Generando datos aleatorios

En este paso, generaremos datos aleatorios que usaremos para crear nuestro gráfico.

```python
# Generate random data
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X ** 2)
```
