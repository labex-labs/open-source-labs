# Iteração e Busca em Listas

Use `for` para iterar sobre o conteúdo da lista.

```python
for name in names:
    # use name
    # e.g. print(name)
    ...
```

Isso é similar a uma instrução `foreach` de outras linguagens de programação.

Para encontrar a posição de algo rapidamente, use `index()`.

```python
names = ['Elwood','Jake','Curtis']
names.index('Curtis')   # 2
```

Se o elemento estiver presente mais de uma vez, `index()` retornará o índice da primeira ocorrência.

Se o elemento não for encontrado, isso irá levantar uma exceção `ValueError`.
