# Auswahl mehrerer Spalten

Um mehrere Spalten auszuwählen, verwenden Sie eine Liste von Spaltennamen innerhalb der Auswahlklammern `[]`.

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```
