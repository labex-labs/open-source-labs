# Создание динамического метода **init**()

Теперь мы применим наши знания о функции `exec()` к реальному программированию. В Python функция `exec()` позволяет выполнять Python-код, хранящийся в строке. На этом этапе мы модифицируем класс `Structure` для динамического создания метода `__init__()`. Метод `__init__()` - это специальный метод в классах Python, который вызывается при создании объекта этого класса. Мы будем создавать этот метод на основе переменной класса `_fields`, которая содержит список имен полей класса.

Сначала давайте посмотрим на существующий файл `structure.py`. Этот файл содержит текущую реализацию класса `Structure` и класс `Stock`, который наследуется от него. Чтобы просмотреть содержимое файла, откройте его в WebIDE с помощью следующей команды:

```bash
cat /home/labex/project/structure.py
```

В выводе вы увидите, что текущая реализация использует ручной подход для инициализации объектов. Это означает, что код для инициализации атрибутов объекта написан явно, а не генерируется динамически.

Теперь мы собираемся модифицировать класс `Structure`. Мы добавим метод класса `create_init()`, который будет динамически генерировать метод `__init__()`. Чтобы внести эти изменения, откройте файл `structure.py` в редакторе WebIDE и следуйте этим шагам:

1. Удалите существующие методы `_init()` и `set_fields()` из класса `Structure`. Эти методы являются частью ручного подхода к инициализации, и нам они больше не понадобятся, так как мы будем использовать динамический подход.

2. Добавьте метод класса `create_init()` в класс `Structure`. Вот код этого метода:

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

В этом методе мы сначала создаем строку `argstr`, которая содержит все имена полей, разделенные запятыми. Эта строка будет использоваться в качестве списка аргументов для метода `__init__()`. Затем мы создаем код для метода `__init__()` в виде строки. Мы проходим по именам полей и добавляем в код строки, которые присваивают каждый аргумент соответствующему атрибуту объекта. После этого мы используем функцию `exec()` для выполнения кода и сохраняем сгенерированную функцию в словаре `locs`. Наконец, мы используем функцию `setattr()` для установки сгенерированной функции в качестве метода `__init__()` класса.

3. Модифицируйте класс `Stock` для использования этого нового подхода:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Здесь мы определяем `_fields` для класса `Stock` и затем вызываем метод `create_init()` для генерации метода `__init__()` для класса `Stock`.

Ваш полный файл `structure.py` должен теперь выглядеть примерно так:

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Теперь давайте протестируем нашу реализацию, чтобы убедиться, что она работает правильно. Мы запустим файл с юнит-тестами, чтобы проверить, проходят ли все тесты. Используйте следующие команды:

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

Если ваша реализация правильная, вы должны увидеть, что все тесты проходят. Это означает, что динамически сгенерированный метод `__init__()` работает как ожидается.

Вы также можете протестировать класс вручную в оболочке Python. Вот как это можно сделать:

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

В оболочке Python мы сначала импортируем класс `Stock` из файла `structure.py`. Затем мы создаем экземпляр класса `Stock` и выводим его. Мы также можем изменить атрибут `shares` объекта. Однако, когда мы пытаемся установить атрибут, который не существует в списке `_fields`, мы должны получить ошибку `AttributeError`.

Поздравляем! Вы успешно использовали функцию `exec()` для динамического создания метода `__init__()` на основе атрибутов класса. Этот подход может сделать ваш код более гибким и легким в поддержке, особенно при работе с классами, имеющими переменное количество атрибутов.
