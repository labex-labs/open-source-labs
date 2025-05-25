# 머신러닝 모델 학습

이제 데이터셋을 준비했으므로 학습 데이터를 사용하여 머신러닝 모델을 학습시킬 수 있습니다. 이 예제에서는 서포트 벡터 머신 (SVM) 알고리즘을 사용합니다.

```python
from sklearn.svm import SVC

# SVM 분류기를 생성
clf = SVC(kernel='linear')

# 학습 데이터로 분류기를 학습
clf.fit(X_train, y_train)
```
