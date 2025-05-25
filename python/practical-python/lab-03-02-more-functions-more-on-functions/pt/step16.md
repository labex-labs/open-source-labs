# Exercício 3.6: Trabalhando sem Cabeçalhos

Alguns arquivos CSV não incluem nenhuma informação de cabeçalho. Por exemplo, o arquivo `prices.csv` se parece com isto:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
...
```

Modifique a função `parse_csv()` em `/home/labex/project/fileparse_3.6.py` para que ela possa trabalhar com esses arquivos, criando uma lista de tuplas em vez disso. Por exemplo:

```python
>>> prices = parse_csv('/home/labex/project/prices.csv', types=[str,float], has_headers=False)
>>> prices
[('AA', 9.22), ('AXP', 24.85), ('BA', 44.85), ('BAC', 11.27), ('C', 3.72), ('CAT', 35.46), ('CVX', 66.67), ('DD', 28.47), ('DIS', 24.22), ('GE', 13.48), ('GM', 0.75), ('HD', 23.16), ('HPQ', 34.35), ('IBM', 106.28), ('INTC', 15.72), ('JNJ', 55.16), ('JPM', 36.9), ('KFT', 26.11), ('KO', 49.16), ('MCD', 58.99), ('MMM', 57.1), ('MRK', 27.58), ('MSFT', 20.89), ('PFE', 15.19), ('PG', 51.94), ('T', 24.79), ('UTX', 52.61), ('VZ', 29.26), ('WMT', 49.74), ('XOM', 69.35)]
>>>
```

Para fazer essa alteração, você precisará modificar o código para que a primeira linha de dados não seja interpretada como uma linha de cabeçalho. Além disso, você precisará garantir que não crie dicionários, pois não haverá mais nomes de colunas para usar como chaves.
