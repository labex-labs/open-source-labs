# LDA 구현

다음으로, scikit-learn 의 `LinearDiscriminantAnalysis` 클래스를 사용하여 LDA 를 구현합니다. 세 가지 분류기를 생성합니다.

- 축소 없이 LDA
- Ledoit-Wolf 축소를 사용한 LDA
- OAS 축소를 사용한 LDA

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.covariance import OAS

clf1 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage=None)
clf2 = LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")
oa = OAS(store_precision=False, assume_centered=False)
clf3 = LinearDiscriminantAnalysis(solver="lsqr", covariance_estimator=oa)
```
