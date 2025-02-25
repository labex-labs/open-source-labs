# Exécution de fonction retardée

## Problème

Écrivez une fonction `delay(fn, ms, *args)` qui prend une fonction `fn`, un temps en millisecondes `ms` et un nombre quelconque d'arguments `args`. La fonction devrait retarder l'exécution de `fn` de `ms` millisecondes puis l'appeler avec les arguments fournis. La fonction devrait renvoyer le résultat de l'appel de `fn`.

Pour retarder l'exécution de `fn`, utilisez la fonction `time.sleep()`. Cette fonction prend un nombre de secondes en argument, donc vous devrez convertir `ms` en secondes avant de la passer à `time.sleep()`.

## Exemple

```python
def add(x, y):
  return x + y

result = delay(add, 2000, 2, 3)
print(result) # Sortie : 5
```

Dans l'exemple ci-dessus, la fonction `add` est retardée de 2000 millisecondes (2 secondes) avant d'être appelée avec les arguments `2` et `3`. Le résultat de la fonction `add` est ensuite renvoyé et affiché dans la console.
