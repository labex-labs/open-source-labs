# Création de formateurs supplémentaires

En programmation, l'héritage est un concept puissant qui nous permet de créer de nouvelles classes à partir de classes existantes. Cela facilite la réutilisation du code et rend nos programmes plus extensibles. Dans cette partie de l'expérience, nous allons utiliser l'héritage pour créer deux nouveaux formateurs pour différents formats de sortie : CSV et HTML. Ces formateurs hériteront d'une classe de base, ce qui signifie qu'ils partageront certains comportements communs tout en ayant leurs propres manières uniques de formater les données.

Maintenant, ajoutons les classes suivantes à votre fichier `tableformat.py`. Ces classes définiront comment formater les données respectivement au format CSV et HTML.

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

La classe `CSVTableFormatter` est conçue pour formater les données au format CSV (Comma-Separated Values, valeurs séparées par des virgules). La méthode `headings` prend une liste d'en - têtes et les affiche séparées par des virgules. La méthode `row` prend une liste de données pour une seule ligne et les affiche également séparées par des virgules.

La classe `HTMLTableFormatter`, en revanche, est utilisée pour générer du code de tableau HTML. La méthode `headings` crée les en - têtes de tableau en utilisant les balises HTML `<th>`, et la méthode `row` crée une ligne de tableau en utilisant les balises HTML `<td>`.

Testons ces nouveaux formateurs pour voir comment ils fonctionnent.

1. Tout d'abord, testons le formateur CSV :

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Dans ce code, nous importons d'abord les modules nécessaires. Ensuite, nous lisons les données à partir d'un fichier CSV nommé `portfolio.csv` et créons des instances de la classe `Stock`. Ensuite, nous créons une instance de la classe `CSVTableFormatter`. Enfin, nous utilisons la fonction `print_table` pour afficher les données du portefeuille au format CSV.

Vous devriez voir la sortie au format CSV suivante :

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. Maintenant, testons le formateur HTML :

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

Ici, nous créons une instance de la classe `HTMLTableFormatter` et utilisons à nouveau la fonction `print_table` pour afficher les données du portefeuille au format HTML.

Vous devriez voir la sortie au format HTML suivante :

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

Comme vous pouvez le voir, chaque formateur produit une sortie dans un format différent, mais ils partagent tous la même interface définie par la classe de base `TableFormatter`. Ceci est un excellent exemple de la puissance de l'héritage et du polymorphisme. Nous pouvons écrire du code qui fonctionne avec la classe de base, et il fonctionnera automatiquement avec n'importe quelle sous - classe.

La fonction `print_table()` n'a pas besoin de savoir quoi que ce soit sur le formateur spécifique utilisé. Elle appelle simplement les méthodes définies dans la classe de base, et l'implémentation appropriée est sélectionnée en fonction du type de formateur fourni. Cela rend notre code plus flexible et plus facile à maintenir.
