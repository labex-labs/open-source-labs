# 딕셔너리 조회

키의 존재 여부를 테스트할 수 있습니다.

```python
if key in d:
    # YES
else:
    # NO
```

존재하지 않을 수 있는 값을 조회하고, 존재하지 않는 경우 기본값을 제공할 수 있습니다.

```python
name = d.get(key, default)
```

예시:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
