# Exercice 4.11 : Définition d'une exception personnalisée

Il est souvent une bonne pratique pour les bibliothèques de définir leurs propres exceptions.

Cela facilite la distinction entre les exceptions de Python levées en réponse à des erreurs de programmation courantes et les exceptions intentionnellement levées par une bibliothèque pour signaler un problème d'utilisation spécifique.

Modifiez la fonction `create_formatter()` de l'exercice précédent de sorte qu'elle lève une exception personnalisée `FormatError` lorsque l'utilisateur fournit un nom de format incorrect.

Par exemple :

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```
