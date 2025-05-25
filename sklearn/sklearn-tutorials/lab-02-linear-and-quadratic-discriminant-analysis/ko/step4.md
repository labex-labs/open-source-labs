# LDA 를 이용한 차원 축소 수행

LDA 는 지도 학습 차원 축소에도 사용될 수 있습니다. 이를 보여주기 위해 아이리스 데이터셋의 차원을 축소해 보겠습니다.

```python
from sklearn.datasets import load_iris

# 아이리스 데이터셋 로드
iris = load_iris()
X, y = iris.data, iris.target

# LDA 를 이용하여 차원 축소 수행
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
```
