# Utilisation de l'héritage

L'héritage est parfois utilisé pour organiser des objets apparentés.

```python
class Shape:
 ...

class Circle(Shape):
 ...

class Rectangle(Shape):
 ...
```

Pensez à une hiérarchie logique ou une taxonomie. Cependant, une utilisation plus courante (et pratique) est liée à la création de code réutilisable ou extensible. Par exemple, un framework peut définir une classe de base et vous demander de la personnaliser.

```python
class CustomHandler(TCPHandler):
    def handle_request(self):
     ...
        # Traitement personnalisé
```

La classe de base contient du code à usage général. Votre classe hérite et personnalise des parties spécifiques.
