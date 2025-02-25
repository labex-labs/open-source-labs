# Exécution de fonction retardée

Écrivez une fonction `delay(fn, ms, *args)` qui prend une fonction `fn`, un temps en millisecondes `ms` et un nombre quelconque d'arguments `args`. La fonction devrait retarder l'exécution de `fn` de `ms` millisecondes puis l'appeler avec les arguments fournis. La fonction devrait renvoyer le résultat de l'appel de `fn`.

Pour retarder l'exécution de `fn`, utilisez la fonction `time.sleep()`. Cette fonction prend un nombre de secondes en argument, donc vous devrez convertir `ms` en secondes avant de la passer à `time.sleep()`.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # affiche 'later' après une seconde
```
