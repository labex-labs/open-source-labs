# Treinar e testar o classificador K-Vizinhos Mais Próximos

Agora, treinaremos um classificador K-Vizinhos Mais Próximos (KNN) usando a função `KNeighborsClassifier` do scikit-learn e testaremos-o no conjunto de teste. Em seguida, imprimiremos a pontuação de precisão do classificador.

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```
