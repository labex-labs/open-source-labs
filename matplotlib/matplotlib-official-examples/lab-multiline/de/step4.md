# Anpassen der Achsenbeschriftungen

Um die Achsenbeschriftungen anzupassen, können wir die Funktionen `set_xlabel` und `set_ylabel` verwenden. Wir können auch Zeilenumbrüche mit dem Zeichens "\n" hinzufügen.

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```
