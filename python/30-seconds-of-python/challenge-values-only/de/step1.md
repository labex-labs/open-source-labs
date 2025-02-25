# Dictionary-Werte

## Problem

Es wird Ihnen ein flaches Dictionary gegeben, und Sie müssen eine Funktion erstellen, die eine flache Liste aller Werte im Dictionary zurückgibt. Ihre Aufgabe ist es, die Funktion `values_only(flat_dict)` zu implementieren, die ein flaches Dictionary als Argument nimmt und eine Liste aller Werte im Dictionary zurückgibt.

Um dieses Problem zu lösen, können Sie die Methode `dict.values()` verwenden, um die Werte im gegebenen Dictionary zurückzugeben. Anschließend können Sie das Ergebnis mithilfe der Funktion `list()` in eine Liste umwandeln.

## Beispiel

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
