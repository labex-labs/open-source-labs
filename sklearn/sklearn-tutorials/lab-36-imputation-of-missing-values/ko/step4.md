# KNNImputer 를 이용한 최근접 이웃 임퓨테이션

`KNNImputer` 클래스는 k-최근접 이웃 접근 방식을 사용하여 누락된 값을 채우는 임퓨테이션을 제공합니다. 누락된 값이 있는 각 샘플에 대한 최근접 이웃을 찾고, 이웃의 값을 기반으로 누락된 특징 값을 임퓨테이션합니다.

```python
from sklearn.impute import KNNImputer
nan = np.nan
X = [[1, 2, nan], [3, 4, 3], [nan, 6, 5], [8, 8, 7]]
imputer = KNNImputer(n_neighbors=2)
imputed_X = imputer.fit_transform(X)
```
