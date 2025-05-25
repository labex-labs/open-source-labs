# 모델 학습

이 단계에서는 생성된 데이터를 사용하여 RBF 커널을 가진 SVM 분류기를 학습합니다.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
