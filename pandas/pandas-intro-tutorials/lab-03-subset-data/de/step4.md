# Filtern von bestimmten Zeilen

Um Zeilen basierend auf einem bedingten Ausdruck auszuwählen, verwenden Sie die Bedingung innerhalb der Auswahlklammern `[]`.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
