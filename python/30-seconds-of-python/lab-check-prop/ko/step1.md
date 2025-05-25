# 속성 확인

`check_prop`이라는 함수를 생성합니다. 이 함수는 두 개의 매개변수 `fn`과 `prop`을 받습니다. `fn` 매개변수는 딕셔너리의 지정된 속성에 적용될 술어 함수 (predicate function) 입니다. `prop` 매개변수는 술어 함수가 적용될 속성의 이름을 나타내는 문자열입니다.

`check_prop` 함수는 딕셔너리를 입력으로 받아 지정된 속성에 술어 함수 `fn`을 적용하는 람다 함수 (lambda function) 를 반환해야 합니다.

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
