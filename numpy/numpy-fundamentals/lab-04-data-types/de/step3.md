# Abrufen des Datentyps eines Arrays

Um den Datentyp eines Arrays zu bestimmen, können Sie das `dtype`-Attribut verwenden. Beispielsweise:

```python
z.dtype
# gibt den dtype des Arrays z zurück, was uint8 ist
```

Das `dtype`-Objekt enthält auch Informationen über den Typ, wie seine Bitbreite und Byte-Reihenfolge. Sie können das `dtype`-Objekt verwenden, um Eigenschaften des Typs abzufragen, wie beispielsweise, ob es eine Ganzzahl ist. Beispielsweise:

```python
d = np.dtype(int)
# erstellt ein dtype-Objekt für int

np.issubdtype(d, np.integer)
# gibt True zurück, was darauf hinweist, dass d ein Untertyp von np.integer ist

np.issubdtype(d, np.floating)
# gibt False zurück, was darauf hinweist, dass d kein Untertyp von np.floating ist
```
