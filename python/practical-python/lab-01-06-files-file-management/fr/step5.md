# Exercice 1.27: Lecture d'un fichier de données

Maintenant que vous savez lire un fichier, écrivons un programme pour effectuer un calcul simple.

Les colonnes dans `portfolio.csv` correspondent au nom de l'action, au nombre d'actions et au prix d'achat d'une seule position d'action. Écrivez un programme appelé `pcost.py` dans le répertoire `/home/labex/project` qui ouvre ce fichier, lit toutes les lignes et calcule combien il a coûté d'acheter toutes les actions du portefeuille.

_Indice : pour convertir une chaîne de caractères en entier, utilisez `int(s)`. Pour convertir une chaîne de caractères en nombre à virgule flottante, utilisez `float(s)`._

Votre programme devrait afficher une sortie telle que la suivante :

```bash
Total cost 44671.15
```
