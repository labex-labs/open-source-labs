# Exemple d'affectation

Considérez ce fragment de code.

```python
a = [1,2,3]
b = a
c = [a,b]
```

Une représentation des opérations mémoire sous-jacentes. Dans cet exemple, il n'y a qu'un seul objet liste `[1,2,3]`, mais quatre références différentes à cet objet.

![Diagramme d'exemple de référence mémoire](../assets/references.png)

Cela signifie que modifier une valeur affecte _toutes_ les références.

```python
>>> a.append(999)
>>> a
[1,2,3,999]
>>> b
[1,2,3,999]
>>> c
[[1,2,3,999], [1,2,3,999]]
>>>
```

Remarquez comment un changement dans la liste d'origine se reflète partout ailleurs (yikes!). C'est parce qu'aucune copie n'a été faite. Tout pointe vers la même chose.
