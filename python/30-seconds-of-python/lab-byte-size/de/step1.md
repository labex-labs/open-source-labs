# Bytegröße eines Strings

Schreiben Sie eine Funktion `byte_size(s)`, die einen String `s` als Eingabe nimmt und seine Bytegröße zurückgibt. Die Bytegröße eines Strings ist die Anzahl der Bytes, die erforderlich sind, um den String im Speicher zu speichern. Um die Bytegröße eines Strings zu berechnen, müssen Sie den String mit einem bestimmten Codierungsschema codieren. In diesem Lab verwenden Sie das UTF-8-Codierungsschema.

Um die Bytegröße eines Strings zu berechnen, können Sie die folgenden Schritte ausführen:

1. Codieren Sie den String mit dem UTF-8-Codierungsschema.
2. Ermitteln Sie die Länge des codierten Strings.

Ihre Funktion sollte die Länge des codierten Strings zurückgeben.

```python
def byte_size(s):
  return len(s.encode('utf-8'))
```

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```
