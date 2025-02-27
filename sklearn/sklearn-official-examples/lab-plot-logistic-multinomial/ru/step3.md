# Обучение модели многонаправленной логистической регрессии

Теперь мы обучим модель многонаправленной логистической регрессии с использованием функции `LogisticRegression` из scikit-learn. Мы установим решатель в `"sag"`, максимальное количество итераций в 100, случайное состояние в 42 и параметр многоклассовой классификации в `"multinomial"`. Затем мы выведем оценку обучения модели.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
