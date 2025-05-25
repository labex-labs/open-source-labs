# "믹스인 (Mixin)" 패턴

_믹스인 (Mixin)_ 패턴은 코드 조각을 가진 클래스입니다.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

이 클래스는 단독으로 사용할 수 없습니다. 상속을 통해 다른 클래스와 섞입니다.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

놀랍게도, 이제 시끄러움 (loudness) 은 단 한 번 구현되었고, 완전히 관련 없는 두 클래스에서 재사용되었습니다. 이러한 트릭은 Python 에서 다중 상속을 사용하는 주요 목적 중 하나입니다.
