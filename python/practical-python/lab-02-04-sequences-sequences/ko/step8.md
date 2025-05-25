# 정수 반복 (Looping over integers)

카운트가 필요한 경우, `range()`를 사용하십시오.

```python
for i in range(100):
    # i = 0,1,...,99
```

구문은 `range([start,] end [,step])`입니다.

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Notice how it counts in steps of 2, not 1.
```

- 종료 값은 절대 포함되지 않습니다. 슬라이스의 동작을 미러링합니다.
- `start`는 선택 사항입니다. 기본값은 `0`입니다.
- `step`은 선택 사항입니다. 기본값은 `1`입니다.
- `range()`는 필요에 따라 값을 계산합니다. 실제로 많은 수의 숫자를 저장하지 않습니다.
