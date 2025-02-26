# Portée des classes

Les classes ne définissent pas une portée de noms.

```python
class Player:
 ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NON. Appelle une fonction `move` globale
        self.move(-amt, 0)  # OUI. Appelle la méthode `move` ci-dessus.
```

Si vous voulez opérer sur une instance, vous la référencez toujours explicitement (par exemple, `self`).

À partir de cet ensemble d'exercices, nous commençons à apporter une série de modifications au code existant des sections précédentes. Il est crucial d'avoir une version fonctionnelle de l'Exercice 3.18 pour commencer. Si vous n'en avez pas, veuillez travailler à partir du code de solution trouvé dans le répertoire `Solutions/3_18`. Il est possible de le copier.
