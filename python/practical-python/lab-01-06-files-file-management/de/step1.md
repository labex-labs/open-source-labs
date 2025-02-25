# Dateieneingabe und -ausgabe

Eine Datei öffnen.

```python
f = open('foo.txt', 'rt')     # Zum Lesen (Text) öffnen
g = open('bar.txt', 'wt')     # Zum Schreiben (Text) öffnen
```

Alle Daten lesen.

```python
data = f.read()

# Nur bis zu'maxbytes' Bytes lesen
data = f.read([maxbytes])
```

Text schreiben.

```python
g.write('einige Text')
```

Beenden, wenn fertig.

```python
f.close()
g.close()
```

Dateien sollten richtig geschlossen werden, und es ist ein einfacher Schritt, den man vergisst. Daher ist der bevorzugte Ansatz, die `with`-Anweisung wie folgt zu verwenden.

```python
with open(filename, 'rt') as file:
    # Die Datei `file` verwenden
  ...
    # Keine explizite Schließung erforderlich
...Anweisungen
```

Dies schließt die Datei automatisch, wenn der Steuerfluss den eingerückten Codeblock verlässt.
