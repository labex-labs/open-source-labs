# 서포트 벡터 머신 (SVMs)

이 단계에서는 서포트 벡터 머신 (SVMs) 의 개념과 분류 작업에 어떻게 사용될 수 있는지 살펴봅니다. SVM 은 서로 다른 클래스의 데이터 포인트를 최대한 분리하는 초평면을 찾으려고 합니다.

#### 선형 SVM 생성 및 학습

```python
from sklearn import svm

svc = svm.SVC(kernel='linear')
svc.fit(iris_X_train, iris_y_train)
```

#### 서로 다른 커널을 사용한 SVM 생성 및 학습

```python
svc_poly = svm.SVC(kernel='poly', degree=3)
svc_rbf = svm.SVC(kernel='rbf')

svc_poly.fit(iris_X_train, iris_y_train)
svc_rbf.fit(iris_X_train, iris_y_train)
```
