# Extrair Sobrenomes dos Nomes Completos

Agora, vamos criar uma nova coluna `Surname` que contém o sobrenome dos passageiros. Faremos isso extraindo a parte antes da vírgula na coluna `Name`.

```python
# Dividir a coluna 'Name' na vírgula e extrair a primeira parte
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
