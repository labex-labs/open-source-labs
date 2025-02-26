# Globale Variablen

Funktionen können frei auf die Werte von globalen Variablen zugreifen, die in der selben Datei definiert sind.

```python
name = 'Dave'

def greeting():
    print('Hello', name)  # Verwenden der globalen Variable `name`
```

Funktionen können globale Variablen jedoch nicht verändern:

```python
name = 'Dave'

def spam():
  name = 'Guido'

spam()
print(name) # Gibt 'Dave' aus
```

**Denken Sie daran: Alle Zuweisungen in Funktionen sind lokal.**
