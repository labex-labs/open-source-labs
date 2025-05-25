# 기준 모델 설정

원본 특징에 대한 선형 SVM 을 학습하여 기준 모델을 설정하고 정확도를 출력합니다.

```python
from sklearn.svm import LinearSVC

# 원본 특징에 대한 선형 SVM 학습
lsvm = LinearSVC(dual="auto")
lsvm.fit(X_train, y_train)
lsvm_score = 100 * lsvm.score(X_test, y_test)

# 기준 모델의 정확도 출력
print(f"원본 특징에 대한 선형 SVM 점수: {lsvm_score:.2f}%")
```
