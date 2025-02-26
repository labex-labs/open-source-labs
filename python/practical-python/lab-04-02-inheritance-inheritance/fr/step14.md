# Exercice 4.7 : Le polymorphisme en action

Une caractéristique majeure de la programmation orientée objet est que vous pouvez insérer un objet dans un programme et qu'il fonctionnera sans avoir à modifier aucun des codes existants. Par exemple, si vous écriviez un programme qui devait utiliser un objet `TableFormatter`, il fonctionnerait peu importe le type d'objet `TableFormatter` que vous lui donniez réellement. Ce comportement est parfois appelé "polymorphisme".

Un problème potentiel est de trouver comment permettre à l'utilisateur de choisir le formatteur qu'il veut. L'utilisation directe des noms de classes tels que `TextTableFormatter` est souvent gênante. Ainsi, vous pourriez envisager une approche simplifiée. Peut-être insérez-vous une instruction `if` dans le code comme ceci :

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Génère un rapport sur les actions à partir de fichiers de données sur le portefeuille et les prix.
    '''
    # Lire les fichiers de données
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Créer les données du rapport
    report = make_report_data(portfolio, prices)

    # L'afficher
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Format inconnu {fmt}')
    print_report(report, formatter)
```

Dans ce code, l'utilisateur spécifie un nom simplifié tel que `'txt'` ou `'csv'` pour choisir un format. Cependant, est-ce que mettre une grosse instruction `if` dans la fonction `portfolio_report()` comme ça est la meilleure idée? Il serait peut-être mieux de déplacer ce code vers une fonction générale ailleurs.

Dans le fichier `tableformat.py`, ajoutez une fonction `create_formatter(name)` qui permet à l'utilisateur de créer un formatteur en donnant un nom de sortie tel que `'txt'`, `'csv'` ou `'html'`. Modifiez `portfolio_report()` de sorte qu'elle ressemble à ceci :

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Génère un rapport sur les actions à partir de fichiers de données sur le portefeuille et les prix.
    '''
    # Lire les fichiers de données
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Créer les données du rapport
    report = make_report_data(portfolio, prices)

    # L'afficher
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

Essayez d'appeler la fonction avec différents formats pour vous assurer qu'elle fonctionne.
