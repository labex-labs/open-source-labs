# 주성분 분석 (PCA)

#### 정확한 PCA 와 확률적 해석

주성분 분석 (PCA) 는 다변량 데이터를 최대 분산을 설명하는 연속적인 직교 성분 집합으로 분해하는 데 사용됩니다. PCA 는 scikit-learn 의 `PCA` 클래스를 사용하여 구현할 수 있습니다. `fit` 메서드는 성분을 학습하는 데 사용되고, `transform` 메서드는 새로운 데이터를 이러한 성분에 투영하는 데 사용할 수 있습니다.

```python
from sklearn.decomposition import PCA

# 원하는 성분의 수를 n_components 로 설정한 PCA 객체 생성
pca = PCA(n_components=2)

# PCA 모델을 데이터에 맞춤
pca.fit(data)

# 학습된 성분에 데이터를 투영하여 변환
transformed_data = pca.transform(data)
```
