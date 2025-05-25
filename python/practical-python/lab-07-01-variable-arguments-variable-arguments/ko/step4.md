# 튜플 (Tuples) 과 딕셔너리 (Dicts) 전달하기

튜플은 가변 인자로 확장될 수 있습니다.

```python
numbers = (2,3,4)
f(1, *numbers)      # Same as f(1,2,3,4)
```

딕셔너리도 키워드 인자로 확장될 수 있습니다.

```python
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# Same as f(data, color='red', delimiter=',', width=400)
```
