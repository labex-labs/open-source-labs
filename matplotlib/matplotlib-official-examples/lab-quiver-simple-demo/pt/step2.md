# Criar Dados

Precisamos criar as coordenadas `X` e `Y` usando a função `np.meshgrid()`. Em seguida, criamos os arrays `U` e `V` que representam os campos vetoriais.

```python
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
```
