# Construção de Listas (List construction)

Construindo uma lista do zero.

```python
records = []  # Lista inicial vazia

# Use .append() para adicionar mais itens
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

Um exemplo ao ler registros de um arquivo.

```python
records = []  # Lista inicial vazia

with open('portfolio.csv', 'rt') as f:
    next(f) # Ignora o cabeçalho (header)
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
