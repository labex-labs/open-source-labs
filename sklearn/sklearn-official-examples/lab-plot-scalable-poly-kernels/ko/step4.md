# 커널 기반 SVM 모델 설정

커널의 성능을 PolynomialCountSketch 가 얼마나 잘 근사하는지 확인하기 위해 커널 기반 SVM 을 학습합니다.

```python
from sklearn.svm import SVC

# 커널 기반 SVM 학습
ksvm = SVC(C=500.0, kernel="poly", degree=4, coef0=0, gamma=1.0)
ksvm.fit(X_train, y_train)
ksvm_score = 100 * ksvm.score(X_test, y_test)

# 커널 기반 SVM 의 정확도 출력
print(f"원본 특징에 대한 커널-SVM 점수: {ksvm_score:.2f}%")
```
