# Ideia Profunda: "Duck Typing"

[Duck Typing](https://en.wikipedia.org/wiki/Duck_typing) é um conceito de programação de computadores para determinar se um objeto pode ser usado para um propósito específico. É uma aplicação do [teste do pato](https://en.wikipedia.org/wiki/Duck_test).

> Se parece com um pato, nada como um pato e grasna como um pato, então provavelmente é um pato.

Na segunda versão de `read_data()` acima, a função espera qualquer objeto iterável. Não apenas as linhas de um arquivo.

```python
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
```

Isso significa que podemos usá-la com outras _linhas_.

```python
# A CSV file
lines = open('data.csv')
data = read_data(lines)

# A zipped file
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# The Standard Input
lines = sys.stdin
data = read_data(lines)

# A list of strings
lines = ['ACME,50,91.1','IBM,75,123.45', ... ]
data = read_data(lines)
```

Há considerável flexibilidade com este design.

_Pergunta: Devemos abraçar ou lutar contra essa flexibilidade?_
