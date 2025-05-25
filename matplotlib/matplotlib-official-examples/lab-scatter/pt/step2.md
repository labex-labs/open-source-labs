# Gerar dados aleatórios

Nesta etapa, geraremos dados aleatórios para nosso gráfico de dispersão. Geraremos 50 pontos de dados para cada variável usando a biblioteca NumPy.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
