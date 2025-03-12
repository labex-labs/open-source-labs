# Définition d'une fonction

Dans cette étape, nous allons apprendre à créer une fonction. Une fonction en Python est un bloc de code organisé et réutilisable utilisé pour effectuer une seule action liée. Ici, notre fonction lira les données d'un portefeuille depuis un fichier et calculera le coût total. Cela est utile car une fois que nous avons cette fonction, nous pouvons l'utiliser plusieurs fois avec différents fichiers de portefeuille, ce qui nous évite d'écrire le même code à plusieurs reprises.

## Comprendre le problème

Dans le laboratoire précédent, vous avez peut - être écrit du code pour lire les données d'un portefeuille et calculer le coût total. Mais ce code était probablement écrit de manière à ne pas être facilement réutilisable. Maintenant, nous allons convertir ce code en une fonction réutilisable.

Les fichiers de données de portefeuille ont un format spécifique. Ils contiennent des informations sous la forme "Symbole Nombre_de_titres Prix". Chaque ligne du fichier représente une action détenue. Par exemple, dans un fichier nommé `portfolio.dat`, vous pourriez voir des lignes comme celles - ci :

```
AA 100 32.20
IBM 50 91.10
...
```

Ici, la première partie (comme "AA" ou "IBM") est le symbole de l'action, qui est un identifiant unique pour l'action. La deuxième partie est le nombre de titres que vous possédez de cette action, et la troisième partie est le prix par titre.

## Création de la fonction

Créons un fichier Python appelé `pcost.py` dans le répertoire `/home/labex/project`. Ce fichier contiendra notre fonction. Voici le code que nous allons placer dans le fichier `pcost.py` :

```python
def portfolio_cost(filename):
    """
    Calcule le coût total (nombre_de_titres*prix) d'un fichier de portefeuille

    Args:
        filename: Le nom du fichier de portefeuille

    Returns:
        Le coût total du portefeuille sous forme de nombre à virgule flottante
    """
    total_cost = 0.0

    # Ouvre le fichier et lit chaque ligne
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            # Extrait les données (symbole, nombre_de_titres, prix)
            shares = int(fields[1])
            price = float(fields[2])
            # Ajoute le coût au total en cours
            total_cost += shares * price

    return total_cost

# Appelle la fonction avec le fichier portfolio.dat
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

Dans ce code, nous définissons d'abord une fonction nommée `portfolio_cost` qui prend un `filename` comme argument. À l'intérieur de la fonction, nous initialisons une variable `total_cost` à 0.0. Ensuite, nous ouvrons le fichier à l'aide de la fonction `open` en mode lecture (`'r'`). Nous utilisons une boucle `for` pour parcourir chaque ligne du fichier. Pour chaque ligne, nous la divisons en champs à l'aide de la méthode `split()`. Nous extrayons ensuite le nombre de titres et le convertissons en entier, et le prix et le convertissons en nombre à virgule flottante. Nous calculons le coût de cette action détenue en multipliant le nombre de titres par le prix et l'ajoutons au `total_cost`. Enfin, nous retournons le `total_cost`.

La partie `if __name__ == '__main__':` est utilisée pour appeler la fonction lorsque le script est exécuté directement. Nous passons le chemin du fichier `portfolio.dat` à la fonction et affichons le résultat.

## Test de la fonction

Maintenant, exécutons le programme pour voir s'il fonctionne. Nous devons nous déplacer dans le répertoire où se trouve le fichier `pcost.py`, puis exécuter le script Python. Voici les commandes pour cela :

```bash
cd /home/labex/project
python3 pcost.py
```

Après avoir exécuté ces commandes, vous devriez voir la sortie suivante :

```
44671.15
```

Cette sortie représente le coût total de toutes les actions du portefeuille.

## Comprendre le code

Découpons ce que fait notre fonction étape par étape :

1. Elle prend un `filename` comme paramètre d'entrée. Cela nous permet d'utiliser la fonction avec différents fichiers de portefeuille.
2. Elle ouvre le fichier et le lit ligne par ligne. Cela est fait à l'aide de la fonction `open` et d'une boucle `for`.
3. Pour chaque ligne, elle divise la ligne en champs à l'aide de la méthode `split()`. Cette méthode divise la ligne en une liste de chaînes de caractères en fonction des espaces.
4. Elle convertit le nombre de titres en entier et le prix en nombre à virgule flottante. Cela est nécessaire car les données lues depuis le fichier sont au format chaîne de caractères, et nous devons effectuer des opérations arithmétiques sur elles.
5. Elle calcule le coût (nombre_de_titres \* prix) pour chaque action détenue et l'ajoute au total en cours. Cela nous donne le coût total du portefeuille.
6. Elle retourne le coût total final. Cela nous permet d'utiliser le résultat dans d'autres parties de notre programme si nécessaire.

Cette fonction est maintenant réutilisable. Nous pouvons l'appeler avec différents fichiers de portefeuille pour calculer leurs coûts, ce qui rend notre code plus efficace et plus facile à maintenir.
