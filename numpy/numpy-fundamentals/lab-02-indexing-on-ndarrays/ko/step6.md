# 평탄화된 이터레이터 인덱싱 (Flat Iterator Indexing)

`x.flat` 속성은 C-연속 스타일로 전체 배열을 반복하는 데 사용할 수 있는 이터레이터 (iterator) 를 반환합니다. 이 이터레이터는 기본 슬라이싱 (slicing) 또는 고급 인덱싱을 사용하여 인덱싱할 수도 있습니다.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Output: [1, 2, 3, 4]
```
