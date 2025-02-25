# Anzahl der Datensätze nach Kategorie zählen

Schließlich werden wir die Anzahl der Datensätze nach Kategorie zählen.

```python
# Counting the number of passengers in each of the cabin classes
passengers_per_class = titanic["Pclass"].value_counts()
# Printing the result
print(f"The number of passengers in each of the cabin classes is {passengers_per_class}")
```
