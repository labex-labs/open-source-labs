# Idiomas Comuns para Leitura de Dados de Arquivos

Ler um arquivo inteiro de uma vez como uma string.

```python
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`
```

Ler um arquivo linha por linha, iterando.

```python
with open(filename, 'rt') as file:
    for line in file:
        # Process the line
```
