# Criar dados para o gráfico

Em seguida, vamos criar alguns dados que usaremos para plotar. Usaremos a função `numpy.arange()` para criar um array de valores de 0 a 14 e armazená-lo na variável `x`. Também usaremos a função `numpy.sin()` para criar um array de valores que são o seno de cada valor em `x` dividido por 2, e armazená-lo na variável `y`.

```python
x = np.arange(14)
y = np.sin(x / 2)
```
