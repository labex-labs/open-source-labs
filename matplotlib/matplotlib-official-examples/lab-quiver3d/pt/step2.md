# Criar a Grade

Em seguida, criaremos uma grade de pontos na qual exibiremos o campo vetorial. Neste exemplo, criaremos uma meshgrid de pontos usando a função `meshgrid` do NumPy. A função `arange` é usada para criar um array de pontos espaçados uniformemente dentro de um intervalo especificado.

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```
