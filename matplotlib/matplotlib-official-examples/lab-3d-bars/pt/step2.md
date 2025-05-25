# Criar Dados Falsos

No segundo passo, criaremos dados falsos para usar no gráfico.

```python
# fake data
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1
```
