# 연습 문제 7.10: 시간 측정을 위한 데코레이터

함수를 정의하면, 해당 함수의 이름과 모듈은 `__name__` 및 `__module__` 속성에 저장됩니다. 예를 들어:

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

`timethis.py` 파일에서, 함수가 실행되는 데 걸리는 시간을 출력하는 추가적인 로직 레이어로 함수를 감싸는 데코레이터 함수 `timethis(func)`를 작성하십시오. 이를 위해, 다음과 같이 시간 측정 호출로 함수를 감싸야 합니다:

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

다음은 데코레이터가 작동하는 방식의 예입니다:

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

토론: 이 `@timethis` 데코레이터는 모든 함수 정의 앞에 배치될 수 있습니다. 따라서 성능 튜닝을 위한 진단 도구로 사용할 수 있습니다.
