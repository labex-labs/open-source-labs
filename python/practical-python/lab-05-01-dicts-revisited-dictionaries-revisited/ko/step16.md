# 왜 `super()`를 사용해야 하는가

메서드를 재정의할 때는 항상 `super()`를 사용하십시오.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

`super()`는 MRO (Method Resolution Order, 메서드 결정 순서) 에서 *다음 클래스*로 위임합니다.

까다로운 부분은 그것이 무엇인지 모른다는 것입니다. 특히 다중 상속이 사용되는 경우 무엇인지 알 수 없습니다.
