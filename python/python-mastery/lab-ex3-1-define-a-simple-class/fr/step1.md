# Ajout d'une méthode sell à la classe Stock

Dans cette étape, nous allons améliorer la classe `Stock` en ajoutant une nouvelle méthode. Une méthode est comme une fonction spéciale qui appartient à une classe et peut interagir avec les objets créés à partir de cette classe. Nous allons créer une méthode nommée `sell(nshares)` qui nous aidera à simuler l'action de vendre des actions d'une entreprise. Lorsque vous vendez des actions, le nombre d'actions que vous possédez diminue, et cette méthode se chargera de cette réduction pour nous.

## Qu'est-ce qu'une méthode ?

Commençons par comprendre ce qu'est une méthode. Une méthode est une fonction définie à l'intérieur d'une classe. Elle est conçue pour opérer sur les instances (qui sont comme des copies individuelles) de cette classe. Lorsqu'une méthode est appelée sur un objet, elle peut accéder à tous les attributs (caractéristiques) de cet objet. Elle le fait grâce au paramètre `self`. Le paramètre `self` est une référence à l'objet sur lequel la méthode est appelée. Donc, lorsque vous utilisez `self` à l'intérieur d'une méthode, vous faites référence à l'objet spécifique sur lequel la méthode agit.

## Instructions d'implémentation

1. Tout d'abord, nous devons ouvrir le fichier `stock.py` dans l'éditeur. Pour ce faire, nous allons utiliser la ligne de commande. Ouvrez votre terminal et exécutez la commande suivante. Cette commande change le répertoire pour le dossier `project` où se trouve le fichier `stock.py`.

```bash
cd ~/project
```

2. Une fois que vous avez ouvert le fichier `stock.py`, vous devez trouver un commentaire spécifique dans la classe `Stock`. Recherchez le commentaire `# TODO: Add sell(nshares) method here`. Ce commentaire est un emplacement qui indique où nous devons ajouter notre nouvelle méthode `sell`.

3. Maintenant, il est temps d'ajouter la méthode `sell`. Cette méthode prendra un paramètre appelé `nshares`, qui représente le nombre d'actions que vous souhaitez vendre. Le principal rôle de cette méthode est de diminuer l'attribut `shares` de l'objet `Stock` du nombre d'actions que vous vendez.

Voici le code de la méthode `sell` que vous devez ajouter :

```python
def sell(self, nshares):
    self.shares -= nshares
```

Dans ce code, `self.shares` fait référence à l'attribut `shares` de l'objet `Stock`. L'opérateur `-=` soustrait la valeur de `nshares` de la valeur actuelle de `self.shares`.

4. Après avoir ajouté la méthode `sell`, vous devez enregistrer le fichier `stock.py`. Vous pouvez le faire en appuyant sur `Ctrl+S` sur votre clavier ou en sélectionnant "File > Save" dans le menu de votre éditeur.

5. Pour vous assurer que notre méthode `sell` fonctionne correctement, nous allons créer un script de test. Créez un nouveau fichier Python appelé `test_sell.py` et ajoutez le code suivant :

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

Dans ce script, nous importons d'abord la classe `Stock` à partir du fichier `stock.py`. Ensuite, nous créons un objet `Stock` nommé `s` avec le symbole d'action `GOOG`, 100 actions et un prix de 490,10. Nous affichons le nombre initial d'actions. Ensuite, nous appelons la méthode `sell` sur l'objet `s` pour vendre 25 actions. Enfin, nous affichons le nombre d'actions après la vente.

6. Maintenant, nous allons exécuter le script de test pour voir si notre méthode `sell` fonctionne comme prévu. Ouvrez à nouveau votre terminal et exécutez la commande suivante :

```bash
python3 test_sell.py
```

Si tout fonctionne correctement, vous devriez voir une sortie similaire à ceci :

```
Initial shares: 100
Shares after selling: 75
```

Cette sortie confirme que notre méthode `sell` fonctionne correctement. Elle a réussi à réduire le nombre d'actions du montant que nous avons spécifié.
