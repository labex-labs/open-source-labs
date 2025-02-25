# Clés composites

Presque tout type de valeur peut être utilisé comme clé d'un dictionnaire en Python. Une clé de dictionnaire doit être d'un type qui est immuable. Par exemple, des tuples :

```python
holidays = {
  (1, 1) : 'Jour de l'an',
  (3, 14) : 'Jour de Pi',
  (9, 13) : "Jour du programmeur",
}
```

Ensuite, pour accéder :

```python
>>> holidays[3, 14]
'Jour de Pi'
>>>
```

_Aucune liste, ensemble ni autre dictionnaire ne peut servir de clé de dictionnaire, car les listes et les dictionnaires sont mutables._
