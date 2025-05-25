# 딕셔너리에서 값의 키 찾기

제공된 딕셔너리에서 주어진 값을 가진 첫 번째 키를 찾는 함수 `find_key(dict, val)`을 작성하십시오.

함수는 다음을 수행해야 합니다.

- 딕셔너리 `dict`와 값 `val`을 입력으로 받습니다.
- `dictionary.items()`와 `next()`를 사용하여 값이 `val`과 같은 첫 번째 키를 반환합니다.
- 키를 출력으로 반환합니다.

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
