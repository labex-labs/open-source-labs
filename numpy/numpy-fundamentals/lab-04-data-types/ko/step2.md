# 데이터 유형 작업

NumPy 데이터 유형은 `dtype` (data-type) 객체로 표현됩니다. `import numpy as np`를 사용하여 NumPy 를 가져온 후, `np.bool_`, `np.float32` 등을 사용하여 데이터 유형에 접근할 수 있습니다.

데이터 유형을 함수로 사용하여 Python 숫자를 배열 스칼라로, Python 숫자 시퀀스를 해당 유형의 배열로 변환하거나, 많은 NumPy 함수 또는 메서드의 `dtype` 키워드에 대한 인수로 사용할 수 있습니다. 다음은 몇 가지 예입니다.

```python
x = np.float32(1.0)
# x is now a float32 array scalar with value 1.0

y = np.int_([1,2,4])
# y is now an int array with values [1, 2, 4]

z = np.arange(3, dtype=np.uint8)
# z is now a uint8 array with values [0, 1, 2]
```

또한, dtype 객체를 사용하는 것이 권장되지만, 문자 코드를 사용하여 배열 유형을 참조할 수도 있습니다. 예를 들어:

```python
np.array([1, 2, 3], dtype='f')
# returns an array with values [1., 2., 3.] and dtype float32
```

배열의 유형을 변환하려면 `.astype()` 메서드 또는 유형 자체를 함수로 사용할 수 있습니다. 예를 들어:

```python
z.astype(float)
# returns the array z with dtype float64

np.int8(z)
# returns the array z with dtype int8
```
