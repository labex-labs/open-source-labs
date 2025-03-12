# La délégation comme alternative à l'héritage

En programmation orientée objet, la réutilisation et l'extension de code sont des tâches courantes. Il existe deux principales façons d'y parvenir : l'héritage et la délégation.

**L'héritage** est un mécanisme par lequel une sous - classe hérite des méthodes et des attributs d'une classe mère. La sous - classe peut choisir de remplacer certaines de ces méthodes héritées pour fournir sa propre implémentation.

**La délégation**, en revanche, consiste à ce qu'un objet contienne un autre objet et transmette des appels de méthode spécifiques à celui - ci.

Dans cette étape, nous allons explorer la délégation comme alternative à l'héritage. Nous allons implémenter une classe qui délègue une partie de son comportement à un autre objet.

## Configuration d'un exemple de délégation

Tout d'abord, nous devons configurer la classe de base avec laquelle notre classe délégatrice va interagir.

1. Créez un nouveau fichier appelé `base_class.py` dans le répertoire `/home/labex/project`. Ce fichier définira une classe nommée `Spam` avec trois méthodes : `method_a`, `method_b` et `method_c`. Chaque méthode affiche un message et retourne un résultat. Voici le code à placer dans `base_class.py` :

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

Ensuite, nous allons créer la classe délégatrice.

2. Créez un nouveau fichier appelé `delegator.py`. Dans ce fichier, nous allons définir une classe nommée `DelegatingSpam` qui délègue une partie de son comportement à une instance de la classe `Spam`.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

Dans la méthode `__init__`, nous créons une instance de la classe `Spam`. La méthode `method_a` remplace la méthode d'origine mais appelle également la méthode `method_a` de la classe `Spam`. La méthode `method_c` remplace complètement la méthode d'origine. La méthode `__getattr__` est une méthode spéciale en Python qui est appelée lorsqu'un attribut ou une méthode qui n'existe pas dans la classe `DelegatingSpam` est accédé. Elle transmet alors l'appel à l'instance de `Spam`.

Maintenant, créons un fichier de test pour vérifier notre implémentation.

3. Créez un fichier de test nommé `test_delegation.py`. Ce fichier créera une instance de la classe `DelegatingSpam` et appellera ses méthodes.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Enfin, nous allons exécuter le script de test.

4. Exécutez le script de test en utilisant les commandes suivantes dans le terminal :

```bash
cd /home/labex/project
python3 test_delegation.py
```

Vous devriez voir une sortie similaire à ce qui suit :

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## Délégation vs. Héritage

Maintenant, comparons la délégation avec l'héritage traditionnel.

1. Créez un fichier appelé `inheritance_example.py`. Dans ce fichier, nous allons définir une classe nommée `InheritingSpam` qui hérite de la classe `Spam`.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

La classe `InheritingSpam` remplace les méthodes `method_a` et `method_c`. Dans la méthode `method_a`, nous utilisons `super()` pour appeler la méthode `method_a` de la classe mère.

Ensuite, nous allons créer un fichier de test pour l'exemple d'héritage.

2. Créez un fichier de test nommé `test_inheritance.py`. Ce fichier créera une instance de la classe `InheritingSpam` et appellera ses méthodes.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Enfin, nous allons exécuter le test d'héritage.

3. Exécutez le test d'héritage en utilisant les commandes suivantes dans le terminal :

```bash
cd /home/labex/project
python3 test_inheritance.py
```

Vous devriez voir une sortie similaire à ce qui suit :

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## Principales différences et considérations

Regardons les similitudes et les différences entre la délégation et l'héritage.

1. **Remplacement de méthode** : La délégation et l'héritage vous permettent de remplacer des méthodes, mais la syntaxe est différente.

   - En délégation, vous définissez votre propre méthode et décidez si vous appelez la méthode de l'objet enveloppé.
   - En héritage, vous définissez votre propre méthode et utilisez `super()` pour appeler la méthode de la classe mère.

2. **Accès aux méthodes** :

   - En délégation, les méthodes non définies sont transmises via la méthode `__getattr__`.
   - En héritage, les méthodes non définies sont héritées automatiquement.

3. **Relations de type** :

   - Avec la délégation, `isinstance(delegating_spam, Spam)` retourne `False` car l'objet `DelegatingSpam` n'est pas une instance de la classe `Spam`.
   - Avec l'héritage, `isinstance(inheriting_spam, Spam)` retourne `True` car la classe `InheritingSpam` hérite de la classe `Spam`.

4. **Limitations** : La délégation via `__getattr__` ne fonctionne pas avec les méthodes spéciales comme `__getitem__`, `__len__`, etc. Ces méthodes devraient être explicitement définies dans la classe délégatrice.

La délégation est particulièrement utile dans les situations suivantes :

- Vous souhaitez personnaliser le comportement d'un objet sans affecter sa hiérarchie.
- Vous souhaitez combiner des comportements de plusieurs objets qui n'ont pas de parent commun.
- Vous avez besoin de plus de flexibilité que ce que l'héritage offre.

L'héritage est généralement préféré lorsque :

- La relation "est - un" est claire (par exemple, une Voiture est un Véhicule).
- Vous devez maintenir la compatibilité de type dans votre code.
- Les méthodes spéciales doivent être héritées.
