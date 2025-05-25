# 정수를 로마 숫자로 변환하기

1 에서 3999 사이의 정수 `num`을 입력받아 로마 숫자 표현을 문자열로 반환하는 함수 `to_roman_numeral(num)`을 작성하십시오.

정수를 로마 숫자 표현으로 변환하려면 (로마 값, 정수) 형식의 튜플을 포함하는 조회 목록 (lookup list) 을 사용할 수 있습니다. 그런 다음 `for` 루프를 사용하여 조회 목록의 값을 반복하고 `divmod()`를 사용하여 `num`을 나머지로 업데이트하고 로마 숫자 표현을 결과에 추가할 수 있습니다.

함수는 입력 정수의 로마 숫자 표현을 반환해야 합니다.

```python
def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
