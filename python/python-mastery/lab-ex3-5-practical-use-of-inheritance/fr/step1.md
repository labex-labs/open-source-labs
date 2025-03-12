# Comprendre le problème

Dans ce laboratoire, nous allons apprendre l'héritage en Python et comment il peut nous aider à créer un code extensible et adaptable. L'héritage est un concept puissant en programmation orientée objet où une classe peut hériter d'attributs et de méthodes d'une autre classe. Cela nous permet de réutiliser le code et de construire des fonctionnalités plus complexes sur la base du code existant.

Commençons par examiner la fonction existante `print_table()`. C'est cette fonction que nous allons améliorer pour la rendre plus flexible en termes de formats de sortie.

Tout d'abord, vous devez ouvrir le fichier `tableformat.py` dans l'éditeur WebIDE. Le chemin de ce fichier est le suivant :

```
/home/labex/project/tableformat.py
```

Une fois que vous avez ouvert le fichier, vous verrez l'implémentation actuelle de la fonction `print_table()`. Cette fonction est conçue pour formater et afficher des données tabulaires. Elle prend deux entrées principales : une liste d'enregistrements (qui sont des objets) et une liste de noms de champs. Sur la base de ces entrées, elle affiche un tableau bien formaté.

Maintenant, testons cette fonction pour voir comment elle fonctionne. Ouvrez un terminal dans le WebIDE et exécutez les commandes Python suivantes. Ces commandes importent les modules nécessaires, lisent les données à partir d'un fichier CSV, puis utilisent la fonction `print_table()` pour afficher les données.

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

Après avoir exécuté ces commandes, vous devriez voir la sortie suivante :

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

La sortie est correcte, mais cette fonction présente une limitation. Actuellement, elle ne prend en charge qu'un seul format de sortie, qui est le texte brut. Dans des scénarios réels, vous pourriez vouloir afficher vos données dans différents formats tels que CSV, HTML ou d'autres.

Au lieu de modifier la fonction `print_table()` chaque fois que nous voulons prendre en charge un nouveau format de sortie, nous pouvons utiliser l'héritage pour créer une solution plus flexible. Voici comment nous allons procéder :

1. Nous allons définir une classe de base `TableFormatter`. Cette classe aura des méthodes utilisées pour formater les données. La classe de base fournit une structure et une fonctionnalité communes sur lesquelles toutes les sous - classes peuvent s'appuyer.
2. Nous allons créer diverses sous - classes. Chaque sous - classe sera conçue pour un format de sortie différent. Par exemple, une sous - classe pourrait être pour la sortie au format CSV, une autre pour la sortie au format HTML, etc. Ces sous - classes hériteront des méthodes de la classe de base et peuvent également ajouter leur propre fonctionnalité spécifique.
3. Nous allons modifier la fonction `print_table()` pour qu'elle puisse fonctionner avec n'importe quel formateur. Cela signifie que nous pouvons passer différentes sous - classes de la classe `TableFormatter` à la fonction `print_table()`, et elle sera capable d'utiliser les méthodes de formatage appropriées.

Cette approche présente un grand avantage. Elle nous permet d'ajouter de nouveaux formats de sortie sans modifier la fonctionnalité principale de la fonction `print_table()`. Ainsi, lorsque vos besoins changent et que vous avez besoin de prendre en charge plus de formats de sortie, vous pouvez facilement le faire en créant de nouvelles sous - classes.
