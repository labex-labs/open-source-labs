# Implementando una función pura de Python

Comenzaremos creando una función en puro Python que opere fila por fila en el DataFrame.

```python
# Define a function
def f(x):
    return x * (x - 1)

# Define another function that uses the first function
def integrate_f(a, b, N):
       s = 0
       dx = (b - a) / N
       for i in range(N):
           s += f(a + i * dx)
       return s * dx
```
