# Definieren der Schriftfunktion

In diesem Schritt definieren wir eine Funktion, die die Schrift setzt. Diese Funktion nimmt einen Schriftnamen als Argument entgegen und gibt einen String zurück, der die Schrift auf den angegebenen Namen setzt.

```python
def setfont(font):
    return rf'\font\a {font} at 14pt\a '
```
