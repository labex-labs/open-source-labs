# Выбор определенных строк и столбцов

Для одновременного выбора строк и столбцов мы используем операторы `loc` или `iloc`.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
