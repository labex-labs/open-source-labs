# Criando o Círculo

Criaremos o círculo usando a função `make_circle()`. A função recebe o raio do círculo como entrada e retorna as coordenadas x e y do círculo.

```python
def make_circle(r):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
```
