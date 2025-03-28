# Использование синтаксиса from module import

В Python существует несколько способов импортировать компоненты из модулей. Одним из них является синтаксис `from module import`, который мы рассмотрим в этом разделе.

При импорте компонентов из модуля часто хорошей идеей является начать с "чистого листа". Это гарантирует, что не остается переменных или настроек от предыдущих взаимодействий, которые могли бы повлиять на наш текущий эксперимент.

1. Перезапустите интерпретатор Python, чтобы получить чистый статус:

```python
>>> exit()
```

Эта команда завершает текущую сессию интерпретатора Python. После выхода мы запустим новую сессию, чтобы обеспечить свежее окружение.

```bash
python3
```

Эта команда bash запускает новую сессию интерпретатора Python 3. Теперь, когда у нас есть чистое окружение Python, мы можем начать импортировать компоненты из модуля.

2. Импортируйте конкретные компоненты из модуля, используя синтаксис `from module import`:

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Здесь мы используем инструкцию `from simplemod import foo` для импорта только функции `foo` из модуля `simplemod`. Обратите внимание, что даже несмотря на то, что мы запросили только функцию `foo`, весь модуль `simplemod` был загружен. Это подтверждается выводом "Loaded simplemod". Причина этого заключается в том, что Python должен загрузить весь модуль, чтобы получить доступ к функции `foo`.

3. При использовании `from module import` вы не можете обращаться к самому модулю:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

Когда мы используем синтаксис `from module import`, мы напрямую импортируем только указанные компоненты в наше пространство имен. Само имя модуля не импортируется. Поэтому, когда мы пытаемся обратиться к `simplemod.foo()`, Python не распознает `simplemod`, так как он не был импортирован таким образом.

4. Вы можете импортировать несколько компонентов сразу:

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

Синтаксис `from module import` позволяет нам импортировать несколько компонентов из модуля в одной инструкции. Здесь мы импортируем как переменную `x`, так и функцию `foo` из модуля `simplemod`. После импорта мы можем напрямую обращаться к этим компонентам в нашем коде.

5. Когда вы импортируете переменную из модуля, вы создаете новую ссылку на объект, а не ссылку на переменную в модуле:

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

Когда мы импортируем переменную из модуля, мы по сути создаем новую ссылку на тот же объект в нашем локальном пространстве имен. Поэтому, когда мы изменяем локальную переменную `x` на `13`, это не влияет на переменную `x` внутри модуля `simplemod`. Функция `foo()` по-прежнему ссылается на переменную `x` модуля, которая равна `42`. Понимание этого концепта является важным для избежания путаницы в вашем коде.
