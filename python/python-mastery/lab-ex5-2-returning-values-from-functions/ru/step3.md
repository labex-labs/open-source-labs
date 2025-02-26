# Futures

Иногда код на Python выполняется одновременно с использованием потоков или процессов. Для примера попробуйте этот код:

```python
>>> import time
>>> def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

>>> worker(2, 3)     # Обычный вызов функции
About to work
Done
5
>>>
```

Теперь запустите `worker()` в отдельном потоке:

```python
>>> import threading
>>> t = threading.Thread(target=worker, args=(2, 3))
>>> t.start()
About to work
>>>
Done
```

Обратите внимание, что результат вычисления нигде не появляется. Не только это, вы даже не знаете, когда оно будет завершено. Здесь есть определенная проблема координации. Convention для обработки этого случая - обернуть результат функции в `Future`. `Future` представляет будущий результат. Вот, как это работает:

```python
>>> from concurrent.futures import Future
>>> # Обертка вокруг функции для использования future
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

Вы будете часто видеть такой паттерн, если работаете с пулом потоков, процессами и другими конструкциями. Например:

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
