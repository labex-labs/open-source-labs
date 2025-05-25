# 타이 브레이킹 유무에 따른 SVM 모델 생성

이 단계에서는 타이 브레이킹을 비활성화한 SVM 모델과 활성화한 SVM 모델을 각각 생성합니다. scikit-learn 의 `SVC` 클래스를 사용하여 이러한 모델을 생성합니다. 두 모델에 대해 `break_ties` 매개변수는 각각 `False`와 `True`로 설정됩니다.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```
