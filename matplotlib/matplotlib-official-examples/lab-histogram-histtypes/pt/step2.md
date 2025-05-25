# Gerar dados aleatórios

Geraremos dois conjuntos de dados aleatórios usando a função `random.normal` do NumPy. Esses conjuntos serão usados para criar histogramas com diferentes estilos.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
