# Verwendung von regulären Ausdrücken (Regular Expressions) für die Mustererkennung

Um Zeichenketten (Strings) in Snake Case umzuwandeln, verwenden wir reguläre Ausdrücke (regex), um Wortgrenzen zu identifizieren. Das `re`-Modul in Python bietet leistungsstarke Mustererkennungsfunktionen, die wir für diese Aufgabe nutzen können.

Lassen Sie uns unsere Funktion aktualisieren, um camelCase-Zeichenketten zu verarbeiten:

1. Zunächst müssen wir das Muster identifizieren, bei dem ein Kleinbuchstabe von einem Großbuchstaben gefolgt wird (wie in "camelCase").
2. Dann fügen wir einen Leerzeichen zwischen ihnen ein.
3. Schließlich wandeln wir alles in Kleinbuchstaben um und ersetzen die Leerzeichen durch Unterstriche.

Aktualisieren Sie Ihre `snake_case.py`-Datei mit dieser verbesserten Funktion:

```python
import re

def snake(s):
    # Replace pattern of a lowercase letter followed by uppercase with lowercase, space, uppercase
    s1 = re.sub('([a-z])([A-Z])', r'\1 \2', s)

    # Replace spaces with underscores and convert to lowercase
    return s1.lower().replace(' ', '_')

# Test with a simple example
if __name__ == "__main__":
    test_string = "helloWorld"
    result = snake(test_string)
    print(f"Original: {test_string}")
    print(f"Snake case: {result}")
```

Lassen Sie uns analysieren, was diese Funktion tut:

- `re.sub('([a-z])([A-Z])', r'\1 \2', s)` sucht nach Mustern, bei denen ein Kleinbuchstabe `([a-z])` von einem Großbuchstaben `([A-Z])` gefolgt wird. Es ersetzt dann dieses Muster durch dieselben Buchstaben, fügt aber mithilfe von `\1` und `\2`, die auf die erfassten Gruppen verweisen, einen Leerzeichen zwischen sie ein.
- Dann wandeln wir alles mit `lower()` in Kleinbuchstaben um und ersetzen die Leerzeichen durch Unterstriche.

Führen Sie Ihr Skript erneut aus, um zu sehen, ob es für camelCase funktioniert:

```bash
python3 ~/project/snake_case.py
```

Die Ausgabe sollte jetzt wie folgt aussehen:

```
Original: helloWorld
Snake case: hello_world
```

Toll! Unsere Funktion kann jetzt camelCase-Zeichenketten verarbeiten. Im nächsten Schritt werden wir sie erweitern, um komplexere Fälle zu behandeln.
