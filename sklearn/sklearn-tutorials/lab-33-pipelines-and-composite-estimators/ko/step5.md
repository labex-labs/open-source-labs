# FeatureUnion - 복합 특징 공간

`FeatureUnion` 클래스는 여러 변환기 객체를 결합하여 출력을 결합하는 새로운 변환기로 결합하는 데 사용됩니다. 텍스트, 부동 소수점 및 날짜를 별도로 전처리하는 것과 같이 데이터의 서로 다른 특징에 서로 다른 변환을 적용하려는 경우 유용합니다. 변환기는 병렬로 적용되며, 출력하는 특징 행렬은 큰 행렬에 나란히 연결됩니다. 예제는 다음과 같습니다.

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```
