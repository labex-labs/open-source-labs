# Implémentation d'une fonction en Python pur

Nous commencerons par créer une fonction en Python pur qui opère ligne par ligne sur le DataFrame.

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
