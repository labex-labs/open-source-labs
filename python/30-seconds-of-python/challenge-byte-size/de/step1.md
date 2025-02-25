# Byte-Größe eines Strings

## Problemstellung

Schreiben Sie eine Funktion `byte_size(s)`, die einen String `s` als Eingabe nimmt und seine Byte-Größe zurückgibt. Die Byte-Größe eines Strings ist die Anzahl der Bytes, die erforderlich sind, um den String im Speicher zu speichern. Um die Byte-Größe eines Strings zu berechnen, müssen Sie den String mit einem bestimmten Codierungsschema codieren. In dieser Herausforderung werden Sie das UTF-8-Codierungsschema verwenden.

Um die Byte-Größe eines Strings zu berechnen, können Sie die folgenden Schritte ausführen:

1. Codieren Sie den String mit dem UTF-8-Codierungsschema.
2. Bestimmen Sie die Länge des codierten Strings.

Ihre Funktion sollte die Länge des codierten Strings zurückgeben.

## Beispiel

```python
byte_size('😀') # 4
byte_size('Hello World') # 11
```

Im obigen Beispiel ist die Byte-Größe des Strings `'😀'` 4, da es 4 Bytes benötigt, um die UTF-8-codierte Version des Strings im Speicher zu speichern. Die Byte-Größe des Strings `'Hello World'` ist 11, da es 11 Bytes benötigt, um die UTF-8-codierte Version des Strings im Speicher zu speichern.
