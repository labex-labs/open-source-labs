# Ajout de la gestion d'erreurs

Lors de la rédaction de programmes qui traitent des données, il est fréquent de rencontrer des erreurs liées à des données invalides (malformées, champs manquants, etc.). Modifiez votre programme `pcost.py` pour lire le fichier de données `portfolio3.dat` et exécutez-le (indice : il devrait planter).

Modifiez légèrement votre fonction de manière à ce qu'elle soit capable de récupérer à partir de lignes avec des données invalides. Par exemple, les fonctions de conversion `int()` et `float()` lèvent une exception `ValueError` si elles ne peuvent pas convertir l'entrée. Utilisez `try` et `except` pour attraper et afficher un message d'avertissement concernant les lignes qui ne peuvent pas être analysées. Par exemple :

```shell
Impossible d'analyser : 'C - 53.08\n'
Raison : littéral invalide pour int() avec base 10 : '-'
Impossible d'analyser : 'DIS - 34.20\n'
Raison : littéral invalide pour int() avec base 10 : '-'
...
```

Essayez d'exécuter à nouveau votre programme sur le fichier `portfolio3.dat`. Il devrait s'exécuter avec succès malgré les messages d'avertissement affichés.
