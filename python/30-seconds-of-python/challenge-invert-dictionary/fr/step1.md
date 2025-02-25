# Inverser un dictionnaire

## Problème

Écrivez une fonction Python appelée `invert_dictionary(obj)` qui prend un dictionnaire `obj` en argument et renvoie un nouveau dictionnaire avec les clés et les valeurs inversées. Le dictionnaire d'entrée `obj` aura des valeurs hachables uniques. Le dictionnaire de sortie devrait avoir les mêmes clés que le dictionnaire d'entrée, mais les valeurs devraient être les clés du dictionnaire d'entrée.

Vous devriez utiliser `dictionary.items()` en combinaison avec une compréhension de liste pour créer le nouveau dictionnaire.

## Exemple

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```
