# Verwendung von Vererbung

Vererbung wird manchmal verwendet, um verwandte Objekte zu organisieren.

```python
class Shape:
 ...

class Circle(Shape):
 ...

class Rectangle(Shape):
 ...
```

Denke an eine logische Hierarchie oder Taxonomie. Ein häufiger (und praktischer) Einsatz ist jedoch in Bezug auf wiederverwendbaren oder erweiterbaren Code. Beispielsweise kann ein Framework eine Basisklasse definieren und Sie auffordern, sie anzupassen.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
     ...
        # Anpassende Verarbeitung
```

Die Basisklasse enthält einige allgemeingültigen Code. Ihre Klasse erbt und passt spezifische Teile an.
