# Ensemble des parties

## Problème

Étant donné un ensemble, retourner tous les sous-ensembles possibles de cet ensemble. Les sous-ensembles doivent être uniques, ce qui signifie que si deux sous-ensembles ont les mêmes éléments, ils doivent être considérés comme le même sous-ensemble. L'ensemble vide doit également être inclus en tant que sous-ensemble. Les entrées ne sont pas nécessairement uniques, et on ne peut pas supposer que les entrées sont valides. Cependant, on peut supposer que le problème tient en mémoire.

## Exigences

Pour générer l'ensemble des parties d'un ensemble, nous devons répondre aux exigences suivantes :

- Les sous-ensembles résultants doivent être uniques, considérant comme identiques les sous-ensembles ayant les mêmes éléments.
- L'ensemble vide doit être inclus en tant que sous-ensemble.
- Les entrées ne sont pas nécessairement uniques.
- On ne peut pas supposer que les entrées sont valides.
- On peut supposer que le problème tient en mémoire.

## Utilisation de l'exemple

```txt
* None -> None
* [] -> [[]]
* ['a'] -> [[],
            ['a']]
* ['a', 'b'] -> [[],
                 ['a'],
                 ['b'],
                 ['a', 'b']]
* ['a', 'b', 'c'] -> [[],
                      ['a'],
                      ['b'],
                      ['c'],
                      ['a', 'b'],
                      ['a', 'c'],
                      ['b', 'c'],
                      ['a', 'b', 'c']]
```
