# Definir a Função do Ticker Personalizado

Em seguida, precisamos definir a função do ticker (marcador) personalizado. A função do ticker personalizado recebe dois argumentos - o valor e a posição do tick - e retorna o rótulo do tick formatado. Neste caso, formataremos o rótulo do tick como dólares em milhões.

```python
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'${x*1e-6:1.1f}M'
```
