# Exercice 1.16 : Méthodes de chaîne de caractères

À l'invite interactive de Python, essayez d'expérimenter avec certaines des méthodes de chaîne de caractères.

```python
>>> symbols.lower()
?
>>> symbols
?
>>>
```

Rappelez-vous, les chaînes de caractères sont toujours en lecture seule. Si vous voulez conserver le résultat d'une opération, vous devez le placer dans une variable :

```python
>>> lowersyms = symbols.lower()
>>>
```

Essayez d'autres opérations :

```python
>>> symbols.find('MSFT')
?
>>> symbols[13:17]
?
>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
?
>>> name = '   IBM   \n'
>>> name = name.strip()    # Supprime les espaces blancs environnants
>>> name
?
>>>
```
