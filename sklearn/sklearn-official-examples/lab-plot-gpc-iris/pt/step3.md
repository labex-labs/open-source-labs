# Criando uma malha para plotagem

Agora, criaremos uma malha para plotagem. A malha será usada para plotar as probabilidades previstas para cada ponto na malha. Também definiremos o tamanho do passo para a malha.

```python
h = 0.02  # tamanho do passo na malha

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
