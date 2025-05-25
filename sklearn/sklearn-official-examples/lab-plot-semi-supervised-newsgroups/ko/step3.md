# 지도 학습 모델 학습 및 평가

이 단계에서는 데이터셋을 학습용과 테스트용으로 분할하고, 2 단계에서 생성한 지도 학습 모델 파이프라인을 학습 및 평가합니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# 데이터셋을 학습용과 테스트용으로 분할
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 지도 학습 모델 파이프라인 학습 및 평가
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "테스트 세트에서의 마이크로 평균 F1 점수: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
