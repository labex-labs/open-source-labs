# Exercice 1.31 : Gestion des erreurs

Que se passe-t-il si vous essayez d'utiliser votre fonction sur un fichier avec des champs manquants?

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

À ce stade, vous êtes confronté à un choix. Pour que le programme fonctionne, vous pouvez soit nettoyer le fichier d'entrée original en éliminant les lignes erronées, soit modifier votre code pour gérer les lignes erronées d'une certaine manière.

Modifiez le programme `pcost.py` pour attraper l'exception, afficher un message d'avertissement et continuer le traitement du reste du fichier.
