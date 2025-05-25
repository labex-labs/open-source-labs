# Gerar uma imagem falsa

Primeiramente, geraremos uma imagem em tons de cinza falsa usando o módulo `random` do NumPy. Definiremos a semente (seed) para garantir que os resultados sejam reproduzíveis.

```python
np.random.seed(19680801)
N = 128
img = np.random.randn(N, N)
```
