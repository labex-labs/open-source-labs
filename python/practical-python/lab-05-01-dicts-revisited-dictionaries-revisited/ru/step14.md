# Странный способ повторного использования кода (с использованием множественного наследования)

Рассмотрим два совершенно не связанных объекта:

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Общий код с LoudBike (ниже)
        return super().noise().upper()
```

И

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Общий код с LoudDog (выше)
        return super().noise().upper()
```

В реализации `LoudDog.noise()` и `LoudBike.noise()` есть общий код. На самом деле, код идентичен. Естественно, такой код неизбежно привлекает внимание программистов.
