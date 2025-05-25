# 모델 생성

이 단계에서는 선형, 다항식, 그리고 방사 기저 함수 (RBF) 세 가지 다른 커널을 사용하는 SVM 모델을 생성합니다. 선형 커널은 선형적으로 분리 가능한 데이터 포인트에 사용되며, 다항식 및 RBF 커널은 비선형적으로 분리 가능한 데이터 포인트에 유용합니다.

```python
# 모델 학습
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
