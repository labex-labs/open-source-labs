# 정의하기

이름은 나중에 사용되기 전에 항상 정의되어야 합니다.

```python
def square(x):
    return x*x

a = 42
b = a + 2     # Requires that `a` is defined

z = square(b) # Requires `square` and `b` to be defined
```

**순서가 중요합니다.** 변수와 함수의 정의는 거의 항상 맨 위에 둡니다.
