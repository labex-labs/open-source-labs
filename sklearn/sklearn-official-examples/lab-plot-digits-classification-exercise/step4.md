# Train and test the K-Nearest Neighbors classifier

We will now train a K-Nearest Neighbors (KNN) classifier using scikit-learn's `KNeighborsClassifier` function and test it on the testing set. We will then print the accuracy score of the classifier.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
