# Auswählen bestimmter Zeilen und Spalten

Um sowohl Zeilen als auch Spalten auf einmal auszuwählen, verwenden wir die `loc`- oder `iloc`-Operatoren.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
