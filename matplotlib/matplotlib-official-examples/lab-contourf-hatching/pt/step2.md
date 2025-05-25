# Criar Dados

Em seguida, criaremos alguns dados de exemplo para plotar. Neste exemplo, criaremos uma grade 2D de valores x e y e os usaremos para calcular os valores z.

```python
# invent some numbers, turning the x and y arrays into simple
# 2d arrays, which make combining them together easier.
x = np.linspace(-3, 5, 150).reshape(1, -1)
y = np.linspace(-3, 5, 120).reshape(-1, 1)
z = np.cos(x) + np.sin(y)
```
