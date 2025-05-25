# Implementando Função em Python Puro

Começaremos criando uma função em Python puro que opera linha a linha no DataFrame.

```python
# Definir uma função
def f(x):
    return x * (x - 1)

# Definir outra função que usa a primeira função
def integrate_f(a, b, N):
       s = 0
       dx = (b - a) / N
       for i in range(N):
           s += f(a + i * dx)
       return s * dx
```
