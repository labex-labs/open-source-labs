# 데이터 포인트 생성

이 단계에서는 사용자 정의 단위 클래스인 `Foo`를 사용하여 몇 개의 데이터 포인트를 생성합니다.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
