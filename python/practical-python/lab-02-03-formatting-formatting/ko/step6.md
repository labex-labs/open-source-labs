# 연습 문제 2.8: 숫자를 서식 지정하는 방법

숫자를 출력할 때 흔히 발생하는 문제는 소수점 자릿수를 지정하는 것입니다. 이를 해결하는 한 가지 방법은 f-string 을 사용하는 것입니다. 다음 예제를 시도해 보세요.

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```

f-string 에서 사용되는 서식 코드에 대한 전체 문서는 [여기](https://docs.python.org/3/library/string.html#format-specification-mini-language)에서 찾을 수 있습니다. 서식 지정은 문자열의 `%` 연산자를 사용하여 수행되기도 합니다.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

`%`와 함께 사용되는 다양한 코드에 대한 문서는 [여기](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)에서 찾을 수 있습니다.

`print`와 함께 자주 사용되지만, 문자열 서식 지정은 출력에만 국한되지 않습니다. 서식이 지정된 문자열을 저장하려면 변수에 할당하기만 하면 됩니다.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```
