# 16 진수에서 RGB 변환

문자열로 된 16 진수 색상 코드를 입력받아 해당 RGB 구성 요소에 해당하는 정수 튜플을 반환하는 함수 `hex_to_rgb(hex_code)`를 작성하십시오. 이 함수는 다음 단계를 수행해야 합니다.

1. 리스트 컴프리헨션 (list comprehension) 을 `int()` 및 리스트 슬라이스 표기법과 함께 사용하여 16 진수 문자열에서 RGB 구성 요소를 가져옵니다.
2. `tuple()`을 사용하여 결과 리스트를 튜플로 변환합니다.

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
