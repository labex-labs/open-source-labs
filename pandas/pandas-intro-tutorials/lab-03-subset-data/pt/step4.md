# Filtrando Linhas Específicas

Para selecionar linhas com base em uma expressão condicional, use a condição dentro dos colchetes de seleção `[]`.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
