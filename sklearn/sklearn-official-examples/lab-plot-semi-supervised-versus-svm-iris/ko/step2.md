# 레이블 확산 분류기 설정

다양한 레이블 데이터 비율 (30%, 50%, 100%) 을 가진 세 개의 레이블 확산 분류기를 설정합니다. 레이블 확산은 레이블이 지정된 데이터 포인트에서 레이블이 지정되지 않은 데이터 포인트로 유사성을 기반으로 레이블을 전파하는 반지도 학습 알고리즘입니다.

```python
from sklearn.semi_supervised import LabelSpreading

# 레이블 확산 분류기 설정
rng = np.random.RandomState(0)
y_rand = rng.rand(y.shape[0])
y_30 = np.copy(y)
y_30[y_rand < 0.3] = -1  # 임의의 샘플을 레이블이 없는 것으로 설정
y_50 = np.copy(y)
y_50[y_rand < 0.5] = -1
ls30 = (LabelSpreading().fit(X, y_30), y_30, "레이블 확산 30% 데이터")
ls50 = (LabelSpreading().fit(X, y_50), y_50, "레이블 확산 50% 데이터")
ls100 = (LabelSpreading().fit(X, y), y, "레이블 확산 100% 데이터")
```
