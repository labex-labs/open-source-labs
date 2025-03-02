# Экземплярные методы

Экземплярные методы - это функции, применяемые к экземплярам объекта.

```python
class Player:
  ...
    # `move` - это метод
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

Объект сам по себе всегда передается в качестве первого аргумента.

```python
>>> a.move(1, 2)

# сопоставляет `a` с `self`
# сопоставляет `1` с `dx`
# сопоставляет `2` с `dy`
def move(self, dx, dy):
```

По соглашению экземпляр называется `self`. Однако, на самом деле имя, которое используется, не имеет значения. Объект всегда передается в качестве первого аргумента. Просто по стилям программирования на Python этот аргумент называется `self`.
