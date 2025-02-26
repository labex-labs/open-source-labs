# Exercice 4.5 : Un problème d'extension

Supposons que vous vouliez modifier la fonction `print_report()` pour prendre en charge diverses formats de sortie différents, tels que le texte brut, le HTML, le CSV ou le XML. Pour ce faire, vous pourriez essayer d'écrire une fonction énorme qui ferait tout. Cependant, cela entraînerait probablement un bordel impraticable à maintenir. Au lieu de cela, c'est une excellente occasion d'utiliser l'héritage à la place.

Pour commencer, concentrez-vous sur les étapes impliquées dans la création d'un tableau. En haut du tableau se trouve un ensemble d'en-têtes de tableau. Après cela, apparaissent les lignes de données du tableau. Prenons ces étapes et mettons-les dans leur propre classe. Créez un fichier appelé `tableformat.py` et définissez la classe suivante :

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Émet les en-têtes de tableau.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Émet une seule ligne de données de tableau.
        '''
        raise NotImplementedError()
```

Cette classe ne fait rien, mais elle sert comme une sorte de spécification de conception pour les classes supplémentaires qui seront définies bientôt. Une classe comme celle-ci est parfois appelée une "classe de base abstraite".

Modifiez la fonction `print_report()` de sorte qu'elle accepte un objet `TableFormatter` en entrée et invoque des méthodes dessus pour produire la sortie. Par exemple, comme ceci :

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Affiche un tableau bien formaté à partir d'une liste de tuples (nom, actions, prix, variation).
    '''
    formatter.headings(['Nom','Actions','Prix','Variation'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

Depuis que vous avez ajouté un argument à `print_report()`, vous devrez également modifier la fonction `portfolio_report()`. Modifiez-la de sorte qu'elle crée un `TableFormatter` comme ceci :

```python
# report.py

import tableformat

...
def portfolio_report(portfoliofile, pricefile):
    '''
    Génère un rapport sur les actions à partir de fichiers de données sur le portefeuille et les prix.
    '''
    # Lire les fichiers de données
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Créer les données du rapport
    report = make_report_data(portfolio, prices)

    # L'afficher
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

Exécutez ce nouveau code :

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... plante...
```

Il devrait immédiatement planter avec une exception `NotImplementedError`. Ce n'est pas très passionnant, mais c'est exactement ce que nous attendions. Passons à la partie suivante.
