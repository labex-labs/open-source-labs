# Criar um Conjunto de Dados Aleatório

Neste passo, criaremos um conjunto de dados aleatório. Usaremos a biblioteca `numpy` para criar um array ordenado de 100 elementos, com valores aleatórios de 0 a 200, depois subtrairemos 100 de cada elemento. Em seguida, usaremos `numpy` para calcular o seno e o cosseno de cada elemento e juntar esses arrays em um array 2D com forma (100, 2) para criar o array `y`. Também adicionaremos ruído aleatório a cada quinto elemento.

```python
# Criar um conjunto de dados aleatório
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y[::5, :] += 0.5 - rng.rand(20, 2)
```
