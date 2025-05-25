# 최소값의 키

딕셔너리 `d`를 인수로 받아 딕셔너리에서 최소값을 가진 키를 반환하는 함수 `key_of_min(d)`를 작성하십시오.

이 문제를 해결하기 위해, `dict.get()`으로 설정된 `key` 매개변수와 함께 내장 함수 `min()`을 사용할 수 있습니다. 이렇게 하면 딕셔너리에서 최소값을 가진 키가 반환됩니다.

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
