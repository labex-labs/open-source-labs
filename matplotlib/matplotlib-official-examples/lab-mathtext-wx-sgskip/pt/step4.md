# Definir Funções

Defina uma lista de funções que a aplicação irá exibir. Cada função é definida por um texto matemático (math text) e uma função lambda que recebe um valor de entrada e retorna um valor de saída.

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
