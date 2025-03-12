# Comprendre le problème

Avant de commencer à explorer les métaclasses, il est important de comprendre le problème que nous visons à résoudre. En programmation, nous avons souvent besoin de créer des structures avec des types spécifiques pour leurs attributs. Dans nos travaux précédents, nous avons développé un système pour les structures avec vérification de type. Ce système nous permet de définir des classes où chaque attribut a un type spécifique, et les valeurs assignées à ces attributs sont validées en fonction de ce type.

Voici un exemple de la façon dont nous avons utilisé ce système pour créer une classe `Stock` :

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Dans ce code, nous importons d'abord les types de validateurs (`String`, `PositiveInteger`, `PositiveFloat`) depuis le module `validate` et la classe `Structure` depuis le module `structure`. Ensuite, nous définissons la classe `Stock`, qui hérite de `Structure`. À l'intérieur de la classe `Stock`, nous définissons des attributs avec des types de validateurs spécifiques. Par exemple, l'attribut `name` doit être une chaîne de caractères, `shares` doit être un entier positif et `price` doit être un nombre à virgule flottante positif.

Cependant, il y a un problème avec cette approche. Nous devons importer tous les types de validateurs en haut de notre fichier. Au fur et à mesure que nous ajoutons de plus en plus de types de validateurs dans un scénario du monde réel, ces importations peuvent devenir très longues et difficiles à gérer. Cela pourrait nous amener à utiliser `from validate import *`, ce qui est généralement considéré comme une mauvaise pratique car cela peut causer des conflits de noms et rendre le code moins lisible.

Pour comprendre notre point de départ, regardons la classe `Structure`. Vous devez ouvrir le fichier `structure.py` dans l'éditeur et examiner son contenu. Cela vous aidera à voir comment la gestion de la structure de base est implémentée avant d'ajouter la fonctionnalité de métaclasse.

```bash
code structure.py
```

Lorsque vous ouvrez le fichier, vous verrez une implémentation de base de la classe `Structure`. Cette classe est responsable de la gestion de l'initialisation des attributs, mais elle n'a pas encore de fonctionnalité de métaclasse.

Ensuite, examinons les classes de validateurs. Ces classes sont définies dans le fichier `validate.py`. Elles ont déjà une fonctionnalité de descripteur, ce qui signifie qu'elles peuvent contrôler la façon dont les attributs sont accédés et définis. Mais nous devrons les améliorer pour résoudre le problème d'importation que nous avons discuté précédemment.

```bash
code validate.py
```

En regardant ces classes de validateurs, vous comprendrez mieux comment le processus de validation fonctionne et quelles modifications nous devons apporter pour améliorer notre code.
