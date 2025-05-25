# Tamanho em Bytes de uma String

Escreva uma função `byte_size(s)` que recebe uma string `s` como entrada e retorna seu tamanho em bytes. O tamanho em bytes de uma string é o número de bytes necessários para armazenar a string na memória. Para calcular o tamanho em bytes de uma string, você precisa codificar a string usando um esquema de codificação específico. Neste laboratório, você usará o esquema de codificação UTF-8.

Para calcular o tamanho em bytes de uma string, você pode seguir estas etapas:

1.  Codifique a string usando o esquema de codificação UTF-8.
2.  Obtenha o comprimento da string codificada.

Sua função deve retornar o comprimento da string codificada.

```python
def byte_size(s):
  return len(s.encode('utf-8'))
```

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```
