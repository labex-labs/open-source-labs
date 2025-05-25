# 독립 성분 분석 (ICA)

#### 맹검 소스 분리에 사용되는 ICA

독립 성분 분석 (ICA) 는 혼합된 신호를 원래의 소스 성분으로 분리하는 데 사용됩니다. ICA 는 성분들이 통계적으로 독립적이며 선형 혼합 해제 과정을 통해 추출될 수 있다고 가정합니다. ICA 는 scikit-learn 의 `FastICA` 클래스를 사용하여 구현할 수 있습니다.

```python
from sklearn.decomposition import FastICA

# 원하는 성분의 수를 n_components 로 설정한 ICA 객체 생성
ica = FastICA(n_components=2)

# 혼합 신호에 ICA 모델을 맞춤
ica.fit(mixed_signals)

# 혼합 신호를 원래 소스 성분으로 분리
source_components = ica.transform(mixed_signals)
```
