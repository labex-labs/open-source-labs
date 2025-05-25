# MissingIndicator 를 이용한 임퓨테이션 값 표시

`MissingIndicator` 변환기는 데이터 세트에서 누락된 값의 존재를 나타내는 데 유용합니다. 임퓨테이션과 함께 사용하여 어떤 값이 임퓨테이션되었는지에 대한 정보를 보존하는 데 사용할 수 있습니다. 이 변환기는 데이터 세트에서 누락된 값의 존재를 나타내는 이진 행렬을 반환합니다.

```python
from sklearn.impute import MissingIndicator
X = np.array([[-1, -1, 1, 3], [4, -1, 0, -1], [8, -1, 1, 0]])
indicator = MissingIndicator()
mask_missing_values_only = indicator.fit_transform(X)
```
