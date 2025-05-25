# Criar dados para as elipses

Criamos dados para nossas elipses na forma de arrays de coordenadas x, coordenadas y, largura, altura e ângulo.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
