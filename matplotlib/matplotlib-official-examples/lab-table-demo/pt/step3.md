# Criar Rótulos de Linha

Criaremos rótulos de linha para o conjunto de dados para representar o número de anos para os quais a perda foi registrada. Usaremos uma compreensão de lista (list comprehension) para criar os rótulos de linha.

```python
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
```
