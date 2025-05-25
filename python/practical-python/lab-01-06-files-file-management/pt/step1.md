# Entrada e Saída de Arquivos

Abrir um arquivo.

```python
f = open('foo.txt', 'rt')     # Open for reading (text)
g = open('bar.txt', 'wt')     # Open for writing (text)
```

Ler todos os dados.

```python
data = f.read()

# Read only up to 'maxbytes' bytes
data = f.read([maxbytes])
```

Escrever algum texto.

```python
g.write('some text')
```

Fechar quando terminar.

```python
f.close()
g.close()
```

Arquivos devem ser fechados corretamente, e é fácil esquecer essa etapa. Portanto, a abordagem preferida é usar a instrução `with`, assim:

```python
with open(filename, 'rt') as file:
    # Use the file `file`
    ...
    # No need to close explicitly
...statements
```

Isso fecha automaticamente o arquivo quando o controle sai do bloco de código indentado.
