# Extrahieren von spezifischen Passagierdaten

Als nächstes extrahieren wir die Passagierdaten der Grafinnen an Bord der Titanic. Wir verwenden die Methode `str.contains()`, um Zeilen zu finden, in denen die Spalte `Name` das Wort 'Countess' enthält.

```python
# Find rows where 'Name' contains 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
