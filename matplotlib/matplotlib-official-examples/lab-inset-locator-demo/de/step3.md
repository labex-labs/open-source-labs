# Entfernen von Skalenmarkierungen

Um die Skalenmarkierungen von jedem der Einfügebereiche zu entfernen, können wir die `tick_params()`-Methode verwenden und `labelleft` und `labelbottom` auf `False` setzen.

```python
# Entfernen Sie die Skalenmarkierungen der Einfügebereiche
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```
