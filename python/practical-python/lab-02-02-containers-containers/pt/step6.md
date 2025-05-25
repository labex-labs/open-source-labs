# Pesquisas em Dicionários (Dictionary Lookups)

Você pode testar a existência de uma chave.

```python
if key in d:
    # SIM
else:
    # NÃO
```

Você pode pesquisar um valor que pode não existir e fornecer um valor padrão caso ele não exista.

```python
name = d.get(key, default)
```

Um exemplo:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
