# Exercice 3.8 : Reprovoquer des exceptions

La fonction `parse_csv()` que vous avez écrite dans la section précédente permet de sélectionner des colonnes spécifiées par l'utilisateur, mais cela ne fonctionne que si le fichier de données d'entrée a des en-têtes de colonne.

Modifiez le code de manière à ce qu'une exception soit levée si les arguments `select` et `has_headers=False` sont tous les deux passés. Par exemple :

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Ayant ajouté ce contrôle, vous pourriez vous demander si vous devriez effectuer d'autres types de vérifications de cohérence dans la fonction. Par exemple, devriez-vous vérifier que le nom de fichier est une chaîne de caractères, que types est une liste, ou quelque chose de ce genre?

En règle générale, il est généralement préférable de sauter de telles vérifications et de laisser le programme échouer sur des entrées erronées. Le message de traceback indiquera la source du problème et peut aider à déboguer.

La principale raison d'ajouter le contrôle ci-dessus est d'éviter d'exécuter le code dans un mode absurde (par exemple, en utilisant une fonctionnalité qui nécessite des en-têtes de colonne, mais en spécifiant simultanément qu'il n'y a pas d'en-têtes).

Cela indique une erreur de programmation de la part du code appelant. Vérifier les cas qui "ne devraient pas arriver" est souvent une bonne idée.
