# Expressions génératrices et efficacité mémoire

Dans cette étape, nous allons explorer les expressions génératrices. Elles sont incroyablement utiles lorsque vous travaillez avec de grands ensembles de données en Python. Elles peuvent rendre votre code beaucoup plus efficace en termes de mémoire, ce qui est crucial lorsque vous manipulez de grandes quantités de données.

## Comprendre les expressions génératrices

Une expression génératrice est similaire à une compréhension de liste, mais il y a une différence clé. Lorsque vous utilisez une compréhension de liste, Python crée une liste avec tous les résultats d'un coup. Cela peut prendre beaucoup de mémoire, surtout si vous travaillez avec un grand ensemble de données. En revanche, une expression génératrice produit les résultats un par un au fur et à mesure qu'ils sont nécessaires. Cela signifie qu'elle n'a pas besoin de stocker tous les résultats en mémoire d'un coup, ce qui peut économiser une quantité significative de mémoire.

Regardons un exemple simple pour voir comment cela fonctionne :

```python
# Démarrez une nouvelle session Python si nécessaire
# python3

# Compréhension de liste (crée une liste en mémoire)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Expression génératrice (crée un objet générateur)
squares_gen = (x*x for x in nums)
print(squares_gen)  # Cela n'affiche pas les valeurs, seulement l'objet générateur

# Itérez à travers le générateur pour obtenir les valeurs
for n in squares_gen:
    print(n)
```

Lorsque vous exécutez ce code, vous verrez la sortie suivante :

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

Une chose importante à noter sur les générateurs est qu'ils ne peuvent être itérés qu'une seule fois. Une fois que vous avez parcouru toutes les valeurs d'un générateur, il est épuisé et vous ne pouvez plus obtenir les valeurs.

```python
# Essayez d'itérer à nouveau sur le même générateur
for n in squares_gen:
    print(n)  # Rien ne sera affiché, car le générateur est déjà épuisé
```

Vous pouvez également obtenir manuellement les valeurs d'un générateur une par une en utilisant la fonction `next()`.

```python
# Créez un nouveau générateur
squares_gen = (x*x for x in nums)

# Obtenez les valeurs une par une
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

Lorsqu'il n'y a plus de valeurs dans le générateur, l'appel de `next()` lèvera une exception `StopIteration`.

## Fonctions génératrices avec `yield`

Pour une logique de génération plus complexe, vous pouvez écrire des fonctions génératrices en utilisant l'instruction `yield`. Une fonction génératrice est un type spécial de fonction qui utilise `yield` pour retourner des valeurs une par une au lieu de retourner un seul résultat d'un coup.

```python
def squares(nums):
    for x in nums:
        yield x*x

# Utilisez la fonction génératrice
for n in squares(nums):
    print(n)
```

Lorsque vous exécutez ce code, vous verrez la sortie suivante :

```
1
4
9
16
25
```

## Réduire l'utilisation de mémoire avec les expressions génératrices

Maintenant, voyons comment les expressions génératrices peuvent économiser de la mémoire lorsqu'elles sont utilisées avec de grands ensembles de données. Nous allons utiliser le fichier de données des bus CTA, qui est assez volumineux.

Tout d'abord, essayons une approche gourmande en mémoire :

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Vérifiez l'utilisation de mémoire
current, peak = tracemalloc.get_traced_memory()
print(f"Utilisation mémoire actuelle : {current / 1024 / 1024:.2f} MB")
print(f"Utilisation mémoire maximale : {peak / 1024 / 1024:.2f} MB")
```

Maintenant, quittez Python et redémarrez - le pour comparer avec une approche basée sur les générateurs :

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Utilisez des expressions génératrices pour toutes les opérations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Vérifiez l'utilisation de mémoire
current, peak = tracemalloc.get_traced_memory()
print(f"Utilisation mémoire actuelle : {current / 1024 / 1024:.2f} MB")
print(f"Utilisation mémoire maximale : {peak / 1024 / 1024:.2f} MB")
```

Vous devriez remarquer une différence significative dans l'utilisation de mémoire entre ces deux approches. L'approche basée sur les générateurs traite les données de manière incrémentielle sans charger tout en mémoire d'un coup, ce qui est beaucoup plus efficace en termes de mémoire.

## Expressions génératrices avec des fonctions de réduction

Les expressions génératrices sont particulièrement utiles lorsqu'elles sont combinées avec des fonctions telles que `sum()`, `min()`, `max()`, `any()` et `all()` qui traitent une séquence entière et produisent un seul résultat.

Regardons quelques exemples :

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculez la valeur totale du portefeuille
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Valeur totale du portefeuille : {total_value}")

# Trouvez le nombre minimum d'actions dans n'importe quelle holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Nombre minimum d'actions dans n'importe quelle holding : {min_shares}")

# Vérifiez si une action est IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Le portefeuille contient IBM : {has_ibm}")

# Vérifiez si toutes les actions sont IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"Toutes les actions sont IBM : {all_ibm}")

# Comptez le nombre d'actions IBM
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Nombre total d'actions IBM : {ibm_shares}")
```

Les expressions génératrices sont également utiles pour les opérations sur les chaînes de caractères. Voici comment joindre les valeurs d'un tuple :

```python
s = ('GOOG', 100, 490.10)
# Cela échouerait : ','.join(s)
# Utilisez une expression génératrice pour convertir tous les éléments en chaînes de caractères
joined = ','.join(str(x) for x in s)
print(joined)  # Sortie : 'GOOG,100,490.1'
```

L'avantage clé de l'utilisation d'expressions génératrices dans ces exemples est qu'aucune liste intermédiaire n'est créée, ce qui entraîne un code plus efficace en termes de mémoire.
