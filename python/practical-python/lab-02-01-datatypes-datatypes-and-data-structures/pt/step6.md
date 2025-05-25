# Desempacotamento de Tuplas (Tuple Unpacking)

Para usar a tupla em outro lugar, você pode desempacotar suas partes em variáveis.

```python
name, shares, price = s
print('Cost', shares * price)
```

O número de variáveis à esquerda deve corresponder à estrutura da tupla.

```python
name, shares = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
