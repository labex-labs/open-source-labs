# 사용자 정의 단위 클래스 등록

이 단계에서는 사용자 정의 단위 클래스인 `Foo`를 변환기 클래스인 `FooConverter`에 등록합니다.

```python
units.registry[Foo] = FooConverter()
```
