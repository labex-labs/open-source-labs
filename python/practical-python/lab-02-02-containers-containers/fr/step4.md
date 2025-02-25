# Les dictionnaires en tant que conteneur

Les dictionnaires sont utiles si vous voulez effectuer des recherches aléatoires rapides (par nom de clé). Par exemple, un dictionnaire de prix d'actions :

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Voici quelques recherches simples :

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```
