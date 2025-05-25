# 모델 학습

Scikit-learn 의 `SVC` 클래스를 사용하여 SVM 모델을 학습합니다. 커널을 선형으로 설정하고, 정규화되지 않은 경우 페널티 매개변수 `C`를 1 로, 정규화된 경우 0.05 로 설정합니다. 그런 다음 모델의 계수와 절편을 사용하여 분리 초평면을 계산합니다.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```
