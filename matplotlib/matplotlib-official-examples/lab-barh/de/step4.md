# Vorbereiten der Daten

In diesem Schritt werden die Daten für das Diagramm vorbereitet. Wir werden eine Liste mit Namen von Personen, ihrer Leistung und der Fehlerrate erstellen.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
