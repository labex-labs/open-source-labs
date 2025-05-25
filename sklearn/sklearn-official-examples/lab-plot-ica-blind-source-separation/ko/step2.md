# ICA 및 PCA 모델 적합

독립적인 소스를 추정하기 위해 FastICA 를 사용합니다. 그런 다음 비교를 위해 PCA 를 계산합니다.

```python
from sklearn.decomposition import FastICA, PCA

# ICA 계산
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # 신호 재구성
A_ = ica.mixing_  # 추정된 혼합 행렬 가져오기

# ICA 모델이 적용되는지 확인하기 위해 역혼합을 통해 검증할 수 있습니다.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# 비교를 위해 PCA 계산
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # 직교 구성 요소 기반 신호 재구성
```
