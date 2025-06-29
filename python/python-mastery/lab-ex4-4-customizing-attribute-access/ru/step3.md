# Делегирование как альтернатива наследованию

В объектно-ориентированном программировании повторное использование и расширение кода - обычная задача. Существует два основных способа достичь этого: наследование и делегирование.

**Наследование** - это механизм, при котором подкласс наследует методы и атрибуты от родительского класса. Подкласс может переопределить некоторые из этих унаследованных методов, чтобы предоставить свою собственную реализацию.

**Делегирование**, с другой стороны, предполагает, что объект содержит другой объект и перенаправляет определенные вызовы методов ему.

В этом шаге мы рассмотрим делегирование как альтернативу наследованию. Мы реализуем класс, который делегирует часть своего поведения другому объекту.

## Создание примера делегирования

Сначала нам нужно создать базовый класс, с которым будет взаимодействовать наш делегирующий класс.

1. Создайте новый файл с именем `base_class.py` в директории `/home/labex/project`. В этом файле будет определен класс с именем `Spam` с тремя методами: `method_a`, `method_b` и `method_c`. Каждый метод выводит сообщение и возвращает результат. Вот код, который нужно поместить в `base_class.py`:

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

Далее мы создадим делегирующий класс.

2. Создайте новый файл с именем `delegator.py`. В этом файле мы определим класс с именем `DelegatingSpam`, который делегирует часть своего поведения экземпляру класса `Spam`.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

В методе `__init__` мы создаем экземпляр класса `Spam`. Метод `method_a` переопределяет исходный метод, но также вызывает метод `method_a` класса `Spam`. Метод `method_c` полностью переопределяет исходный метод. Метод `__getattr__` - это специальный метод в Python, который вызывается, когда обращаются к атрибуту или методу, который не существует в классе `DelegatingSpam`. Затем он делегирует вызов экземпляру `Spam`.

Теперь давайте создадим тестовый файл, чтобы проверить нашу реализацию.

3. Создайте тестовый файл с именем `test_delegation.py`. В этом файле будет создан экземпляр класса `DelegatingSpam` и будут вызваны его методы.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Наконец, мы запустим тестовый скрипт.

4. Запустите тестовый скрипт, используя следующие команды в терминале:

```bash
cd /home/labex/project
python3 test_delegation.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## Делегирование против наследования

Теперь давайте сравним делегирование с традиционным наследованием.

1. Создайте файл с именем `inheritance_example.py`. В этом файле мы определим класс с именем `InheritingSpam`, который наследует от класса `Spam`.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

Класс `InheritingSpam` переопределяет методы `method_a` и `method_c`. В методе `method_a` мы используем `super()`, чтобы вызвать метод `method_a` родительского класса.

Далее мы создадим тестовый файл для примера наследования.

2. Создайте тестовый файл с именем `test_inheritance.py`. В этом файле будет создан экземпляр класса `InheritingSpam` и будут вызваны его методы.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Наконец, мы запустим тест наследования.

3. Запустите тест наследования, используя следующие команды в терминале:

```bash
cd /home/labex/project
python3 test_inheritance.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## Основные различия и соображения

Давайте рассмотрим сходства и различия между делегированием и наследованием.

1. **Переопределение методов**: И делегирование, и наследование позволяют переопределять методы, но синтаксис различается.
   - В делегировании вы определяете собственный метод и решаете, вызывать ли метод обернутого объекта.
   - В наследовании вы определяете собственный метод и используете `super()`, чтобы вызвать метод родительского класса.

2. **Доступ к методам**:
   - В делегировании неопределенные методы перенаправляются через метод `__getattr__`.
   - В наследовании неопределенные методы наследуются автоматически.

3. **Типовые отношения**:
   - При делегировании `isinstance(delegating_spam, Spam)` возвращает `False`, потому что объект `DelegatingSpam` не является экземпляром класса `Spam`.
   - При наследовании `isinstance(inheriting_spam, Spam)` возвращает `True`, потому что класс `InheritingSpam` наследует от класса `Spam`.

4. **Ограничения**: Делегирование через `__getattr__` не работает с специальными методами, такими как `__getitem__`, `__len__` и т.д. Эти методы должны быть явно определены в делегирующем классе.

Делегирование особенно полезно в следующих ситуациях:

- Вы хотите настроить поведение объекта без влияния на его иерархию.
- Вы хотите объединить поведения из нескольких объектов, которые не имеют общего родителя.
- Вам нужна больше гибкости, чем предоставляет наследование.

Наследование обычно предпочтительнее, когда:

- Отношение "является - подтипом" ясно (например, автомобиль является транспортным средством).
- Вам нужно сохранить совместимость типов в вашем коде.
- Необходимо наследовать специальные методы.
