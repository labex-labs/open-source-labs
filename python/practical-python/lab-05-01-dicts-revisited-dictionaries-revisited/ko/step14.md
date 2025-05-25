# 이상한 코드 재사용 (다중 상속 관련)

완전히 관련 없는 두 객체를 생각해 봅시다.

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # Code commonality with LoudBike (below)
        return super().noise().upper()
```

그리고

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # Code commonality with LoudDog (above)
        return super().noise().upper()
```

`LoudDog.noise()`와 `LoudBike.noise()`의 구현에 코드 공통성이 있습니다. 사실, 코드는 정확히 같습니다. 당연히, 이러한 코드는 소프트웨어 엔지니어의 관심을 끌 것입니다.
