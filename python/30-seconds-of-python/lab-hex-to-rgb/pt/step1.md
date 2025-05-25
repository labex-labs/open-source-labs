# Conversão de Hexadecimal para RGB

Escreva uma função `hex_to_rgb(hex_code)` que recebe um código de cor hexadecimal como uma string e retorna uma tupla de inteiros correspondentes aos seus componentes RGB. A função deve realizar as seguintes etapas:

1. Use uma compreensão de lista em combinação com `int()` e a notação de fatiamento de lista para obter os componentes RGB da string hexadecimal.
2. Use `tuple()` para converter a lista resultante em uma tupla.

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
