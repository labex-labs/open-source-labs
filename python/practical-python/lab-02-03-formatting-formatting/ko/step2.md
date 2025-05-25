# 서식 코드 (Format codes)

서식 코드 ( `{}` 안의 `:` 뒤) 는 C 의 `printf()`와 유사합니다. 일반적인 코드는 다음과 같습니다.

```code
d       Decimal integer
b       Binary integer
x       Hexadecimal integer
f       Float as [-]m.dddddd
e       Float as [-]m.dddddde+-xx
g       Float, but selective use of E notation
s       String
c       Character (from integer)
```

일반적인 수정자는 필드 너비와 소수점 정밀도를 조정합니다. 다음은 부분 목록입니다.

```code
:>10d   Integer right aligned in 10-character field
:<10d   Integer left aligned in 10-character field
:^10d   Integer centered in 10-character field
:0.2f   Float with 2 digit precision
```
