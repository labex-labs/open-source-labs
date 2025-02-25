# Konvertieren von Zeichen in Kleinbuchstaben

Als nächstes werden wir alle Zeichen in der Spalte `Name` in Kleinbuchstaben umwandeln. Wir verwenden die Methode `str.lower()`, um dies zu erreichen.

```python
# Convert all characters in the 'Name' column to lowercase
titanic["Name"] = titanic["Name"].str.lower()
```
