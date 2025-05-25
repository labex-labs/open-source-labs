# 모델 학습

`svm` 라이브러리의 `SVC` 함수를 사용하여 모델을 학습하고 분리 초평면을 구합니다. 선형 커널을 사용하고 `C`를 1.0 으로 설정합니다.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
