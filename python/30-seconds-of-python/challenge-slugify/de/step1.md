# String zu Slug Herausforderung

## Problemstellung

Schreiben Sie eine Funktion `slugify(s)`, die einen String `s` als Argument nimmt und einen Slug zurückgibt. Die Funktion sollte die folgenden Operationen durchführen:

1. Konvertieren Sie den String in Kleinbuchstaben und entfernen Sie alle führenden oder nachfolgenden Leerzeichen.
2. Ersetzen Sie alle Sonderzeichen (d.h. jedes Zeichen, das kein Buchstabe, Ziffer, Leerzeichen, Bindestrich oder Unterstrich ist) durch eine leere Zeichenfolge.
3. Ersetzen Sie alle Leerzeichen, Bindestriche und Unterstriche durch einen einzelnen Bindestrich.
4. Entfernen Sie alle führenden oder nachfolgenden Bindestriche.

## Beispiel

```python
slugify('Hello World!') # 'hello-world'
slugify('  My Example 123  ') #'my-example-123'
slugify('This is a long sentence with spaces and punctuation!') # 'this-is-a-long-sentence-with-spaces-and-punctuation'
```
