# Exercice 2.16 : Utilisation de la fonction `zip()`

Dans le fichier `portfolio.csv`, la première ligne contient les en-têtes de colonne. Dans tout le code précédent, nous les avons ignorés.

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>>
```

Cependant, que se passe-t-il si vous pouvez utiliser les en-têtes pour quelque chose de pratique? C'est là que la fonction `zip()` entre en jeu. Essayez d'abord ceci pour associer les en-têtes de fichier à une ligne de données :

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

Remarquez comment `zip()` a associé les en-têtes de colonne aux valeurs de colonne. Nous avons utilisé `list()` ici pour convertir le résultat en une liste afin que vous puissiez le voir. Normalement, `zip()` crée un itérateur qui doit être consommé par une boucle `for`.

Cette association est une étape intermédiaire pour construire un dictionnaire. Maintenant, essayez ceci :

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Cette transformation est l'un des trucs les plus utiles à connaître lorsqu'il s'agit de traiter de nombreux fichiers de données. Par exemple, supposons que vous vouliez faire en sorte que le programme `pcost.py` fonctionne avec différents fichiers d'entrée, mais sans vous soucier du numéro réel de colonne où apparaissent le nom, le nombre d'actions et le prix.

Modifiez la fonction `portfolio_cost()` dans `pcost.py` de sorte qu'elle ressemble à ceci :

```python
# pcost.py

def portfolio_cost(filename):
 ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # Cela capture les erreurs dans les conversions de int() et float() ci-dessus
            except ValueError:
                print(f'Ligne {rowno} : Mauvaise ligne : {row}')
 ...
```

Maintenant, essayez votre fonction sur un fichier de données complètement différent `portfoliodate.csv` qui ressemble à ceci :

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

Si vous avez fait cela correctement, vous constaterez que votre programme fonctionne toujours même si le fichier de données a un format de colonne complètement différent de celui d'avant. C'est génial!

Le changement apporté ici est subtil, mais important. Au lieu que `portfolio_cost()` soit codé en dur pour lire un seul format de fichier fixe, la nouvelle version lit n'importe quel fichier CSV et extrait les valeurs d'intérêt. Tant que le fichier a les colonnes requises, le code fonctionnera.

Modifiez le programme `report.py` que vous avez écrit dans la section 2.3 de sorte qu'il utilise la même technique pour extraire les en-têtes de colonne.

Essayez d'exécuter le programme `report.py` sur le fichier `portfoliodate.csv` et constatez qu'il produit la même réponse qu'auparavant.
