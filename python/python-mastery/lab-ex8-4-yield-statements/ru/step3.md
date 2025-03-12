# Практические применения управления генераторами

В этом шаге мы рассмотрим, как применить концепции, которые мы узнали о управлении генераторами и обработке исключений в генераторах, в реальных сценариях. Понимание этих практических применений поможет вам писать более надежный и эффективный код на Python.

## Создание надежной системы мониторинга файлов

Построим более надежный вариант нашей системы мониторинга файлов. Эта система должна уметь обрабатывать различные ситуации, такие как истечение времени ожидания и запросы пользователя на остановку.

Сначала откройте редактор WebIDE и создайте новый файл с именем `robust_follow.py`. Вот код, который нужно написать в этом файле:

```python
import os
import time
import signal

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

def follow(filename, timeout=None):
    """
    A generator that yields new lines in a file.
    With timeout handling and proper cleanup.
    """
    try:
        # Set up timeout if specified
        if timeout:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)

        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line == '':
                    # No new data, wait briefly
                    time.sleep(0.1)
                    continue
                yield line
    except TimeoutError:
        print(f"Following timed out after {timeout} seconds")
    except GeneratorExit:
        print("Following stopped by request")
    finally:
        # Clean up timeout alarm if it was set
        if timeout:
            signal.alarm(0)
        print("Follow generator cleanup complete")
```

В этом коде мы сначала определяем пользовательский класс `TimeoutError`. Функция `timeout_handler` используется для вызова этого ошибки при истечении времени ожидания. Функция `follow` является генератором, который читает файл и возвращает новые строки. Если задано время ожидания, она устанавливает сигнал с использованием модуля `signal`. Если в файле нет новых данных, она ждет короткое время перед повторной попыткой. Блок `try - except - finally` используется для обработки различных исключений и обеспечения правильной очистки.

После написания кода сохраните файл.

## Эксперименты с надежной системой мониторинга файлов

Теперь протестируем нашу улучшенную систему мониторинга файлов. Откройте терминал и запустите интерпретатор Python с помощью следующих команд:

```bash
cd ~/project
python3
```

### Эксперимент 1: Базовое использование

В интерпретаторе Python протестируем базовую функциональность нашего генератора `follow`. Вот код для запуска:

```python
>>> from robust_follow import follow
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 2:  # Just read a few lines for the example
...         break
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Line 3: "HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
```

Здесь мы импортируем функцию `follow` из файла `robust_follow.py`. Затем создаем объект - генератор `f`, который отслеживает файл `stocklog.csv`. Мы используем цикл `for` для итерации по строкам, возвращаемым генератором, и выводим первые три строки.

### Эксперимент 2: Использование таймаута

Посмотрим, как работает функция таймаута. Запустите следующий код в интерпретаторе Python:

```python
>>> # Create a generator that will time out after 3 seconds
>>> f = follow('stocklog.csv', timeout=3)
>>> for line in f:
...     print(line.strip())
...     time.sleep(1)  # Process each line slowly
...
"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
Following timed out after 3 seconds
Follow generator cleanup complete
```

В этом эксперименте мы создаем генератор с таймаутом в 3 секунды. Мы обрабатываем каждую строку медленно, засыпая на 1 секунду между каждой строкой. После примерно 3 секунд генератор вызывает исключение по таймауту, и выполняется код очистки в блоке `finally`.

### Эксперимент 3: Явное закрытие

Протестируем, как генератор обрабатывает явное закрытие. Запустите следующий код:

```python
>>> f = follow('stocklog.csv')
>>> for i, line in enumerate(f):
...     print(f"Line {i+1}: {line.strip()}")
...     if i >= 1:
...         print("Explicitly closing the generator...")
...         f.close()
...
Line 1: "MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314
Line 2: "VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
Explicitly closing the generator...
Following stopped by request
Follow generator cleanup complete
```

Здесь мы создаем генератор и начинаем итерироваться по его строкам. После обработки двух строк мы явно закрываем генератор с помощью метода `close`. Затем генератор обрабатывает исключение `GeneratorExit` и выполняет необходимую очистку.

## Создание конвейера обработки данных с обработкой ошибок

Далее мы создадим простой конвейер обработки данных с использованием корутин. Этот конвейер должен уметь обрабатывать ошибки на разных этапах.

Откройте редактор WebIDE и создайте новый файл с именем `pipeline.py`. Вот код, который нужно написать в этом файле:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def grep(pattern, target):
    """Filter lines containing pattern and send to target"""
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except Exception as e:
        target.throw(e)

@consumer
def printer():
    """Print received items"""
    try:
        while True:
            item = yield
            print(f"PRINTER: {item}")
    except Exception as e:
        print(f"PRINTER ERROR: {repr(e)}")

def follow_and_process(filename, pattern):
    """Follow a file and process its contents"""
    import time
    import os

    output = printer()
    filter_pipe = grep(pattern, output)

    try:
        with open(filename, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                filter_pipe.send(line)
    except KeyboardInterrupt:
        print("Processing stopped by user")
    finally:
        filter_pipe.close()
        output.close()
```

В этом коде декоратор `consumer` используется для инициализации корутин. Корутина `grep` фильтрует строки, содержащие определенный шаблон, и отправляет их в другую корутину. Корутина `printer` выводит полученные элементы. Функция `follow_and_process` читает файл, фильтрует его строки с использованием корутины `grep` и выводит совпадающие строки с использованием корутины `printer`. Она также обрабатывает исключение `KeyboardInterrupt` и обеспечивает правильную очистку.

После написания кода сохраните файл.

## Тестирование конвейера обработки данных

Протестируем наш конвейер обработки данных. В терминале запустите следующую команду:

```bash
cd ~/project
python3 -c "from pipeline import follow_and_process; follow_and_process('stocklog.csv', 'IBM')"
```

Вы должны увидеть вывод, похожий на следующий:

```
PRINTER: "IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550

PRINTER: "IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859

PRINTER: "IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
```

Этот вывод показывает, что конвейер работает правильно, фильтруя и выводя строки, содержащие шаблон "IBM".

Для остановки процесса нажмите `Ctrl + C`. Вы должны увидеть следующее сообщение:

```
Processing stopped by user
```

## Основные выводы

1. Правильная обработка исключений в генераторах позволяет создавать надежные системы, которые могутGracefully обрабатывать ошибки. Это означает, что ваши программы не будут аварийно завершаться, если что - то пойдет не так.
2. Вы можете использовать такие техники, как таймауты, чтобы предотвратить бесконечное выполнение генераторов. Это помогает управлять системными ресурсами и гарантирует, что ваша программа не застрянет в бесконечном цикле.
3. Генераторы и корутины могут образовывать мощные конвейеры обработки данных, где ошибки могут распространяться и обрабатываться на соответствующем уровне. Это упрощает построение сложных систем обработки данных.
4. Блок `finally` в генераторах гарантирует выполнение операций очистки, независимо от того, как генератор завершается. Это помогает сохранить целостность вашей программы и предотвратить утечку ресурсов.
