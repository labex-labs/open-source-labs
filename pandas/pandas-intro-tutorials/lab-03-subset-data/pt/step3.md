# Selecionando Múltiplas Colunas

Para selecionar múltiplas colunas, use uma lista de nomes de colunas dentro dos colchetes de seleção `[]`.

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```
