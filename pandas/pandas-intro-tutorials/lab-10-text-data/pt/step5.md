# Encontrar o Nome Mais Longo

Vamos descobrir qual passageiro do Titanic tem o nome mais longo. Usaremos o método `str.len()` para obter o comprimento de cada nome e o método `idxmax()` para encontrar o índice do nome mais longo.

```python
# Obter o comprimento de cada nome
name_lengths = titanic["Name"].str.len()

# Encontrar o índice do nome mais longo
longest_name_index = name_lengths.idxmax()

# Obter o nome mais longo
longest_name = titanic.loc[longest_name_index, "Name"]
```
