# Exercice 4.6 : Utiliser l'héritage pour produire différents formats de sortie

La classe `TableFormatter` que vous avez définie dans la partie (a) est destinée à être étendue via l'héritage. En fait, c'est tout le concept. Pour illustrer, définissez une classe `TextTableFormatter` comme ceci :

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    Affiche un tableau au format texte brut
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 +' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Modifiez la fonction `portfolio_report()` comme ceci et essayez-la :

```python
# report.py
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
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

Cela devrait produire la même sortie que précédemment :

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Nom     Actions      Prix     Variation
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Cependant, modifions la sortie en quelque chose d'autre. Définissez une nouvelle classe `CSVTableFormatter` qui produit une sortie au format CSV :

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Affiche les données du portefeuille au format CSV.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Modifiez votre programme principal comme suit :

```python
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
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

Vous devriez maintenant voir une sortie au format CSV comme ceci :

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
Nom,Actions,Prix,Variation
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

En utilisant une idée similaire, définissez une classe `HTMLTableFormatter` qui produit un tableau avec la sortie suivante :

    <tr><th>Nom</th><th>Actions</th><th>Prix</th><th>Variation</th></tr>
    <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
    <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
    <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
    <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
    <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
    <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
    <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

Testez votre code en modifiant le programme principal pour créer un objet `HTMLTableFormatter` au lieu d'un objet `CSVTableFormatter`.
