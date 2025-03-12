# Comprendre le module principal (main module) en Python

En Python, lorsque vous exécutez directement un script, il agit comme le "module principal" (main module). Python a une variable spéciale nommée `__name__`. Lorsqu'un fichier est exécuté directement, Python attribue à la valeur de `__name__` la chaîne `"__main__"`. Cela est différent du cas où le fichier est importé comme un module.

Cette fonctionnalité est très utile car elle vous permet d'écrire un code qui se comporte différemment selon que le fichier est exécuté directement ou importé. Par exemple, vous pourriez vouloir que certains codes s'exécutent seulement lorsque vous exécutez le fichier comme un script, mais pas lorsqu'il est importé par un autre script.

## Modifier pcost.py pour utiliser le modèle du module principal

Modifions le programme `pcost.py` pour tirer parti de ce modèle.

1. Tout d'abord, vous devez ouvrir le fichier `pcost.py` dans l'éditeur. Vous pouvez utiliser les commandes suivantes pour accéder au répertoire du projet et créer le fichier s'il n'existe pas :

```bash
cd ~/project
touch pcost.py
```

La commande `cd` change le répertoire actuel pour le répertoire `project` dans votre répertoire personnel. La commande `touch` crée un nouveau fichier nommé `pcost.py` s'il n'existe pas déjà.

2. Maintenant, modifiez le fichier `pcost.py` pour qu'il ressemble à ceci :

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# Ce code ne s'exécute que lorsque le fichier est exécuté comme un script
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

La principale modification ici est que nous avons enveloppé le code à la fin dans une condition `if __name__ == "__main__":`. Cela signifie que le code à l'intérieur de ce bloc ne s'exécutera que lorsque le fichier est exécuté directement comme un script, pas lorsqu'il est importé comme un module.

3. Après avoir effectué ces modifications, enregistrez le fichier et quittez l'éditeur.

## Tester le module modifié

Maintenant, testons notre module modifié de deux manières différentes pour voir comment il se comporte.

1. Tout d'abord, exécutez le programme directement comme un script en utilisant la commande suivante :

```bash
python3 pcost.py
```

Vous devriez voir la sortie `44671.15`, comme avant. C'est parce que lorsque vous exécutez le script directement, la variable `__name__` est définie sur `"__main__"`, donc le code à l'intérieur du bloc `if __name__ == "__main__":` est exécuté.

2. Ensuite, redémarrez l'interpréteur Python et importez le module :

```bash
python3
```

```python
import pcost
```

Cette fois, vous ne verrez aucune sortie. Lorsque vous importez le module, la variable `__name__` est définie sur `"pcost"` (le nom du module), pas `"__main__"`. Donc, le code à l'intérieur du bloc `if __name__ == "__main__":` ne s'exécute pas.

3. Pour vérifier que la fonction `portfolio_cost` fonctionne toujours, vous pouvez l'appeler comme ceci :

```python
pcost.portfolio_cost('portfolio.dat')
```

La fonction devrait retourner `44671.15`, ce qui signifie qu'elle fonctionne correctement.

4. Enfin, quittez l'interpréteur Python en utilisant la commande suivante :

```python
exit()
```

Ce modèle est très utile lors de la création de fichiers Python qui peuvent être utilisés à la fois comme des modules importables et comme des scripts autonomes. Le code à l'intérieur du bloc `if __name__ == "__main__":` ne s'exécute que lorsque le fichier est exécuté directement, pas lorsqu'il est importé comme un module.
