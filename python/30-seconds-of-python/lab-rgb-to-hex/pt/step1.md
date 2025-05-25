# Conversão de RGB para Hexadecimal

Escreva uma função `rgb_to_hex(r, g, b)` que recebe três inteiros representando os valores dos componentes vermelho, verde e azul de uma cor, e retorna uma string representando o código de cor hexadecimal. A string de saída deve estar no formato `RRGGBB`, onde `RR`, `GG` e `BB` são valores hexadecimais de dois dígitos representando os componentes vermelho, verde e azul, respectivamente.

Por exemplo, se os valores de entrada forem `255`, `165` e `1`, a saída deve ser a string `'FFA501'`.

```python
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
```

```python
rgb_to_hex(255, 165, 1) # 'FFA501'
```
