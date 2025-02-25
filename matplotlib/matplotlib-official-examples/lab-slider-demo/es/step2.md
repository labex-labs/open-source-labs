# Definir la función de la onda sinusoidal

A continuación, definiremos la función que generará nuestra onda sinusoidal. La función tomará dos parámetros, amplitud y frecuencia, y devolverá la onda sinusoidal en un momento dado.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
