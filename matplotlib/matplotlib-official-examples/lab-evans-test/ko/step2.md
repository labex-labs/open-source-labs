# 사용자 정의 단위 클래스 생성

이 단계에서는 사용자 정의 단위 클래스인 `Foo`를 생성합니다. 이 클래스는 "단위"에 따라 변환 및 다양한 눈금 형식 지정을 지원합니다. 여기서 "단위"는 단순히 스칼라 변환 계수입니다.

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
