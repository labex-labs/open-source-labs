# 데이터 로드 및 준비

scikit-learn 에서 와인 데이터셋을 로드하고 학습 및 테스트 데이터셋으로 분할합니다. 또한 scikit-learn 전처리 모듈의 StandardScaler 를 사용하여 학습 데이터셋의 특징을 스케일링합니다.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_wine(return_X_y=True, as_frame=True)
scaler = StandardScaler().set_output(transform="pandas")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
scaled_X_train = scaler.fit_transform(X_train)
```
