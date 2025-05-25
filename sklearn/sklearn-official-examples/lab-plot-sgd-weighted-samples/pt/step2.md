# Criar um Conjunto de Dados Ponderado

Criamos um conjunto de dados ponderado utilizando a biblioteca numpy. Geramos 20 pontos com valores aleatórios e atribuímos um peso maior às últimas 10 amostras.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```
