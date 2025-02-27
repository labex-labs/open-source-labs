# Обучение модели

Теперь, когда у нас есть векторы признаков, мы можем обучить модель для классификации текстовых данных. В этом примере мы будем использовать алгоритм Multinomial Naive Bayes, который является популярным алгоритмом для классификации текста.

```python
from sklearn.naive_bayes import MultinomialNB

# Train the model
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

Теперь наша модель обучена и готова к предсказанию.
