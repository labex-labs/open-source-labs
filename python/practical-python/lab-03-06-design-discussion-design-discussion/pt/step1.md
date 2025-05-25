# Nomes de Arquivos versus Iteráveis

Compare estes dois programas que retornam a mesma saída.

```python
# Provide a filename
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Provide lines
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- Qual dessas funções você prefere? Por quê?
- Qual dessas funções é mais flexível?
