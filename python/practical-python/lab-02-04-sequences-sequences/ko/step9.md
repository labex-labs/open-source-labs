# enumerate() 함수

`enumerate` 함수는 반복에 추가적인 카운터 값을 추가합니다.

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # Loops with i = 0, name = 'Elwood'
    # i = 1, name = 'Jake'
    # i = 2, name = 'Curtis'
```

일반적인 형태는 `enumerate(sequence [, start = 0])`입니다. `start`는 선택 사항입니다. `enumerate()`를 사용하는 좋은 예는 파일을 읽는 동안 줄 번호를 추적하는 것입니다.

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        ...
```

결론적으로, `enumerate`는 다음의 간편한 단축키입니다.

```python
i = 0
for x in s:
    statements
    i += 1
```

`enumerate`를 사용하면 타이핑이 줄어들고 약간 더 빠르게 실행됩니다.
