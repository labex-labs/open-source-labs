# 데이터셋 및 모델

붓꽃 (iris) 데이터셋과 선형 SVC 분류기를 사용하여 두 종류의 붓꽃을 구분하는 방법을 보여줍니다. 먼저 필요한 라이브러리를 가져오고 데이터셋을 로드합니다.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = load_iris(return_X_y=True)
```

다음으로, 데이터셋에 노이즈 특징을 추가하고 학습 및 테스트 세트로 분할합니다.

```python
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X[y < 2], y[y < 2], test_size=0.5, random_state=random_state
)
```

마지막으로, `StandardScaler`를 사용하여 데이터를 스케일링하고 선형 SVC 분류기를 학습 데이터에 맞춥니다.

```python
classifier = make_pipeline(
    StandardScaler(), LinearSVC(random_state=random_state, dual="auto")
)
classifier.fit(X_train, y_train)
```
