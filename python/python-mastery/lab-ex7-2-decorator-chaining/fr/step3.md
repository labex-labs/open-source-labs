# Application de décorateurs aux méthodes de classe

Maintenant, nous allons explorer comment les décorateurs interagissent avec les méthodes de classe. Cela peut être un peu délicat car Python a différents types de méthodes : les méthodes d'instance, les méthodes de classe, les méthodes statiques et les propriétés. Les décorateurs sont des fonctions qui prennent une autre fonction et étendent le comportement de cette dernière sans la modifier explicitement. Lorsque nous appliquons des décorateurs aux méthodes de classe, nous devons faire attention à la façon dont ils fonctionnent avec ces différents types de méthodes.

## Compréhension du défi

Voyons ce qui se passe lorsque nous appliquons notre décorateur `@logged` à différents types de méthodes. Le décorateur `@logged` est probablement utilisé pour enregistrer des informations sur les appels de méthode.

1. Créez un nouveau fichier `methods.py` dans le WebIDE. Ce fichier contiendra notre classe avec différents types de méthodes décorées avec le décorateur `@logged`.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

Dans ce code, nous avons une classe `Spam` avec quatre types différents de méthodes. Chaque méthode est décorée avec le décorateur `@logged`, et certaines sont également décorées avec d'autres décorateurs intégrés comme `@classmethod`, `@staticmethod` et `@property`.

2. Testons comment cela fonctionne. Nous allons exécuter une commande Python dans le terminal pour appeler ces méthodes et voir la sortie.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Lorsque vous exécutez cette commande, vous pourriez remarquer quelques problèmes :

- Le décorateur `@property` peut ne pas fonctionner correctement avec notre décorateur `@logged`. Le décorateur `@property` est utilisé pour définir une méthode comme une propriété, et il a un mode de fonctionnement spécifique. Lorsqu'il est combiné avec le décorateur `@logged`, il pourrait y avoir des conflits.
- L'ordre des décorateurs est important pour `@classmethod` et `@staticmethod`. L'ordre dans lequel les décorateurs sont appliqués peut changer le comportement de la méthode.

## L'ordre des décorateurs

Lorsque vous appliquez plusieurs décorateurs, ils sont appliqués de bas en haut. Cela signifie que le décorateur le plus proche de la définition de la méthode est appliqué en premier, puis ceux au - dessus sont appliqués séquentiellement. Par exemple :

```python
@decorator1
@decorator2
def func():
    pass
```

Cela équivaut à :

```python
func = decorator1(decorator2(func))
```

Dans cet exemple, `decorator2` est appliqué à `func` en premier, puis `decorator1` est appliqué au résultat de `decorator2(func)`.

## Correction de l'ordre des décorateurs

Mettons à jour notre fichier `methods.py` pour corriger l'ordre des décorateurs. En changeant l'ordre des décorateurs, nous pouvons nous assurer que chaque méthode fonctionne comme prévu.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

Dans cette version mise à jour :

- Pour `instance_method`, l'ordre n'a pas d'importance. Les méthodes d'instance sont appelées sur une instance de la classe, et le décorateur `@logged` peut être appliqué dans n'importe quel ordre sans affecter sa fonctionnalité de base.
- Pour `class_method`, nous appliquons `@classmethod` après `@logged`. Le décorateur `@classmethod` change la façon dont la méthode est appelée, et en l'appliquant après `@logged`, nous nous assurons que la journalisation fonctionne correctement.
- Pour `static_method`, nous appliquons `@staticmethod` après `@logged`. De même que pour `@classmethod`, le décorateur `@staticmethod` a son propre comportement, et l'ordre avec le décorateur `@logged` doit être correct.
- Pour `property_method`, nous appliquons `@property` après `@logged`. Cela garantit que le comportement de la propriété est maintenu tout en obtenant la fonctionnalité de journalisation.

3. Testons le code mis à jour. Nous allons exécuter la même commande que précédemment pour voir si les problèmes sont résolus.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Vous devriez maintenant voir une journalisation correcte pour tous les types de méthodes :

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## Bonnes pratiques pour les décorateurs de méthode

Lorsque vous travaillez avec des décorateurs de méthode, suivez ces bonnes pratiques :

1. Appliquez les décorateurs de transformation de méthode (`@classmethod`, `@staticmethod`, `@property`) **après** vos décorateurs personnalisés. Cela garantit que les décorateurs personnalisés peuvent effectuer leur journalisation ou d'autres opérations en premier, puis les décorateurs intégrés peuvent transformer la méthode comme prévu.
2. Sachez que l'exécution du décorateur se produit au moment de la définition de la classe, pas au moment de l'appel de la méthode. Cela signifie que tout code de configuration ou d'initialisation dans le décorateur sera exécuté lorsque la classe est définie, pas lorsque la méthode est appelée.
3. Pour les cas plus complexes, vous devrez peut - être créer des décorateurs spécialisés pour différents types de méthodes. Les différents types de méthodes ont des comportements différents, et un décorateur universel peut ne pas fonctionner dans toutes les situations.
