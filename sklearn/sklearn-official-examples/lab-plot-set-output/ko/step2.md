# DataFrame 출력을 위한 변환기 설정

`preprocessing.StandardScaler`와 같은 추정기를 DataFrame 을 반환하도록 설정하려면 `set_output`를 호출합니다.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().set_output(transform="pandas")

scaler.fit(X_train)
X_test_scaled = scaler.transform(X_test)
X_test_scaled.head()
```
