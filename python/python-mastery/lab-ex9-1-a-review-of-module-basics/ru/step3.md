# Понимание поведения загрузки модулей

В Python процесс загрузки модулей имеет некоторые интересные особенности. На этом этапе мы рассмотрим эти аспекты, чтобы понять, как Python управляет загрузкой модулей.

1. Сначала посмотрим, что происходит, когда мы пытаемся импортировать модуль снова в рамках одной сессии интерпретатора Python. Когда вы запускаете интерпретатор Python, это похоже на открытие рабочего пространства, где вы можете выполнять код на Python. После того, как вы импортировали модуль, повторный импорт может показаться, что он перезагрузит модуль, но это не так.

```python
>>> import simplemod
```

Обратите внимание, что на этот раз вы не видите вывод "Loaded simplemod". Это потому, что **Python загружает модуль только один раз** за сессию интерпретатора. Последующие инструкции `import` не перезагружают модуль. Python запоминает, что он уже загрузил модуль, поэтому не повторяет процесс загрузки.

2. После импорта модуля вы можете изменить переменные внутри него. Модуль в Python похож на контейнер, который хранит переменные, функции и классы. После импорта модуля вы можете обращаться к его переменным и изменять их, как и с любым другим объектом Python.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

Здесь мы сначала проверяем значение переменной `x` в модуле `simplemod`, которое изначально равно `42`. Затем мы изменяем его значение на `13` и убеждаемся, что изменение произошло. Когда мы вызываем функцию `foo` в модуле, она отражает новое значение `x`.

3. Повторный импорт модуля не сбрасывает изменения, которые мы внесли в его переменные. Даже если мы попытаемся импортировать модуль еще раз, Python не перезагружает его, поэтому изменения, которые мы внесли в его переменные, остаются.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. Если вы хотите принудительно перезагрузить модуль, вам нужно использовать функцию `importlib.reload()`. Иногда вы можете внести изменения в код модуля и хотите, чтобы эти изменения вступили в силу сразу. Функция `importlib.reload()` позволяет сделать именно это.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

Модуль был перезагружен, и значение `x` было сброшено до `42`. Это показывает, что модуль был загружен снова из его исходного кода, и все переменные были инициализированы, как изначально.

5. Python отслеживает все загруженные модули в словаре `sys.modules`. Этот словарь действует как реестр, где Python хранит информацию о всех модулях, которые были загружены в текущей сессии интерпретатора.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

Проверяя, находится ли имя модуля в словаре `sys.modules`, вы можете узнать, был ли модуль загружен. И обратившись к словарю с именем модуля в качестве ключа, вы можете получить информацию о модуле.

6. Вы можете удалить модуль из этого словаря, чтобы заставить Python перезагрузить его при следующем импорте. Если вы удалите модуль из словаря `sys.modules`, Python забудет, что он уже загрузил модуль. Поэтому в следующий раз, когда вы попытаетесь импортировать его, Python загрузит его снова из исходного кода.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

Модуль был загружен снова, потому что он был удален из `sys.modules`. Это еще один способ убедиться, что вы работаете с последней версией кода модуля.
