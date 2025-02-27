# Оценка модели

Чтобы оценить производительность нашей модели, мы можем использовать отдельный тестовый набор данных. Мы можем загрузить тестовый набор данных с использованием того же процесса, что и для тренировочного набора.

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

Теперь мы можем предобработать тестовый набор и извлечь векторы признаков.

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

Наконец, мы можем использовать нашу обученную модель для предсказаний на тестовом наборе и вычислить точность.

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```
