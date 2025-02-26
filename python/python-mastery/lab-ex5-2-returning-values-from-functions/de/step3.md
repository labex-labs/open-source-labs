# Futures

Manchmal führt Python-Code parallel über Threads oder Prozesse aus. Um dies zu veranschaulichen, versuchen Sie dieses Beispiel:

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # Normaler Funktionsaufruf
About to work
Done
5
>>>
```

Nun starten Sie `worker()` in einem separaten Thread:

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

Beachten Sie genau, dass das Ergebnis der Berechnung nirgends erscheint. Nicht nur das, Sie wissen auch nicht einmal, wann es abgeschlossen sein wird. Es gibt hier ein gewisses Koordinationsproblem. Die Konvention für das Handling dieses Falls besteht darin, das Ergebnis einer Funktion in einem `Future` zu verpacken. Ein `Future` repräsentiert ein zukünftiges Ergebnis. So funktioniert es:

```python
>>> from concurrent.futures import Future
>>> # Umhüllung der Funktion, um ein Future zu verwenden
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

Sie werden dieses Muster häufig bei der Arbeit mit Thread-Pools, Prozessen und anderen Konstrukten sehen. Beispielsweise:

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
