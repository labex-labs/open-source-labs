# Criar dados para plotagem

Em seguida, precisamos criar alguns dados para plotar. Neste laboratório, usaremos a função seno para criar nossos dados. Geraremos 500 pontos espaçados uniformemente entre 0 e 10 e calcularemos o seno de cada ponto usando a função `np.sin()`.

```python
x = np.linspace(0, 10, 500)
y = np.sin(x)
```
