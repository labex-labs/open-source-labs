# Liste nach Indizes sortieren

Schreiben Sie eine Funktion `sort_by_indexes(lst, indexes, reverse=False)`, die zwei Listen als Argumente nimmt und eine neue Liste zurückgibt, die basierend auf den Indizes der zweiten Liste sortiert ist. Die Funktion sollte die folgenden Parameter haben:

- `lst`: Eine Liste von Elementen, die sortiert werden sollen.
- `indexes`: Eine Liste von ganzen Zahlen, die die gewünschten Indizes darstellen, nach denen die `lst` sortiert werden soll.
- `reverse`: Ein optionaler boolescher Parameter, der, wenn auf `True` gesetzt, die Liste in umgekehrter Reihenfolge sortiert.

Die Funktion sollte eine neue Liste zurückgeben, die basierend auf den Indizes der zweiten Liste sortiert ist.

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['Eier', 'Brot', 'Orangen', 'Konfitüre', 'Äpfel', 'Milch']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['Äpfel', 'Brot', 'Eier', 'Konfitüre', 'Milch', 'Orangen']
sort_by_indexes(a, b, True)
# ['Orangen', 'Milch', 'Konfitüre', 'Eier', 'Brot', 'Äpfel']
```
