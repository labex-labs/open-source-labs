# 고급 인덱싱 (Advanced Indexing)

고급 인덱싱은 선택 객체 `obj`가 튜플이 아닌 시퀀스 객체, ndarray(정수 또는 부울 데이터 유형) 또는 하나 이상의 시퀀스 객체 또는 ndarray(정수 또는 부울 데이터 유형) 를 포함하는 튜플인 경우 트리거됩니다. 고급 인덱싱에는 정수 인덱싱과 부울 인덱싱의 두 가지 유형이 있습니다.

## 정수 배열 인덱싱

정수 배열 인덱싱을 사용하면 N 차원 인덱스를 기반으로 배열에서 임의의 항목을 선택할 수 있습니다. 각 정수 배열은 해당 차원에 대한 여러 인덱스를 나타냅니다.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Output: [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Output: [7, 7, 4, 2]
```

## 부울 배열 인덱싱

부울 배열 인덱싱을 사용하면 부울 조건을 기반으로 배열 요소를 선택할 수 있습니다. 결과는 부울 배열의 `True` 값에 해당하는 요소만 포함하는 새 배열입니다.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Output: [ 1., 19., 18., 3.]
```
