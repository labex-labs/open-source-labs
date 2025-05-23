# 기본 인덱싱

NumPy 배열은 표준 Python 구문 `x[obj]`를 사용하여 인덱싱할 수 있습니다. 여기서 `x`는 배열이고 `obj`는 선택 항목입니다. `obj`의 유형에 따라 다양한 종류의 인덱싱을 사용할 수 있습니다.

## 단일 요소 인덱싱

단일 요소 인덱싱은 다른 표준 Python 시퀀스에 대한 인덱싱과 정확히 동일하게 작동합니다. 0 부터 시작하며, 배열의 끝에서부터 인덱싱하기 위해 음수 인덱스를 허용합니다.

```python
x = np.arange(10)
print(x[2])  # Output: 2
print(x[-2])  # Output: 8
```

## 다차원 인덱싱

배열은 여러 차원을 가질 수 있으며, 각 차원에 대해 동일한 방식으로 인덱싱이 작동합니다. 각 차원의 인덱스를 쉼표로 구분하여 다차원 배열의 요소에 액세스할 수 있습니다.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Output: 8
print(x[1, -1])  # Output: 9
```

## 하위 차원 배열 인덱싱

다차원 배열을 차원보다 적은 인덱스로 인덱싱하면 하위 차원 배열을 얻게 됩니다. 지정된 각 인덱스는 선택된 나머지 차원에 해당하는 배열을 선택합니다.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Output: [0, 1, 2, 3, 4]
```
