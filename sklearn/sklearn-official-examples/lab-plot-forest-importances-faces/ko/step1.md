# 데이터 로드 및 모델 적합

Olivetti 얼굴 데이터셋을 로드하고 데이터셋을 첫 5 개 클래스만 포함하도록 제한합니다. 그런 다음 데이터셋에 랜덤 포레스트를 학습하고 불순도 기반의 특징 중요도를 평가합니다. 작업에 사용할 코어 수를 설정합니다.

```python
from sklearn.datasets import fetch_olivetti_faces

# 병렬적으로 포레스트 모델을 적합하는 데 사용할 코어 수를 선택합니다.
# `-1` 은 사용 가능한 모든 코어를 사용함을 의미합니다.
n_jobs = -1

# 얼굴 데이터셋을 로드합니다.
data = fetch_olivetti_faces()
X, y = data.data, data.target

# 데이터셋을 5 개 클래스로 제한합니다.
mask = y < 5
X = X[mask]
y = y[mask]

# 특징 중요도를 계산하기 위해 랜덤 포레스트 분류기를 적합합니다.
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
