# Criando Dados de Teste Aleatórios

Em seguida, criaremos dados de teste aleatórios usando a biblioteca `numpy`. Geraremos 3 conjuntos de dados, cada um com um desvio padrão diferente.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
