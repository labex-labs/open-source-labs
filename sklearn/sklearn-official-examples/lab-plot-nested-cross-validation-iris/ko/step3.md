# 모델 정의

반경 기저 함수 (radial basis function) 커널을 사용하는 서포트 벡터 분류기를 사용합니다.

```python
from sklearn.svm import SVC

# "rbf" 커널을 사용하는 서포트 벡터 분류기를 사용합니다.
svm = SVC(kernel="rbf")
```
