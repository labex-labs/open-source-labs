# Daten vorbereiten

Als nächstes werden wir die Daten für unser Diagramm vorbereiten. Wir haben drei Pinguinarten und drei Attribute, daher werden wir ein Dictionary erstellen, das die Mittelwerte für jedes Attribut nach Art enthält.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
