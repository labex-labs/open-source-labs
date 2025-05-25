# 해밍 거리 (Hamming Distance)

두 정수를 인수로 받아 해밍 거리를 반환하는 함수 `hamming_distance(a, b)`를 작성하십시오. 이 함수는 다음 단계를 수행해야 합니다.

1. XOR 연산자 (`^`) 를 사용하여 두 숫자 간의 비트 차이를 찾습니다.
2. `bin()`을 사용하여 결과를 이진 문자열로 변환합니다.
3. 문자열을 리스트로 변환하고 `str` 클래스의 `count()`를 사용하여 문자열 내의 `1`의 수를 세어 반환합니다.

```python
def hamming_distance(a, b):
  return bin(a ^ b).count('1')
```

```python
hamming_distance(2, 3) # 1
```
