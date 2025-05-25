# 평균 (Average)

두 개 이상의 숫자를 입력받아 그 평균을 반환하는 `average`라는 함수를 작성하십시오. 함수는 다음 지침을 따라야 합니다.

- 제공된 모든 `args`의 합을 구하기 위해 `sum()`을 사용하고, `len()`으로 나눕니다.
- 함수는 임의의 수의 인수를 처리할 수 있어야 합니다.
- 함수는 float 를 반환해야 합니다.

```python
def average(*args):
  return sum(args, 0.0) / len(args)
```

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
