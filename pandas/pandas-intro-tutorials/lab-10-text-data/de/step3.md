# Extraktion von Nachnamen aus Vornamen und Nachnamen

Lassen Sie uns nun eine neue Spalte `Nachname` erstellen, die den Nachnamen der Passagiere enthält. Wir werden dies erreichen, indem wir den Teil vor dem Komma in der Spalte `Name` extrahieren.

```python
# Split the 'Name' column on comma and extract the first part
titanic["Nachname"] = titanic["Name"].str.split(",").str.get(0)
```
