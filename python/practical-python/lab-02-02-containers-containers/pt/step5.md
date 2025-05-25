# Construção de Dicionários (Dict Construction)

Exemplo de construção de um dicionário do zero.

```python
prices = {} # Dicionário inicial vazio

# Insere novos itens
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

Um exemplo preenchendo o dicionário a partir do conteúdo de um arquivo.

```python
prices = {} # Dicionário inicial vazio

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

Observação: Se você tentar isso no arquivo `prices.csv`, você descobrirá que quase funciona - há uma linha em branco no final que faz com que ele trave. Você precisará descobrir alguma maneira de modificar o código para levar isso em consideração (veja o Exercício 2.6).
