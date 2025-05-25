# Strings de Bytes

Uma string de bytes de 8 bits, comumente encontrada em operações de I/O de baixo nível, é escrita da seguinte forma:

```python
data = b'Hello World\r\n'
```

Ao colocar um 'b' minúsculo antes da primeira aspa, você especifica que é uma string de bytes em vez de uma string de texto.

A maioria das operações de string usuais funciona.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

A indexação é um pouco diferente porque retorna valores de bytes como inteiros.

```python
data[0]   # 72 (ASCII code for 'H')
```

Conversão para/de strings de texto.

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
```

O argumento `'utf-8'` especifica uma codificação de caracteres. Outros valores comuns incluem `'ascii'` e `'latin1'`.
