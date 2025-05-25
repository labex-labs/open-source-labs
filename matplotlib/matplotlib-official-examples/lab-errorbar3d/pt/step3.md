# Gerar Dados para o Gráfico

Geramos os dados para o nosso gráfico criando uma curva paramétrica. Uma curva paramétrica é um conjunto de equações que descrevem as coordenadas x, y e z como uma função de um parâmetro. Usamos a função `arange` do NumPy para criar um array de valores de 0 a 2π. Em seguida, usamos esses valores para calcular as coordenadas x, y e z usando funções trigonométricas.

```python
t = np.arange(0, 2*np.pi+.1, 0.01)
x, y, z = np.sin(t), np.cos(3*t), np.sin(5*t)
```
