# 데이터 로드

먼저, scikit-learn 에서 숫자 데이터셋을 로드합니다. 이 데이터셋에는 0 부터 9 까지의 숫자를 나타내는 8x8 이미지가 포함되어 있습니다. 주성분 분석 (PCA) 을 사용하여 데이터셋의 차원을 15 로 줄일 것입니다.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# 숫자 데이터셋 로드
digits = load_digits()

# PCA 를 사용하여 데이터셋의 차원을 15 로 줄임
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```
