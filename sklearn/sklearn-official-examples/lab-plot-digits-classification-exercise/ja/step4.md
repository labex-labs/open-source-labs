# K近傍法（K-Nearest Neighbors）分類器を学習とテストする

ここでは、scikit-learnの`KNeighborsClassifier`関数を使ってK近傍法（KNN）分類器を学習し、テストセットでテストします。その後、分類器の精度スコアを表示します。

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
