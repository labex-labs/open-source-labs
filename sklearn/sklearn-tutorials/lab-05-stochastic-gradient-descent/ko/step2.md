# 데이터 로드 및 전처리

다음으로, iris 데이터셋을 로드하고 StandardScaler 를 사용하여 특징을 스케일링하여 전처리합니다.

```python
# iris 데이터셋 로드
iris = load_iris()
X, y = iris.data, iris.target

# 특징 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 데이터를 학습 및 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```
