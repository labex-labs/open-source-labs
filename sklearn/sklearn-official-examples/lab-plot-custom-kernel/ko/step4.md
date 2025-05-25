# SVM 분류기 생성

이 단계에서는 SVM 분류기의 인스턴스를 생성하고 데이터를 맞춥니다. 이전 단계에서 생성한 사용자 지정 커널을 사용합니다.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```
