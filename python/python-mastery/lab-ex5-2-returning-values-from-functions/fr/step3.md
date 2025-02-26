# Futures

Parfois, le code Python s'exécute de manière concurrente via des threads ou des processus. Pour illustrer, essayez cet exemple :

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # Appel normal de fonction
About to work
Done
5
>>>
```

Maintenant, lancez `worker()` dans un thread séparé :

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

Remarquez attentivement que le résultat du calcul n'apparaît nulle part. Pas seulement ça, vous ne savez même pas quand il va être terminé. Il y a un certain problème de coordination ici. La convention pour gérer ce cas est d'envelopper le résultat d'une fonction dans un `Future`. Un `Future` représente un résultat futur. Voici comment ça fonctionne :

```python
>>> from concurrent.futures import Future
>>> # Enveloppe autour de la fonction pour utiliser un futur
>>> def do_work(x, y, fut):
        fut.set_result(worker(x,y))

>>> fut = Future()
>>> t = threading.Thread(target=do_work, args=(2, 3, fut))
>>> t.start()
About to work
>>> result = fut.result()
Done
>>> result
5
>>>
```

Vous verrez ce genre de modèle très souvent si vous travaillez avec des pools de threads, des processus et autres constructions. Par exemple :

```python
>>> from concurrent.futures import ThreadPoolExecutor
>>> pool = ThreadPoolExecutor()
>>> fut = pool.submit(worker, 2, 3)
About to work
>>> fut
<Future at 0x102157080 state=running>
>>> fut.result()
Done
5
>>>
```
