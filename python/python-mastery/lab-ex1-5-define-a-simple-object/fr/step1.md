# Comprendre les classes Python

En Python, une classe sert de modèle pour créer des objets. La programmation orientée objet est une approche puissante qui nous permet d'organiser efficacement notre code. Elle le fait en regroupant des données et des fonctions liées ensemble. De cette manière, nous pouvons gérer plus facilement des programmes complexes et rendre notre code plus modulaire et maintenable.

Une classe Python est composée de deux composants principaux :

- **Attributs** : Ce sont des variables qui stockent des données au sein d'une classe. Considérez les attributs comme les caractéristiques ou les propriétés d'un objet. Par exemple, si nous créons une classe pour représenter une personne, les attributs pourraient être le nom, l'âge et la taille de la personne.
- **Méthodes** : Ce sont des fonctions qui appartiennent à une classe et qui peuvent accéder ou modifier ses attributs. Les méthodes définissent les actions que peut effectuer un objet. En utilisant l'exemple de la classe personne, une méthode pourrait être une fonction qui calcule l'âge de la personne en mois.

Les classes sont extrêmement utiles car elles offrent un moyen de créer du code réutilisable et de modéliser des concepts du monde réel. Dans ce laboratoire, nous allons créer une classe `Stock`. Cette classe sera utilisée pour représenter des informations sur les actions (stocks) telles que le nom de l'action, le nombre de parts et le prix par part.

Voici la structure de base d'une classe Python :

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method_name(self):
        # Code that uses the attributes
        return result
```

La méthode `__init__` est une méthode spéciale dans les classes Python. Elle est appelée automatiquement lorsque nous créons un nouvel objet à partir de la classe. Cette méthode est utilisée pour initialiser les attributs de l'objet. Le paramètre `self` est une référence à l'instance de la classe. Il est utilisé pour accéder aux attributs et aux méthodes depuis l'intérieur de la classe. Lorsque nous appelons une méthode sur un objet, Python passe automatiquement l'objet lui-même comme premier argument, c'est pourquoi nous utilisons `self` dans les définitions de méthode. Cela nous permet de travailler avec les attributs de l'instance spécifique et d'effectuer des opérations sur eux.
