# 인덱싱된 배열에 값 할당하기 (Assigning Values to Indexed Arrays)

인덱싱을 사용하여 배열의 특정 요소 또는 요소의 하위 집합에 값을 할당할 수 있습니다. 할당되는 값은 인덱싱된 배열과 형태 (shape) 가 일치해야 합니다.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Output: [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Output: [0, 1, 0, 1, 2, 3, 7, 8, 9]
```
