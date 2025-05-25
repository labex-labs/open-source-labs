# SVM 분류기 설정

RBF(Radial Basis Function) 커널을 사용한 SVM 분류기를 설정합니다. SVM 은 지도 학습 알고리즘으로 데이터를 서로 다른 클래스로 분리하는 최적의 초평면을 찾습니다.

```python
from sklearn.svm import SVC

# SVM 분류기 설정
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "RBF 커널을 사용한 SVC")
```
