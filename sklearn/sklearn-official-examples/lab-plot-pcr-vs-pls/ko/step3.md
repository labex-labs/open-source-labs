# 회귀자 생성

두 개의 회귀자 (PCR 및 PLS) 를 생성합니다. 이 예시에서는 구성 요소 수를 1 로 설정합니다. PCR 의 PCA 단계에 데이터를 입력하기 전에 권장되는 사례에 따라 데이터를 표준화합니다. PLS 추정기는 내장된 스케일링 기능을 가지고 있습니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

pcr = make_pipeline(StandardScaler(), PCA(n_components=1), LinearRegression())
pcr.fit(X_train, y_train)
pca = pcr.named_steps["pca"]  # retrieve the PCA step of the pipeline

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```
