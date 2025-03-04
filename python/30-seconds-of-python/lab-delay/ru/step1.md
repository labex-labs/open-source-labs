# Отложенное выполнение функции

Напишите функцию `delay(fn, ms, *args)`, которая принимает функцию `fn`, время в миллисекундах `ms` и любое количество аргументов `args`. Функция должна задержать выполнение `fn` на `ms` миллисекунд, а затем вызвать ее с предоставленными аргументами. Функция должна возвращать результат вызова `fn`.

Для задержки выполнения `fn` используйте функцию `time.sleep()`. Эта функция принимает количество секунд в качестве аргумента, поэтому вам нужно будет преобразовать `ms` в секунды перед передачей ее в `time.sleep()`.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # выводит 'later' через одну секунду
```
