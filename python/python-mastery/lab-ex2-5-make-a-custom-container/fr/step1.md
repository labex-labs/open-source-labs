# Comprendre l'allocation de mémoire des listes

En Python, les listes sont une structure de données très utile, notamment lorsque vous avez besoin d'ajouter des éléments. Les listes Python sont conçues pour être efficaces pour les opérations d'ajout. Au lieu d'allouer exactement la quantité de mémoire nécessaire, Python alloue de la mémoire supplémentaire en prévision d'ajouts futurs. Cette stratégie minimise le nombre de réallocations de mémoire nécessaires lorsque la liste grandit.

Comprenons mieux ce concept en utilisant la fonction `sys.getsizeof()`. Cette fonction renvoie la taille d'un objet en octets, ce qui nous permet de voir combien de mémoire une liste utilise à différents stades.

1. Tout d'abord, vous devez ouvrir un shell interactif Python dans votre terminal. C'est comme un terrain de jeu où vous pouvez exécuter immédiatement du code Python. Pour l'ouvrir, tapez la commande suivante dans votre terminal et appuyez sur Entrée :

```bash
python3
```

2. Une fois que vous êtes dans le shell interactif Python, vous devez importer le module `sys`. Les modules en Python sont comme des boîtes à outils qui contiennent des fonctions utiles. Le module `sys` possède la fonction `getsizeof()` dont nous avons besoin. Après avoir importé le module, créez une liste vide nommée `items`. Voici le code pour cela :

```python
import sys
items = []
```

3. Maintenant, vérifions la taille initiale de la liste vide. Nous allons utiliser la fonction `sys.getsizeof()` avec la liste `items` comme argument. Tapez le code suivant dans le shell interactif Python et appuyez sur Entrée :

```python
sys.getsizeof(items)
```

Vous devriez voir une valeur comme `64` octets. Cette valeur représente la surcharge pour une liste vide. La surcharge est la quantité de mémoire de base que Python utilise pour gérer la liste, même lorsqu'elle n'a aucun élément.

4. Ensuite, nous allons commencer à ajouter des éléments à la liste un par un et observer comment l'allocation de mémoire change. Nous allons utiliser la méthode `append()` pour ajouter un élément à la liste, puis vérifier à nouveau la taille. Voici le code :

```python
items.append(1)
sys.getsizeof(items)
```

Vous devriez voir une valeur plus grande, environ `96` octets. Cette augmentation de taille montre que Python a alloué plus de mémoire pour accueillir le nouvel élément.

5. Continuons d'ajouter plus d'éléments à la liste et vérifions la taille après chaque ajout. Voici le code pour cela :

```python
items.append(2)
sys.getsizeof(items)  # La taille reste la même

items.append(3)
sys.getsizeof(items)  # La taille reste inchangée

items.append(4)
sys.getsizeof(items)  # La taille reste inchangée

items.append(5)
sys.getsizeof(items)  # La taille saute à une valeur plus grande
```

Vous remarquerez que la taille n'augmente pas avec chaque opération d'ajout. Au lieu de cela, elle augmente périodiquement. Cela démontre que Python alloue de la mémoire par blocs plutôt que pour chaque nouvel élément individuellement.

Ce comportement est intentionnel. Python alloue plus de mémoire que nécessaire au départ pour éviter des réallocations fréquentes à mesure que la liste grandit. Chaque fois que la liste dépasse sa capacité actuelle, Python alloue un bloc de mémoire plus grand.

N'oubliez pas qu'une liste stocke des références aux objets, pas les objets eux - mêmes. Sur un système 64 bits, chaque référence nécessite généralement 8 octets de mémoire. Il est important de comprendre cela car cela affecte la quantité de mémoire qu'une liste utilise réellement lorsqu'elle contient différents types d'objets.
