# Créer votre première métaclasse

Maintenant, nous allons créer notre toute première métaclasse. Avant de commencer à coder, comprenons ce qu'est une métaclasse. En Python, une métaclasse est une classe qui crée d'autres classes. C'est comme un modèle pour les classes. Lorsque vous définissez une classe en Python, Python utilise une métaclasse pour créer cette classe. Par défaut, Python utilise la métaclasse `type`. Dans cette étape, nous allons définir une métaclasse personnalisée qui affiche des informations sur la classe qu'elle crée. Cela nous aidera à comprendre le fonctionnement interne des métaclasses.

1. Ouvrez VSCode dans le WebIDE et créez un nouveau fichier appelé `mymeta.py` dans le répertoire `/home/labex/project`. C'est là que nous allons écrire notre code pour la métaclasse.

2. Ajoutez le code suivant au fichier :

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Analysons ce que ce code fait :

- Tout d'abord, nous définissons une nouvelle classe nommée `mytype` qui hérite de `type`. Étant donné que `type` est la métaclasse par défaut en Python, en héritant d'elle, nous créons notre propre métaclasse personnalisée.
- Ensuite, nous redéfinissons la méthode `__new__`. En Python, la méthode `__new__` est une méthode spéciale qui est appelée lors de la création d'un nouvel objet. Dans le contexte d'une métaclasse, elle est appelée lors de la création d'une nouvelle classe.
- À l'intérieur de notre méthode `__new__`, nous affichons quelques informations sur la classe en cours de création. Nous affichons le nom de la classe, ses classes de base et ses attributs. Après cela, nous appelons la méthode `__new__` du parent en utilisant `super().__new__(meta, name, bases, __dict__)`. Cela est important car c'est cela qui crée effectivement la classe.
- Enfin, nous créons une classe de base nommée `myobject` et spécifions qu'elle doit utiliser notre métaclasse personnalisée `mytype`.

La méthode `__new__` prend les paramètres suivants :

- `meta` : Cela fait référence à la métaclasse elle - même. Dans notre cas, c'est `mytype`.
- `name` : C'est le nom de la classe en cours de création.
- `bases` : C'est un tuple contenant les classes de base dont la nouvelle classe hérite.
- `__dict__` : C'est un dictionnaire qui contient les attributs de la classe.

3. Enregistrez le fichier en appuyant sur Ctrl+S ou en cliquant sur Fichier > Enregistrer. Enregistrer le fichier garantit que votre code est conservé et peut être exécuté plus tard.
