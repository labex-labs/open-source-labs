# Einführung

**Ziele:**

- Lernen Sie über delegierende Generatoren

**Veränderte Dateien:** `cofollow.py`, `server.py`

Ein potenzielles Problem in Code, der auf Generatoren basiert, ist das Problem, Details vor dem Benutzer zu verbergen und Bibliotheken zu schreiben. Um alles zu steuern, werden im Allgemeinen viele niedrigere Mechanismen benötigt, und es ist oft ziemlich unhandlich, es direkt den Benutzern zu präsentieren.

Ab Python 3.3 kann ein neuer `yield from`-Ausdruck verwendet werden, um Generatoren an eine andere Funktion zu delegieren. Es ist eine nützliche Möglichkeit, Code zu bereinigen, der auf Generatoren basiert.
