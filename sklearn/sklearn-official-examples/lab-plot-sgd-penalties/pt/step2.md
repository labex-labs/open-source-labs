# Gerando Dados

Vamos gerar alguns dados de amostra para aplicar nossas penalidades. Neste exemplo, geraremos duas classes de dados com 100 amostras cada.

```python
np.random.seed(42)

# Gerar duas classes de dados
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
