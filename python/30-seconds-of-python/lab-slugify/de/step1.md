# String zu Slug

Schreiben Sie eine Funktion `slugify(s)`, die einen String `s` als Argument nimmt und einen Slug zurückgibt. Die Funktion sollte die folgenden Operationen ausführen:

1. Konvertieren Sie den String in Kleinbuchstaben und entfernen Sie alle führenden oder nachfolgenden Leerzeichen.
2. Ersetzen Sie alle Sonderzeichen (d.h. jedes Zeichen, das kein Buchstabe, Ziffer, Leerzeichen, Bindestrich oder Unterstrich ist) durch eine leere Zeichenfolge.
3. Ersetzen Sie alle Leerzeichen, Bindestriche und Unterstriche durch einen einzelnen Bindestrich.
4. Entfernen Sie alle führenden oder nachfolgenden Bindestriche.

```python
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s
```

```python
slugify('Hello World!') # 'hello-world'
```
