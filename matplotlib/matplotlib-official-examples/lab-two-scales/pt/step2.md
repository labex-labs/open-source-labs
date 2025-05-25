# Criar Dados Fictícios (Mock Data)

Em seguida, criaremos alguns dados fictícios para usar em nossos gráficos. Usaremos `numpy.arange` para criar um array de valores variando de 0.01 a 10.0 com um passo de 0.01. Em seguida, usaremos `numpy.exp` e `numpy.sin` para criar dois conjuntos de dados.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
