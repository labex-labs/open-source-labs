# 시퀀스 데이터 타입 (Sequence Datatypes)

Python 에는 세 가지 _시퀀스_ 데이터 타입이 있습니다.

- 문자열 (String): `'Hello'`. 문자열은 문자들의 시퀀스입니다.
- 리스트 (List): `[1, 4, 5]`.
- 튜플 (Tuple): `('GOOG', 100, 490.1)`.

모든 시퀀스는 정렬되어 있으며, 정수로 인덱싱되고, 길이를 갖습니다.

```python
a = 'Hello'               # String
b = [1, 4, 5]             # List
c = ('GOOG', 100, 490.1)  # Tuple

# Indexed order
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Length of sequence
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3
```

시퀀스는 반복될 수 있습니다: `s * n`.

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

같은 타입의 시퀀스는 연결될 수 있습니다: `s + t`.

```python
>>> a = (1, 2, 3)
>>> b = (4, 5)
>>> a + b
(1, 2, 3, 4, 5)
>>>
>>> c = [1, 5]
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "list") to tuple
```
