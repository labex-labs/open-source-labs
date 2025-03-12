# Création de descripteurs personnalisés

Dans cette étape, nous allons créer notre propre classe de descripteur. Mais d'abord, comprenons ce qu'est un descripteur. Un descripteur est un objet Python qui implémente le protocole des descripteurs, qui se compose des méthodes `__get__`, `__set__` et `__delete__`. Ces méthodes permettent au descripteur de gérer la manière dont un attribut est accédé, défini et supprimé. En créant notre propre classe de descripteur, nous pouvons mieux comprendre le fonctionnement de ce protocole.

Créez un nouveau fichier appelé `descrip.py` dans le répertoire du projet. Ce fichier contiendra notre classe de descripteur personnalisé. Voici le code :

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

Dans la classe `Descriptor`, la méthode `__init__` initialise le descripteur avec un nom. La méthode `__get__` est appelée lorsque l'attribut est accédé, la méthode `__set__` est appelée lorsque l'attribut est défini, et la méthode `__delete__` est appelée lorsque l'attribut est supprimé.

Maintenant, créons un fichier de test pour expérimenter avec notre descripteur personnalisé. Cela nous aidera à voir le comportement du descripteur dans différents scénarios. Créez un fichier nommé `test_descrip.py` avec le code suivant :

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

Dans le fichier `test_descrip.py`, nous importons la classe `Descriptor` depuis `descrip.py`. Ensuite, nous créons une classe `Foo` avec trois attributs `a`, `b` et `c`, chacun géré par un descripteur. Nous créons une instance de `Foo` et effectuons des opérations telles que l'accès, la définition et la suppression d'attributs pour voir comment les méthodes du descripteur sont appelées.

Maintenant, exécutons ce fichier de test pour voir les descripteurs en action. Ouvrez votre terminal, accédez au répertoire du projet et exécutez le fichier de test en utilisant les commandes suivantes :

```bash
cd ~/project
python3 test_descrip.py
```

Vous devriez voir une sortie comme celle-ci :

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

Comme vous pouvez le voir, chaque fois que vous accédez, définissez ou supprimez un attribut géré par un descripteur, la méthode magique correspondante (`__get__`, `__set__` ou `__delete__`) est appelée.

Examinons également notre descripteur de manière interactive. Cela nous permettra de tester le descripteur en temps réel et de voir immédiatement les résultats. Ouvrez votre terminal, accédez au répertoire du projet et démarrez une session Python interactive avec le fichier `descrip.py` :

```bash
cd ~/project
python3 -i descrip.py
```

Maintenant, tapez ces commandes dans la session Python interactive pour voir comment le protocole des descripteurs fonctionne :

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

L'idée clé ici est que les descripteurs offrent un moyen d'intercepter et de personnaliser l'accès aux attributs. Cela les rend puissants pour implémenter la validation des données, les attributs calculés et d'autres comportements avancés. En utilisant des descripteurs, vous pouvez avoir plus de contrôle sur la manière dont les attributs de votre classe sont accédés, définis et supprimés.
