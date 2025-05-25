# explode 함수 정의

다음으로, NumPy 로고의 복셀 이미지를 업스케일링하는 데 사용될 `explode`라는 함수를 정의합니다. 이 함수는 NumPy 배열을 입력으로 받아 입력 배열의 두 배 크기인 새로운 NumPy 배열을 반환합니다.

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
