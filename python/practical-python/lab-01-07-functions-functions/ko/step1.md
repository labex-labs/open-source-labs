# 사용자 정의 함수 (Custom Functions)

재사용하려는 코드에는 함수를 사용하십시오. 다음은 함수 정의입니다.

```python
def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

함수를 호출하려면 다음과 같이 합니다.

```python
a = sumcount(100)
```

함수는 특정 작업을 수행하고 결과를 반환하는 일련의 문장입니다. `return` 키워드는 함수의 반환 값을 명시적으로 지정하는 데 필요합니다.
