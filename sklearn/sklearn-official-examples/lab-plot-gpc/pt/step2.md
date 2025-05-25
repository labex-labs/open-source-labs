# Gerar Dados

Geraremos dados usando o NumPy. Geraremos 100 pontos de dados com uma distribuição uniforme entre 0 e 5. Definiremos o limite em 2,5 e geraremos as etiquetas usando uma expressão booleana. Usaremos os primeiros 50 pontos de dados como dados de treino e o restante como dados de teste.

```python
train_size = 50
rng = np.random.RandomState(0)
X = rng.uniform(0, 5, 100)[:, np.newaxis]
y = np.array(X[:, 0] > 2.5, dtype=int)
```
