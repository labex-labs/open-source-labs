# Setze den Markierungsgeber und den Formatierer

Du wirst die Funktion `RRuleLocator` verwenden, um den Markierungsgeber basierend auf der im vorherigen Schritt gesetzten Wiederholungsregel zu setzen. Du wirst auch die Funktion `DateFormatter` verwenden, um den Formatierer für die Markierungen zu setzen.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```
