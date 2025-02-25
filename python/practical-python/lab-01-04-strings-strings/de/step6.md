# String-Methoden

Strings haben Methoden, die verschiedene Operationen mit den String-Daten ausführen.

Beispiel: Entfernen von führenden / nachfolgenden Leerzeichen.

```python
s ='  Hello '
t = s.strip()     # 'Hello'
```

Beispiel: Groß-/Kleinschreibung umwandeln.

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Beispiel: Text ersetzen.

```python
s = 'Hello world'
t = s.replace('Hello', 'Hallo')   # 'Hallo world'
```

**Weitere String-Methoden:**

Strings haben eine Vielzahl von anderen Methoden zum Testen und Bearbeiten von Text-Daten. Dies ist ein kleiner Auszug von Methoden:

```python
s.endswith(suffix)     # Überprüfen, ob der String mit suffix endet
s.find(t)              # Erstes Vorkommen von t in s
s.index(t)             # Erstes Vorkommen von t in s
s.isalpha()            # Überprüfen, ob die Zeichen alphabetisch sind
s.isdigit()            # Überprüfen, ob die Zeichen numerisch sind
s.islower()            # Überprüfen, ob die Zeichen in Kleinbuchstaben sind
s.isupper()            # Überprüfen, ob die Zeichen in Großbuchstaben sind
s.join(slist)          # Verknüpfen einer Liste von Strings mit s als Trennzeichen
s.lower()              # In Kleinbuchstaben umwandeln
s.replace(old,new)     # Text ersetzen
s.rfind(t)             # Suchen nach t von Ende des Strings
s.rindex(t)            # Suchen nach t von Ende des Strings
s.split([delim])       # String in Liste von Teilstrings aufteilen
s.startswith(prefix)   # Überprüfen, ob der String mit prefix beginnt
s.strip()              # Führende/Nachfolgende Leerzeichen entfernen
s.upper()              # In Großbuchstaben umwandeln
```
