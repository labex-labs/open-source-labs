# Exercice 1.14 : Concaténation de chaînes de caractères

Bien que les données de chaîne de caractères soient en lecture seule, vous pouvez toujours réaffecter une variable à une chaîne de caractères nouvellement créée.

Essayez l'énoncé suivant qui concatène un nouveau symbole "GOOG" à la fin de `symbols` :

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Oups! Ce n'est pas ce que vous vouliez. Corrigez-le de sorte que la variable `symbols` contienne la valeur `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`.

```python
>>> symbols =?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Ajoutez `'HPQ'` au début de la chaîne :

```python
>>> symbols =?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Dans ces exemples, il peut sembler que la chaîne d'origine soit modifiée, en apparence en violation du fait que les chaînes sont en lecture seule. Ce n'est pas le cas. Les opérations sur les chaînes créent une chaîne entièrement nouvelle chaque fois. Lorsque le nom de variable `symbols` est réaffecté, il pointe vers la chaîne nouvellement créée. Ensuite, l'ancienne chaîne est détruite car elle n'est plus utilisée.
