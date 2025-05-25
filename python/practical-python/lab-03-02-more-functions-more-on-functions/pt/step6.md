# Múltiplos Valores de Retorno (Multiple Return Values)

Funções podem retornar apenas um valor. No entanto, uma função pode retornar múltiplos valores, retornando-os em uma tupla.

```python
def divide(a,b):
    q = a // b      # Quociente (Quotient)
    r = a % b       # Resto (Remainder)
    return q, r     # Retorna uma tupla (Return a tuple)
```

Exemplo de uso:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
