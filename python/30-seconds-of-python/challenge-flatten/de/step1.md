# Entschachtele eine Liste

## Problem

Schreiben Sie eine Python-Funktion namens `flatten(lst)`, die eine Liste von Listen als Argument nimmt und eine entschachtelte Liste zurückgibt. Die Funktion sollte die Liste nur einmal entfalten, was bedeutet, dass beliebige geschachtelte Listen innerhalb der ursprünglichen Liste entfaltet werden sollten, aber beliebige geschachtelte Listen innerhalb dieser geschachtelten Listen sollten unverändert bleiben.

Um dieses Problem zu lösen, können Sie eine Listenkomprehension verwenden, um jeden Wert aus den Unterlisten in der Reihenfolge zu extrahieren.

## Beispiel

```python
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```
