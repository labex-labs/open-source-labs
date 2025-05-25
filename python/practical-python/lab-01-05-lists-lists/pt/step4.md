# Remoção de Listas

Você pode remover itens por valor do elemento ou por índice:

```python
# Using the value
names.remove('Curtis')

# Using the index
del names[1]
```

Remover um item não cria um buraco. Outros itens se moverão para baixo para preencher o espaço vago. Se houver mais de uma ocorrência do elemento, `remove()` removerá apenas a primeira ocorrência.
