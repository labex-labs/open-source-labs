# Применение декораторов к методам класса

Теперь мы рассмотрим, как декораторы взаимодействуют с методами класса. Это может быть немного сложно, так как в Python есть разные типы методов: методы экземпляра, методы класса, статические методы и свойства. Декораторы - это функции, которые принимают другую функцию и расширяют поведение последней, не модифицируя ее явно. При применении декораторов к методам класса необходимо обратить внимание на то, как они работают с разными типами методов.

## Понимание проблемы

Давайте посмотрим, что происходит, когда мы применяем наш декоратор `@logged` к разным типам методов. Декоратор `@logged`, вероятно, используется для логирования информации о вызовах методов.

1. Создайте новый файл `methods.py` в WebIDE. Этот файл будет содержать наш класс с разными типами методов, декорированными декоратором `@logged`.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

В этом коде у нас есть класс `Spam` с четырьмя разными типами методов. Каждый метод декорирован декоратором `@logged`, а некоторые также декорированы другими встроенными декораторами, такими как `@classmethod`, `@staticmethod` и `@property`.

2. Давайте протестируем, как это работает. Мы выполним команду Python в терминале, чтобы вызвать эти методы и посмотреть на вывод.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

При выполнении этой команды вы, возможно, заметите некоторые проблемы:

- Декоратор `@property` может не работать корректно с нашим декоратором `@logged`. Декоратор `@property` используется для определения метода как свойства, и он имеет особый способ работы. При использовании вместе с декоратором `@logged` могут возникнуть конфликты.
- Порядок декораторов имеет значение для `@classmethod` и `@staticmethod`. Порядок применения декораторов может изменить поведение метода.

## Порядок применения декораторов

Когда вы применяете несколько декораторов, они применяются снизу вверх. Это означает, что декоратор, ближайший к определению метода, применяется первым, а затем последовательно применяются те, которые находятся выше. Например:

```python
@decorator1
@decorator2
def func():
    pass
```

Это эквивалентно:

```python
func = decorator1(decorator2(func))
```

В этом примере `decorator2` применяется к `func` первым, а затем `decorator1` применяется к результату `decorator2(func)`.

## Исправление порядка декораторов

Давайте обновим наш файл `methods.py`, чтобы исправить порядок декораторов. Изменяя порядок декораторов, мы можем убедиться, что каждый метод работает как ожидается.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

В этой обновленной версии:

- Для `instance_method` порядок не имеет значения. Методы экземпляра вызываются на экземпляре класса, и декоратор `@logged` может быть применен в любом порядке, не влияя на его базовую функциональность.
- Для `class_method` мы применяем `@classmethod` после `@logged`. Декоратор `@classmethod` изменяет способ вызова метода, и применение его после `@logged` гарантирует, что логирование работает корректно.
- Для `static_method` мы применяем `@staticmethod` после `@logged`. Подобно `@classmethod`, декоратор `@staticmethod` имеет свое собственное поведение, и порядок с декоратором `@logged` должен быть правильным.
- Для `property_method` мы применяем `@property` после `@logged`. Это гарантирует, что поведение свойства сохраняется, а также обеспечивается функциональность логирования.

3. Давайте протестируем обновленный код. Мы выполним ту же команду, что и раньше, чтобы проверить, были ли исправлены проблемы.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Теперь вы должны увидеть правильное логирование для всех типов методов:

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## Лучшие практики при использовании декораторов методов

При работе с декораторами методов следуйте этим лучшим практикам:

1. Применяйте декораторы, изменяющие метод (`@classmethod`, `@staticmethod`, `@property`) **после** своих пользовательских декораторов. Это гарантирует, что пользовательские декораторы могут выполнить свои операции по логированию или другим задачам сначала, а затем встроенные декораторы могут изменить метод как задумано.
2. Будьте осведомлены о том, что выполнение декоратора происходит во время определения класса, а не во время вызова метода. Это означает, что любой код настройки или инициализации в декораторе будет выполнен при определении класса, а не при вызове метода.
3. В более сложных случаях вам, возможно, придется создавать специализированные декораторы для разных типов методов. Разные типы методов имеют разное поведение, и универсальный декоратор может не работать во всех ситуациях.
