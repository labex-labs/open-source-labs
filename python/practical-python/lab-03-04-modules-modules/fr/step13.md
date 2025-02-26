# Exercice 3.12 : Utilisation de votre module de bibliothèque

Dans la section 2, vous avez écrit un programme `report.py` qui produisait un rapport sur les actions comme ceci :

          Nom     Actions      Prix     Changement
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

Prenez ce programme et modifiez-le de sorte que tout le traitement des fichiers d'entrée soit effectué à l'aide de fonctions dans votre module `fileparse`. Pour ce faire, importez `fileparse` en tant que module et modifiez les fonctions `read_portfolio()` et `read_prices()` pour utiliser la fonction `parse_csv()`.

Utilisez l'exemple interactif au début de cet exercice comme guide. Ensuite, vous devriez obtenir exactement la même sortie qu'avant.
