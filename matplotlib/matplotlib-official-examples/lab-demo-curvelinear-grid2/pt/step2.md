# Definir Funções de Transformação

O segundo passo é definir as funções de transformação. Neste exemplo, usaremos a função `tr` para transformar os valores do eixo x e deixar os valores do eixo y inalterados. A função `inv_tr` será usada para inverter a transformação.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
