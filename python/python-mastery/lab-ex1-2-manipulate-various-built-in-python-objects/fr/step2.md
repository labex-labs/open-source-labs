# Partie 2 : Manipulation de chaînes de caractères

Définissez une chaîne de caractères contenant une série de symboles de titres boursiers comme ceci :

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
```

Maintenant, essayons différentes opérations sur les chaînes de caractères :

## Extraction de caractères individuels et de sous-chaînes

Les chaînes de caractères sont des tableaux de caractères. Essayez d'en extraire quelques-uns :

```python
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]        # Dernier caractère
'O'
>>> symbols[-2]        # 2e caractère en partant de la fin
'C'
>>>
```

Essayons de prendre quelques tranches :

```python
>>> symbols[:4]
'AAPL'
>>> symbols[-3:]
'SCO'
>>> symbols[5:8]
'IBM'
>>>
```

## Chaînes de caractères en tant qu'objets en lecture seule

Les chaînes de caractères sont en lecture seule. Vérifiez-le en essayant de changer le premier caractère de `symbols` en 'a' en minuscules.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

## Concaténation de chaînes de caractères

Bien que les données de chaîne de caractères soient en lecture seule, vous pouvez toujours réaffecter une variable à une chaîne de caractères nouvellement créée.\
Essayez l'énoncé suivant qui concatène un nouveau symbole "GOOG" à la fin de `symbols` :

```python
>>> symbols += ' GOOG'
>>> symbols
... regardez le résultat...
```

Maintenant, essayez d'ajouter "HPQ" au début de `symbols` comme ceci :

```python
>>> symbols = 'HPQ'+ symbols
>>> symbols
... regardez le résultat...
```

Il est important de noter dans ces deux exemples que la chaîne de caractères d'origine `symbols` n'est _PAS_ modifiée "in place". Au lieu de cela, une chaîne de caractères entièrement nouvelle est créée. Le nom de variable `symbols` est simplement lié au résultat. Ensuite, l'ancienne chaîne de caractères est détruite car elle n'est plus utilisée.

## Test d'appartenance (test de sous-chaîne)

Essayez l'opérateur `in` pour vérifier l'existence de sous-chaînes. Au niveau de l'invite interactive, essayez ces opérations :

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
>>>
```

Assurez-vous de comprendre pourquoi le test pour "AA" a renvoyé `True`.

## Méthodes de chaîne de caractères

Au niveau de l'invite interactive Python, essayez d'expérimenter quelques-unes des méthodes de chaîne de caractères.

```python
>>> symbols.lower()
'hpq aapl ibm msft yhoo sco goog'
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Rappelez-vous, les chaînes de caractères sont toujours en lecture seule. Si vous voulez conserver le résultat d'une opération, vous devez le placer dans une variable :

```python
>>> lowersyms = symbols.lower()
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'
>>>
```

Essayez quelques autres opérations :

```python
>>> symbols.find('MSFT')
13
>>> symbols[13:17]
'MSFT'
>>> symbols = symbols.replace('SCO','')
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```
