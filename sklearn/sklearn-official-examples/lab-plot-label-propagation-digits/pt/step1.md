# Carregar e Embaralha Dados

Primeiro, carregamos o conjunto de dados de dígitos e embaralhamos aleatoriamente os dados.

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```
