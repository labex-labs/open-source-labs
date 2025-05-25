# Criar dados para o gráfico

Crie alguns dados para o gráfico. Neste exemplo, criaremos arrays `x` e `y` usando a biblioteca `numpy`.

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```
