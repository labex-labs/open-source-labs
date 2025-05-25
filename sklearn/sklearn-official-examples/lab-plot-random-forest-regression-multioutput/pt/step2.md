# Criar um Conjunto de Dados Aleatório

Em seguida, criaremos um conjunto de dados aleatório para usar em nossa regressão. Usaremos `numpy` para criar um conjunto de 600 valores de x entre -100 e 100, e os valores correspondentes de y calculados a partir do seno e cosseno dos valores de x mais algum ruído aleatório.

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
