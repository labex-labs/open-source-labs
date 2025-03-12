# Création d'une fonction usine

Lors de l'utilisation de l'héritage, un défi commun est que les utilisateurs doivent se souvenir des noms des classes de formateurs spécifiques. Cela peut être assez ennuyeux, surtout à mesure que le nombre de classes augmente. Pour simplifier ce processus, nous pouvons créer une fonction usine. Une fonction usine est un type spécial de fonction qui crée et retourne des objets. Dans notre cas, elle retournera le formateur approprié en fonction d'un nom de format simple.

Ajoutons la fonction suivante à votre fichier `tableformat.py`. Cette fonction prendra un nom de format en argument et retournera l'objet formateur correspondant.

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

La fonction `create_formatter()` est une fonction usine. Elle vérifie l'argument `format_name` que vous fournissez. Si c'est 'text', elle crée et retourne un objet `TextTableFormatter`. Si c'est 'csv', elle retourne un objet `CSVTableFormatter`, et si c'est 'html', elle retourne un objet `HTMLTableFormatter`. Si le nom de format n'est pas reconnu, elle lève une erreur `ValueError`. De cette façon, les utilisateurs peuvent facilement sélectionner un formateur en fournissant simplement un nom, sans avoir à connaître les noms de classes spécifiques.

Maintenant, testons la fonction usine. Nous allons utiliser certaines fonctions et classes existantes pour lire des données à partir d'un fichier CSV et les afficher dans différents formats.

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Dans ce code, nous importons d'abord les modules et les fonctions nécessaires. Ensuite, nous lisons les données à partir du fichier `portfolio.csv` et créons un objet `portfolio`. Après cela, nous testons la fonction `create_formatter()` avec différents noms de format : 'text', 'csv' et 'html'. Pour chaque format, nous créons un objet formateur, affichons le nom du format, puis utilisons la fonction `print_table()` pour afficher les données du `portfolio` dans le format spécifié.

Lorsque vous exécutez ce code, vous devriez voir des sorties dans les trois formats, séparées par le nom du format :

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

La fonction usine rend le code plus convivial car elle cache les détails de l'instanciation des classes. Les utilisateurs n'ont pas besoin de savoir comment créer des objets formateurs ; ils ont juste besoin de spécifier le format qu'ils souhaitent.

Ce modèle d'utilisation d'une fonction usine pour créer des objets est un modèle de conception commun en programmation orientée objet, connu sous le nom de modèle usine (Factory Pattern). Il fournit une couche d'abstraction entre le code client (le code qui utilise le formateur) et les classes d'implémentation réelles (les classes de formateurs). Cela rend le code plus modulaire et plus facile à utiliser.

**Récapitulatif des concepts clés :**

1. **Classe abstraite de base** : La classe `TableFormatter` sert d'interface. Une interface définit un ensemble de méthodes que toutes les classes qui l'implémentent doivent avoir. Dans notre cas, toutes les classes de formateurs doivent implémenter les méthodes définies dans la classe `TableFormatter`.

2. **Héritage** : Les classes de formateurs concrètes, comme `TextTableFormatter`, `CSVTableFormatter` et `HTMLTableFormatter`, héritent de la classe de base `TableFormatter`. Cela signifie qu'elles obtiennent la structure et les méthodes de base de la classe de base et peuvent fournir leurs propres implémentations spécifiques.

3. **Polymorphisme** : La fonction `print_table()` peut fonctionner avec n'importe quel formateur qui implémente l'interface requise. Cela signifie que vous pouvez passer différents objets formateurs à la fonction `print_table()`, et elle fonctionnera correctement avec chacun d'eux.

4. **Modèle usine** : La fonction `create_formatter()` simplifie la création d'objets formateurs. Elle prend en charge les détails de la création du bon objet en fonction du nom de format, de sorte que les utilisateurs n'ont pas à s'en soucier.

En utilisant ces principes de programmation orientée objet, nous avons créé un système flexible et extensible pour formater des données tabulaires dans différents formats de sortie.
