# Валидация (Redux)

В предыдущем упражнении вы написали декоратор `@validated`, который применял аннотации типов. Например:

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

Создайте новый декоратор `@enforce()`, который будет применять типы, указанные в виде аргументов с ключами к декоратору. Например:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

Поведение декорированной функции должно быть идентично. Примечание: используйте ключевое слово `return_` для указания типа возвращаемого значения. `return` является зарезервированным словом в Python, поэтому вам нужно выбрать немного другое имя.

**Обсуждение**

Написание надежных декораторов часто оказывается намного сложнее, чем кажется. Рекомендуемую литературу:
