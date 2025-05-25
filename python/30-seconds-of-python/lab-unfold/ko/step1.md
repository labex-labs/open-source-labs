# Unfold 리스트

귀하의 과제는 이터레이터 함수와 초기 시드 값을 인수로 사용하는 `unfold` 함수를 구현하는 것입니다. 이터레이터 함수는 하나의 인수 (`seed`) 를 받으며, 항상 두 개의 요소 ([`value`, `nextSeed`]) 를 가진 리스트를 반환하거나 종료하기 위해 `False`를 반환해야 합니다. `unfold` 함수는 `while` 루프를 사용하여 이터레이터 함수를 호출하고 `value`를 `False`를 반환할 때까지 `yield`하는 제너레이터 함수 `fn_generator`를 사용해야 합니다. 마지막으로, `unfold` 함수는 리스트 컴프리헨션 (list comprehension) 을 사용하여 이터레이터 함수를 사용하여 제너레이터에 의해 생성된 리스트를 반환해야 합니다.

`unfold` 함수를 구현하십시오:

```python
def unfold(fn, seed):
    # your code here
```

### 입력

- 하나의 인수 (`seed`) 를 받으며, 항상 두 개의 요소 ([`value`, `nextSeed`]) 를 가진 리스트를 반환하거나 종료하기 위해 `False`를 반환해야 하는 이터레이터 함수 `fn`.
- 초기 시드 값 `seed`.

### 출력

- 이터레이터 함수를 사용하여 제너레이터에 의해 생성된 리스트.

```python
def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

```python
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
```
