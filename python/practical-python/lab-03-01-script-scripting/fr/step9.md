# Chaînes de documentation

Il est recommandé d'inclure une documentation sous forme d'une chaîne de documentation (doc-string). Les doc-strings sont des chaînes écrites immédiatement après le nom de la fonction. Elles alimentent `help()`, les IDE et d'autres outils.

```python
def read_prices(filename):
    '''
    Lire les prix à partir d'un fichier CSV contenant des données nom,prix
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Une bonne pratique pour les doc-strings est d'écrire un court résumé d'une phrase de ce que fait la fonction. Si plus d'informations sont nécessaires, inclure un court exemple d'utilisation ainsi qu'une description plus détaillée des arguments.
