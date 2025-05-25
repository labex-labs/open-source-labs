# SVM 모델 학습

다음으로, 선형 커널과 규제 매개변수 1000 을 사용하여 SVM 모델을 데이터셋에 적합시킵니다. scikit-learn 의 `svm.SVC()` 함수를 사용하여 SVM 분류기를 생성합니다.

```python
from sklearn import svm

# SVM 모델 학습
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```
