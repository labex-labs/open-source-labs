# Longest Item (가장 긴 항목)

`longest_item(*args)` 함수를 작성하세요. 이 함수는 임의의 수의 반복 가능한 객체 또는 length 속성을 가진 객체를 인수로 받아 가장 긴 객체를 반환합니다. 이 함수는 다음을 수행해야 합니다.

- `len()`을 `key`로 사용하여 `max()` 함수를 사용하여 가장 긴 길이를 가진 항목을 반환합니다.
- 여러 항목이 동일한 길이를 갖는 경우, 첫 번째 항목이 반환됩니다.

```python
def longest_item(*args):
  return max(args, key = len)
```

```python
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```
