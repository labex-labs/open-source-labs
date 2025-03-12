# Amélioration du conteneur personnalisé pour le découpage (slicing)

Notre conteneur personnalisé est excellent pour accéder à des enregistrements individuels. Cependant, il y a un problème lorsqu'il s'agit du découpage (slicing). Lorsque vous essayez de prendre une tranche de notre conteneur, le résultat n'est pas celui que vous attendez normalement.

Comprenons pourquoi cela se produit. En Python, le découpage (slicing) est une opération courante utilisée pour extraire une partie d'une séquence. Mais pour notre conteneur personnalisé, Python ne sait pas comment créer un nouvel objet `RideData` avec seulement les données découpées. Au lieu de cela, il crée une liste contenant les résultats de l'appel de `__getitem__` pour chaque index dans la tranche.

1. Testons le découpage (slicing) dans le shell Python :

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

Dans ce code, nous importons d'abord le module `readrides`. Ensuite, nous lisons les données du fichier `ctabus.csv` dans une variable `rows`. Lorsque nous essayons de prendre une tranche des 10 premiers enregistrements et vérifions le type du résultat, nous constatons qu'il s'agit d'une liste au lieu d'un objet `RideData`. L'impression du résultat peut montrer quelque chose d'inattendu, comme une liste de nombres au lieu de dictionnaires.

2. Modifions notre classe `RideData` pour gérer correctement le découpage (slicing). Ouvrez `readrides.py` et mettez à jour la méthode `__getitem__` :

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

Dans cette méthode `__getitem__` mise à jour, nous vérifions d'abord si l'`index` est une tranche (slice). Si c'est le cas, nous créons un nouvel objet `RideData` appelé `result`. Ensuite, nous remplissons cet nouvel objet avec des tranches des colonnes de données originales (`routes`, `dates`, `daytypes` et `numrides`). Cela garantit que lorsque nous découpons notre conteneur personnalisé, nous obtenons un autre objet `RideData` au lieu d'une liste. Si l'`index` n'est pas une tranche (c'est-à-dire qu'il s'agit d'un index unique), nous renvoyons un dictionnaire contenant l'enregistrement pertinent.

3. Testons notre capacité améliorée de découpage (slicing) :

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

Après avoir mis à jour la méthode `__getitem__`, nous pouvons tester à nouveau le découpage (slicing). Lorsque nous prenons une tranche des 10 premiers enregistrements, le type du résultat devrait maintenant être `readrides.RideData`. La longueur de la tranche devrait être de 10, et l'accès aux éléments individuels de la tranche devrait nous donner les mêmes résultats que l'accès aux éléments correspondants dans le conteneur original.

4. Vous pouvez également tester avec différents motifs de découpage (slicing) :

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

Ici, nous testons différents motifs de découpage (slicing). La première tranche `rows[0:20:2]` prend tous les autres enregistrements parmi les 20 premiers enregistrements, et la longueur de la tranche résultante devrait être de 10. La deuxième tranche `rows[-10:]` prend les 10 derniers enregistrements, et sa longueur devrait également être de 10.

En implémentant correctement le découpage (slicing), notre conteneur personnalisé se comporte maintenant encore plus comme une liste Python standard, tout en conservant l'efficacité mémoire du stockage orienté colonne.

Cette approche de création de classes de conteneurs personnalisés qui imitent les conteneurs intégrés de Python mais avec des représentations internes différentes est une technique puissante pour optimiser l'utilisation de la mémoire sans changer l'interface que votre code présente aux utilisateurs.
