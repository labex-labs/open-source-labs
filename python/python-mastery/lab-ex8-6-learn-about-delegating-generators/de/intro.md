# Einführung

In diesem Lab werden Sie lernen, wie man in Python Generatoren delegiert, indem man die Anweisung `yield from` verwendet. Diese Funktion, die in Python 3.3 eingeführt wurde, vereinfacht Code, der auf Generatoren und Koroutinen basiert.

Generatoren sind spezielle Funktionen, die die Ausführung anhalten und fortsetzen können und ihren Zustand zwischen den Aufrufen beibehalten. Die Anweisung `yield from` bietet eine elegante Möglichkeit, die Kontrolle an einen anderen Generator zu delegieren, was die Lesbarkeit und Wartbarkeit des Codes verbessert.

**Ziele:**

- Verstehen Sie den Zweck der Anweisung `yield from`
- Lernen Sie, wie man `yield from` verwendet, um an andere Generatoren zu delegieren
- Wenden Sie diese Kenntnisse an, um auf Koroutinen basierenden Code zu vereinfachen
- Verstehen Sie die Verbindung zur modernen async/await-Syntax

**Dateien, mit denen Sie arbeiten werden:**

- `cofollow.py` - Enthält Hilfsfunktionen für Koroutinen
- `server.py` - Enthält eine einfache Implementierung eines Netzwerkservers
