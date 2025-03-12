# Travailler avec les dictionnaires en Python

En Python, les dictionnaires sont une structure de données fondamentale. Ce sont des magasins de paires clé - valeur, ce qui signifie qu'ils vous permettent de faire correspondre une valeur (la valeur) à une autre (la clé). Cela est extrêmement utile lorsqu'il s'agit de traiter des données qui ont des relations naturelles de type clé - valeur. Par exemple, vous pourriez vouloir associer le nom d'une personne (la clé) à son âge (la valeur), ou, comme nous le verrons dans ce laboratoire, associer des symboles de titres boursiers (les clés) à leurs prix (les valeurs).

## Création et accès aux dictionnaires

Commençons par ouvrir une nouvelle session interactive Python. C'est comme entrer dans un environnement spécial où vous pouvez écrire et exécuter du code Python ligne par ligne. Pour démarrer cette session, ouvrez votre terminal et tapez la commande suivante :

```bash
python3
```

Une fois que vous êtes dans la session interactive Python, vous pouvez créer un dictionnaire. Dans notre cas, nous allons créer un dictionnaire qui associe des symboles de titres boursiers à leurs prix. Voici comment faire :

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

Dans la première ligne, nous créons un dictionnaire nommé `prices` et lui assignons quelques paires clé - valeur. Les clés sont les symboles de titres boursiers (`IBM`, `GOOG`, `AAPL`), et les valeurs sont les prix correspondants. La deuxième ligne nous montre simplement le contenu du dictionnaire `prices`.

Maintenant, voyons comment accéder et modifier les valeurs dans le dictionnaire en utilisant les clés.

```python
>>> prices['IBM']    # Accéder à la valeur pour la clé 'IBM'
91.1

>>> prices['IBM'] = 123.45    # Mettre à jour une valeur existante
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Ajouter une nouvelle paire clé - valeur
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

Dans la première ligne, nous accédons à la valeur associée à la clé `IBM`. Dans les deuxième et troisième lignes, nous mettons à jour la valeur pour la clé `IBM`, puis nous ajoutons une nouvelle paire clé - valeur (`HPQ` avec un prix de `26.15`).

## Obtenir les clés d'un dictionnaire

Parfois, vous pourriez vouloir obtenir une liste de toutes les clés d'un dictionnaire. Il y a plusieurs façons de le faire.

```python
>>> list(prices)    # Convertir les clés du dictionnaire en une liste
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

Ici, nous utilisons la fonction `list()` pour convertir les clés du dictionnaire `prices` en une liste.

Vous pouvez également utiliser la méthode `keys()`, qui retourne un objet spécial appelé `dict_keys`.

```python
>>> prices.keys()    # Retourne un objet dict_keys
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Obtenir les valeurs d'un dictionnaire

De même, vous pourriez vouloir obtenir toutes les valeurs d'un dictionnaire. Vous pouvez utiliser la méthode `values()` pour cela.

```python
>>> prices.values()    # Retourne un objet dict_values
dict_values([123.45, 490.1, 312.23, 26.15])
```

Cette méthode retourne un objet `dict_values` qui contient toutes les valeurs du dictionnaire `prices`.

## Suppression d'éléments

Si vous voulez supprimer une paire clé - valeur d'un dictionnaire, vous pouvez utiliser le mot - clé `del`.

```python
>>> del prices['AAPL']    # Supprimer l'entrée 'AAPL'
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

Ici, nous supprimons la paire clé - valeur avec la clé `AAPL` du dictionnaire `prices`.

## Vérification de l'existence d'une clé

Pour vérifier si une clé existe dans un dictionnaire, vous pouvez utiliser l'opérateur `in`.

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

L'opérateur `in` retourne `True` si la clé existe dans le dictionnaire et `False` sinon.

## Méthodes des dictionnaires

Les dictionnaires ont plusieurs méthodes utiles. Voyons en quelques - unes.

```python
>>> prices.get('MSFT', 0)    # Obtenir la valeur ou une valeur par défaut si la clé n'existe pas
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Mettre à jour plusieurs valeurs
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

La méthode `get()` essaie d'obtenir la valeur associée à une clé. Si la clé n'existe pas, elle retourne une valeur par défaut (dans ce cas, `0`). La méthode `update()` est utilisée pour mettre à jour plusieurs paires clé - valeur dans le dictionnaire en une seule fois.

Lorsque vous avez terminé de travailler dans la session interactive Python, vous pouvez la quitter en tapant :

```python
>>> exit()
```
