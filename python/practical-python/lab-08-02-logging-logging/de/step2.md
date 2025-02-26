# Wiederholung: Ausnahmen

In den Übungen haben wir eine Funktion `parse()` geschrieben, die ungefähr so aussah:

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

Richten Sie Ihre Aufmerksamkeit auf die `try-except`-Anweisung. Was sollten Sie im `except`-Block tun?

Sollten Sie eine Warnmeldung ausgeben?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

Oder ignorieren Sie es stillschweigend?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Keine der Lösungen ist zufriedenstellend, da Sie oft beide Verhaltensweisen (benutzerauswählbar) möchten.
