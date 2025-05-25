# Definir o layout do gráfico 3D

Definimos o layout do gráfico 3D usando uma lista de listas. O `'.'` na lista representa um _subplot_ vazio.

```python
layout = [['XY',  '.',   'L',   '.'],
          ['XZ', 'YZ', '-XZ', '-YZ'],
          ['.',   '.', '-XY',   '.']]
```
