# Übung 3.10: Fehler unterdrücken

Ändern Sie die `parse_csv()`-Funktion so, dass Fehler bei der Analyse unterdrückt werden können, wenn der Benutzer dies explizit wünscht. Beispielsweise:

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```

Das Fehlerhandeln ist eine der schwierigsten Dinge, die man in den meisten Programmen richtig machen muss. Im Allgemeinen sollten Sie Fehler nicht stillschweigend ignorieren. Stattdessen ist es besser, Probleme zu melden und dem Benutzer die Möglichkeit zu geben, die Fehlermeldung zu unterdrücken, wenn er dies wählt.
