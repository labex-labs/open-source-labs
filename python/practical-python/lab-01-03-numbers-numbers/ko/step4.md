# 부동 소수점 (float)

부동 소수점 값을 지정하려면 십진수 또는 지수 표기법을 사용합니다:

```python
a = 37.45
b = 4e5 # 4 x 10**5 or 400,000
c = -1.345e-10
```

부동 소수점은 네이티브 CPU 표현 [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)를 사용하여 배정밀도로 표현됩니다. 이는 프로그래밍 언어 C 의 `double` 유형과 동일합니다.

> 정밀도 17 자리\
> 지수 -308 에서 308 까지

부동 소수점 숫자는 십진수를 표현할 때 정확하지 않다는 점에 유의하십시오.

```python
>>> a = 2.1 + 4.2
>>> a == 6.3
False
>>> a
6.300000000000001
>>>
```

이것은 **Python 문제가 아니라**, CPU 의 기본 부동 소수점 하드웨어 문제입니다.

일반적인 연산:

    x + y      더하기 (Add)
    x - y      빼기 (Subtract)
    x * y      곱하기 (Multiply)
    x / y      나누기 (Divide)
    x // y     정수 나누기 (Floor Divide)
    x % y      나머지 (Modulo)
    x ** y     거듭제곱 (Power)
    abs(x)     절댓값 (Absolute Value)

이들은 비트 연산자를 제외하고 정수와 동일한 연산자입니다. 추가 수학 함수는 `math` 모듈에서 찾을 수 있습니다.

```python
import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)
```
