# Allocation de mémoire des dictionnaires

En Python, tout comme les listes, les dictionnaires sont une structure de données fondamentale. Un aspect important à comprendre à leur sujet est la manière dont ils allouent de la mémoire. L'allocation de mémoire fait référence à la façon dont Python réserve de l'espace dans la mémoire de l'ordinateur pour stocker les données de votre dictionnaire. À l'instar des listes, les dictionnaires Python allouent également de la mémoire par blocs. Explorons comment fonctionne l'allocation de mémoire pour les dictionnaires.

1. Tout d'abord, nous devons créer un dictionnaire avec lequel travailler. Dans le même shell Python (ou ouvrez-en un nouveau si vous l'avez fermé), nous allons créer un dictionnaire représentant un enregistrement de données. Un dictionnaire en Python est une collection de paires clé - valeur, où chaque clé est unique et est utilisée pour accéder à sa valeur correspondante.

```python
import sys  # Importez sys si vous commencez une nouvelle session
row = {'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Ici, nous avons importé le module `sys` qui donne accès à certaines variables utilisées ou maintenues par l'interpréteur Python et à des fonctions qui interagissent fortement avec l'interpréteur. Nous avons ensuite créé un dictionnaire nommé `row` avec quatre paires clé - valeur.

2. Maintenant que nous avons notre dictionnaire, nous voulons vérifier sa taille initiale. La taille d'un dictionnaire fait référence à la quantité de mémoire qu'il occupe dans l'ordinateur.

```python
sys.getsizeof(row)
```

La fonction `sys.getsizeof()` renvoie la taille d'un objet en octets. Lorsque vous exécutez ce code, vous devriez voir une valeur d'environ `240` octets. Cela vous donne une idée de la quantité de mémoire que le dictionnaire occupe initialement.

3. Ensuite, nous allons ajouter de nouvelles paires clé - valeur au dictionnaire et observer comment l'allocation de mémoire change. Ajouter des éléments à un dictionnaire est une opération courante, et il est crucial de comprendre comment cela affecte la mémoire.

```python
row['a'] = 1
sys.getsizeof(row)  # La taille peut rester la même

row['b'] = 2
sys.getsizeof(row)  # La taille peut augmenter
```

Lorsque vous ajoutez la première paire clé - valeur (`'a': 1`), la taille du dictionnaire peut rester la même. C'est parce que Python a déjà alloué un certain bloc de mémoire, et il peut y avoir assez d'espace dans ce bloc pour accueillir le nouvel élément. Cependant, lorsque vous ajoutez la deuxième paire clé - valeur (`'b': 2`), la taille peut augmenter. Vous remarquerez qu'après avoir ajouté un certain nombre d'éléments, la taille du dictionnaire augmente soudainement. C'est parce que les dictionnaires, comme les listes, allouent de la mémoire par blocs pour optimiser les performances. Allouer de la mémoire par blocs réduit le nombre de fois où Python doit demander plus de mémoire au système, ce qui accélère le processus d'ajout de nouveaux éléments.

4. Essayons de supprimer un élément du dictionnaire pour voir si l'utilisation de la mémoire diminue. Supprimer des éléments d'un dictionnaire est également une opération courante, et il est intéressant de voir comment cela affecte la mémoire.

```python
del row['b']
sys.getsizeof(row)
```

Fait intéressant, supprimer un élément ne réduit généralement pas l'allocation de mémoire. C'est parce que Python conserve la mémoire allouée pour éviter de réallouer si des éléments sont ajoutés à nouveau. Réallouer de la mémoire est une opération relativement coûteuse en termes de performances, donc Python essaie de l'éviter autant que possible.

**Considérations sur l'efficacité mémoire :**

Lorsque vous travaillez avec de grands ensembles de données où vous devez créer de nombreux enregistrements, utiliser des dictionnaires pour chaque enregistrement peut ne pas être la méthode la plus efficace en termes de mémoire. Les dictionnaires sont très flexibles et faciles à utiliser, mais ils peuvent consommer une quantité importante de mémoire, notamment lorsqu'il s'agit d'un grand nombre d'enregistrements. Voici quelques alternatives qui consomment moins de mémoire :

- Tuples : Séquences immuables simples. Un tuple est une collection de valeurs qui ne peut pas être modifiée après sa création. Il utilise moins de mémoire qu'un dictionnaire car il n'a pas besoin de stocker les clés et de gérer la correspondance clé - valeur associée.
- Tuples nommés : Tuples avec des noms de champs. Les tuples nommés sont similaires aux tuples ordinaires, mais ils vous permettent d'accéder aux valeurs par nom, ce qui peut rendre le code plus lisible. Ils utilisent également moins de mémoire que les dictionnaires.
- Classes avec `__slots__` : Classes qui définissent explicitement les attributs pour éviter d'utiliser un dictionnaire pour les variables d'instance. Lorsque vous utilisez `__slots__` dans une classe, Python ne crée pas de dictionnaire pour stocker les variables d'instance, ce qui réduit l'utilisation de la mémoire.

Ces alternatives peuvent réduire considérablement l'utilisation de la mémoire lors de la manipulation de nombreux enregistrements.
