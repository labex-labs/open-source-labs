# Definir Dados

O próximo passo é definir os dados que usaremos em nosso gráfico. Usaremos a função `arange` do NumPy para criar um array de valores de 0 a 5 com um passo de 0.1. Usaremos este array como o eixo x. Também definiremos o eixo y usando a função exponencial e a função seno do NumPy.

```python
# Define the data
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```
