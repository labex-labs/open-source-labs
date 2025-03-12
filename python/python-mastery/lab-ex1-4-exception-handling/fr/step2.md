# Ajout de la gestion des erreurs

Lorsque vous travaillez avec des données du monde réel, il est très courant de rencontrer des incohérences ou des erreurs. Par exemple, les données peuvent avoir des valeurs manquantes, des formats incorrects ou d'autres problèmes. Python propose des mécanismes de gestion des exceptions pour gérer ces situations de manière élégante. La gestion des exceptions permet à votre programme de continuer à s'exécuter même lorsqu'il rencontre une erreur, au lieu de planter brutalement.

## Comprendre le problème

Regardons le fichier `portfolio3.dat`. Ce fichier contient des données sur un portefeuille, comme le symbole de l'action, le nombre de titres et le prix par titre. Pour afficher le contenu de ce fichier, nous pouvons utiliser la commande suivante :

```bash
cat /home/labex/project/portfolio3.dat
```

Lorsque vous exécutez cette commande, vous remarquerez que certaines lignes du fichier ont des tirets (`-`) au lieu de nombres pour le nombre de titres. Voici un exemple de ce que vous pourriez voir :

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

Si nous essayons d'exécuter notre code actuel sur ce fichier, il plantera. La raison est que notre code s'attend à convertir le nombre de titres en un entier, mais il ne peut pas convertir un tiret (`-`) en un entier. Essayons d'exécuter le code et voyons ce qui se passe :

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

Vous verrez un message d'erreur comme celui - ci :

```
ValueError: invalid literal for int() with base 10: '-'
```

Cette erreur se produit car Python ne peut pas convertir le caractère `-` en un entier lorsqu'il essaie d'exécuter `int(fields[1])`.

## Introduction à la gestion des exceptions

La gestion des exceptions en Python utilise les blocs `try` et `except`. Le bloc `try` contient le code qui peut lever une exception. Une exception est une erreur qui se produit pendant l'exécution d'un programme. Le bloc `except` contient le code qui sera exécuté si une exception se produit dans le bloc `try`.

Voici un exemple de fonctionnement des blocs `try` et `except` :

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

Lorsque Python exécute le code dans le bloc `try`, si une exception se produit, l'exécution saute immédiatement au bloc `except` correspondant. Le `ExceptionType` dans le bloc `except` spécifie le type d'exception que nous voulons gérer. La variable `e` contient des informations sur l'exception, comme le message d'erreur.

## Modification de la fonction avec gestion des exceptions

Mettons à jour notre fichier `pcost.py` pour gérer les erreurs dans les données. Nous utiliserons les blocs `try` et `except` pour sauter les lignes avec des données incorrectes et afficher un message d'avertissement.

```python
def portfolio_cost(filename):
    """
    Calcule le coût total (nombre_de_titres*prix) d'un fichier de portefeuille
    Gère les lignes avec des données incorrectes en les sautant et en affichant un avertissement.

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
            try:
                # Extrait les données (symbole, nombre_de_titres, prix)
                shares = int(fields[1])
                price = float(fields[2])
                # Ajoute le coût au total en cours
                total_cost += shares * price
            except ValueError as e:
                # Affiche un avertissement pour les lignes qui ne peuvent pas être analysées
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# Appelle la fonction avec le fichier portfolio3.dat
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

Dans ce code mis à jour, nous ouvrons d'abord le fichier et le lisons ligne par ligne. Pour chaque ligne, nous la divisons en champs. Ensuite, nous essayons de convertir le nombre de titres en un entier et le prix en un nombre à virgule flottante. Si cette conversion échoue (c'est - à - dire qu'une `ValueError` se produit), nous affichons un message d'avertissement et sautons cette ligne. Sinon, nous calculons le coût des titres et l'ajoutons au coût total.

## Test de la fonction mise à jour

Maintenant, exécutons le programme mis à jour avec le fichier problématique. Tout d'abord, nous devons nous déplacer dans le répertoire du projet, puis nous pouvons exécuter le script Python.

```bash
cd /home/labex/project
python3 pcost.py
```

Vous devriez voir une sortie comme celle - ci :

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

Le programme fait maintenant ce qui suit :

1. Il tente de traiter chaque ligne du fichier.
2. Si une ligne contient des données invalides, il capture la `ValueError`.
3. Il affiche un message utile sur le problème.
4. Il continue de traiter le reste du fichier.
5. Il retourne le coût total basé sur les lignes valides.

Cette approche rend notre programme beaucoup plus robuste lorsqu'il s'agit de traiter des données imparfaites. Il peut gérer les erreurs de manière élégante et fournir toujours des résultats utiles.
