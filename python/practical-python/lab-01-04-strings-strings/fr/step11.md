# Chaînes f

Une chaîne avec substitution d'expression formatée.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> a = f'{name:>10s} {shares:10d} {price:10.2f}'
>>> a
'       IBM        100      91.10'
>>> b = f'Cost = ${shares*price:0.2f}'
>>> b
'Cost = $9110.00'
>>>
```

**Remarque : Cela nécessite Python 3.6 ou une version ultérieure.** La signification des codes de format est abordée plus tard.

Dans ces exercices, vous allez experimenter avec des opérations sur le type de chaîne de Python. Vous devriez le faire à l'invite interactive de Python où vous pouvez facilement voir les résultats. Note importante :

> Dans les exercices où vous êtes supposé interagir avec l'interpréteur, `>>>` est l'invite de l'interpréteur que vous obtenez lorsque Python vous demande de taper une nouvelle instruction. Certaines instructions dans l'exercice s'étendent sur plusieurs lignes - pour exécuter ces instructions, vous devrez peut-être appuyer sur 'entrée' plusieurs fois. Juste un rappel que vous _NE PAS_ taper le `>>>` lorsque vous travaillez sur ces exemples.

Commencez par définir une chaîne contenant une série de symboles de cotation boursière comme ceci :

```python
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>>
```
