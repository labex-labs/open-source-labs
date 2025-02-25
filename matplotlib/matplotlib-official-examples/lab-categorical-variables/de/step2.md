# Daten vorbereiten

Als nächstes werden wir einige Beispiel-Daten für das Plotten vorbereiten. Wir werden ein Dictionary mit den Zählungen verschiedener Früchte erstellen und dann die Schlüssel und Werte in separate Listen extrahieren.

```python
data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())
```
