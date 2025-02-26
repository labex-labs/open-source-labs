# Futuros

A veces, el código de Python se ejecuta de manera concurrente a través de hilos o procesos. Para ilustrar, prueba este ejemplo:

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # Llamada normal a la función
About to work
Done
5
>>>
```

Ahora, lanza `worker()` en un hilo separado:

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

Observa detenidamente que el resultado del cálculo no aparece en ningún lugar. No solo eso, sino que ni siquiera sabes cuándo se va a completar. Hay un cierto problema de coordinación aquí. La convención para manejar este caso es envolver el resultado de una función en un `Future`. Un `Future` representa un resultado futuro. Aquí es cómo funciona:

```python
>>> from concurrent.futures import Future
>>> # Envoltorio alrededor de la función para usar un futuro
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

Verás este tipo de patrón con frecuencia si trabajas con piscinas de hilos, procesos y otras estructuras. Por ejemplo:

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
