# Работа с объектами Future для параллельного программирования

В Python, когда вам нужно запускать функции одновременно, то есть параллельно, язык предоставляет полезные инструменты, такие как потоки (threads) и процессы (processes). Но здесь возникает общая проблема: как получить значение, возвращаемое функцией, которая запущена в отдельном потоке? Именно здесь концепция объекта `Future` становится очень важной.

Объект `Future` представляет собой своеобразное временное хранилище для результата, который станет доступен позже. Это способ представить значение, которое функция создаст в будущем, еще до того, как функция завершит выполнение. Давайте лучше поймем эту концепцию на простом примере.

### Шаг 1: Создание нового файла

Сначала вам нужно создать новый файл Python. Назовем его `futures_demo.py`. Вы можете использовать следующую команду в терминале для создания этого файла:

```
touch ~/project/futures_demo.py
```

### Шаг 2: Добавление базового кода функции

Теперь откройте файл `futures_demo.py` и добавьте следующий код Python. Этот код определяет простую функцию и показывает, как работает обычный вызов функции.

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

В этом коде функция `worker` принимает два числа, складывает их, но сначала имитирует длительную задачу, приостанавливая выполнение на 5 секунд. Когда вы вызываете эту функцию обычным способом, программа ждет, пока функция завершит выполнение, и только потом получает возвращаемое значение.

### Шаг 3: Запуск базового кода

Сохраните файл и запустите его с помощью следующей команды в терминале:

```
python ~/project/futures_demo.py
```

Вы должны увидеть вывод, похожий на следующий:

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

Это показывает, что обычный вызов функции ждет завершения функции и только потом возвращает результат.

### Шаг 4: Запуск функции в отдельном потоке

Далее давайте посмотрим, что произойдет, когда мы запустим функцию `worker` в отдельном потоке. Добавьте следующий код в файл `futures_demo.py`:

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

Здесь мы используем класс `threading.Thread` для запуска функции `worker` в новом потоке. Главный поток не ждет завершения функции `worker` и продолжает свое выполнение. Однако, когда поток `worker` завершает работу, у нас нет простого способа получить возвращаемое значение.

### Шаг 5: Запуск кода с потоком

Снова сохраните файл и запустите его той же командой:

```
python ~/project/futures_demo.py
```

Вы заметите, что главный поток продолжает работу, поток `worker` запускается, но мы не можем получить возвращаемое значение функции `worker`.

### Шаг 6: Ручное использование объекта `Future`

Чтобы решить проблему получения возвращаемого значения из потока, мы можем использовать объект `Future`. Добавьте следующий код в файл `futures_demo.py`:

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

В этом коде мы создаем объект `Future` и передаем его в новую функцию `do_work_with_future`. Эта функция вызывает функцию `worker` и затем устанавливает результат в объекте `Future`. Затем главный поток может использовать метод `result()` объекта `Future` для получения результата, когда он станет доступен.

### Шаг 7: Запуск кода с использованием объекта `Future`

Сохраните файл и запустите его снова:

```
python ~/project/futures_demo.py
```

Теперь вы увидите, что мы успешно можем получить возвращаемое значение из функции, запущенной в потоке.

### Шаг 8: Использование `ThreadPoolExecutor`

Класс `ThreadPoolExecutor` в Python делает работу с параллельными задачами еще проще. Добавьте следующий код в файл `futures_demo.py`:

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

`ThreadPoolExecutor` заботится о создании и управлении объектами `Future` за вас. Вам нужно только передать функцию и ее аргументы, и он вернет объект `Future`, который вы можете использовать для получения результата.

### Шаг 9: Запуск полного кода

Сохраните файл в последний раз и запустите его:

```
python ~/project/futures_demo.py
```

### Пояснение

1. **Обычный вызов функции**: Когда вы вызываете функцию обычным способом, программа ждет завершения функции и напрямую получает возвращаемое значение.
2. **Проблема с потоками**: Запуск функции в отдельном потоке имеет недостаток. Нет встроенного способа получить возвращаемое значение функции, запущенной в этом потоке.
3. **Ручное использование объекта `Future`**: Создав объект `Future` и передав его в поток, мы можем установить результат в объекте `Future` и затем получить этот результат из главного потока.
4. **ThreadPoolExecutor**: Этот класс упрощает параллельное программирование. Он управляет созданием и управлением объектами `Future` за вас, что делает проще запуск функций параллельно и получение их возвращаемых значений.

Объекты `Future` имеют несколько полезных методов:

- `result()`: Этот метод используется для получения результата функции. Если результат еще не готов, он будет ждать, пока он не станет доступен.
- `done()`: Вы можете использовать этот метод, чтобы проверить, завершено ли выполнение функции.
- `add_done_callback()`: Этот метод позволяет зарегистрировать функцию, которая будет вызвана, когда результат будет готов.

Этот паттерн очень важен в параллельном программировании, особенно когда вам нужно получить результаты от функций, запущенных параллельно.
