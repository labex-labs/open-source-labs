# Criar um histograma

Nesta etapa, criaremos um histograma usando matplotlib. Definiremos o número de bins para 50 e habilitaremos o parâmetro `density` para normalizar as alturas dos bins, de modo que a integral do histograma seja 1.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
