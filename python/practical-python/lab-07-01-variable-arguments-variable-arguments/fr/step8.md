# Exercice 7.4 : Passer à travers les arguments

La fonction `fileparse.parse_csv()` a quelques options pour changer le délimiteur de fichier et pour la notification d'erreurs. Peut-être que vous voudriez exposer ces options à la fonction `read_portfolio()` ci-dessus. Apportez ce changement :

    def read_portfolio(filename, **opts):
        '''
        Lit un fichier de portefeuille d'actions dans une liste de dictionnaires avec les clés
        name, shares et price.
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

Une fois que vous avez apporté le changement, essayez de lire un fichier avec quelques erreurs :

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
```

Maintenant, essayez de silencer les erreurs :

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
