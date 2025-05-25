# 숫자를 범위에 매핑하기

`num_to_range`라는 함수를 작성하세요. 이 함수는 `num`, `inMin`, `inMax`, `outMin`, `outMax`의 다섯 개의 인수를 받습니다. 이 함수는 `inMin`-`inMax` 범위의 `num`을 `outMin`-`outMax` 범위로 매핑하여 반환해야 합니다. 즉, 이 함수는 특정 범위 (`inMin`-`inMax`) 내에 있는 숫자 (`num`) 를 가져와 새로운 범위 (`outMin`-`outMax`) 로 매핑해야 합니다.

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
