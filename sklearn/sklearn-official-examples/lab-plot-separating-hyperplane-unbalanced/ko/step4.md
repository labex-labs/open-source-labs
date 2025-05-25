# 가중치 클래스로 모델 학습

`svm` 라이브러리의 `SVC` 함수를 사용하여 모델을 학습하고 분리 초평면을 구합니다. 선형 커널을 사용하고 `class_weight`를 `{1: 10}`으로 설정합니다. 이렇게 하면 작은 클래스에 더 많은 가중치를 부여합니다.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```
