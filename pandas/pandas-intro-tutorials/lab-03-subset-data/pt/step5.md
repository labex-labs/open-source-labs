# Selecionando Linhas e Colunas Específicas

Para selecionar tanto linhas quanto colunas de uma só vez, usamos os operadores `loc` ou `iloc`.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
