# Travailler avec des fichiers

Le fichier `portfolio.dat` contient une liste de lignes avec des informations sur un portefeuille d'actions. Le fichier ressemble à ceci :

    AA 100 32,20
    IBM 50 91,10
    CAT 150 83,44
    MSFT 200 51,23
    GE 95 40,37
    MSFT 50 65,10
    IBM 100 70,44

La première colonne est le nom de l'action, la deuxième colonne est le nombre d'actions, et la troisième colonne est le prix d'achat d'une seule action.

Écrivez un programme appelé `pcost.py` qui ouvre ce fichier, lit toutes les lignes et calcule combien il a coûté d'acheter toutes les actions du portefeuille. Pour ce faire, calculez la somme de la deuxième colonne multipliée par la troisième colonne. Enfin, affichez les résultats du calcul.
