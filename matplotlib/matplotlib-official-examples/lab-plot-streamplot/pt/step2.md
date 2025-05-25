# Criar Dados

Criaremos os dados para nosso streamplot usando a biblioteca Numpy. Neste exemplo, criaremos uma meshgrid com 100 pontos em ambas as direções e calcularemos os componentes U e V do nosso campo vetorial.

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```
