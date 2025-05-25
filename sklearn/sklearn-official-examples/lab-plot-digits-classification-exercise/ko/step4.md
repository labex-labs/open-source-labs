# K-최근접 이웃 분류기를 학습 및 테스트

이제 scikit-learn 의 `KNeighborsClassifier` 함수를 사용하여 K-최근접 이웃 (KNN) 분류기를 학습하고 테스트 세트에서 테스트합니다. 그런 다음 분류기의 정확도 점수를 출력합니다.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
