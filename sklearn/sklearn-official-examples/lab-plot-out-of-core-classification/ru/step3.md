# Настраиваем векторизатор и выделяем тестовую выборку

```python
# Создаем векторизатор и ограничиваем количество признаков до разумного
# максимума
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# Итератор по разобранным файлам Reuters в формате SGML.
data_stream = stream_reuters_documents()

# Мы обучаем бинарную классификацию между классом "acq" и всеми остальными.
# "acq" был выбран, так как он более - менее равномерно распределен в файлах Reuters.
# Для других датасетов нужно убедиться, что тестовая выборка содержит
# реальный процент положительных инстансов.
all_classes = np.array([0, 1])
positive_class = "acq"

# Вот некоторые классификаторы, которые поддерживают метод `partial_fit`
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive - Aggressive": PassiveAggressiveClassifier(),
}

# Статистика по тестовым данным
test_stats = {"n_test": 0, "n_test_pos": 0}

# Во - первых, мы выделяем некоторое количество примеров для оценки точности
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("Тестовая выборка состоит из %d документов (%d положительных)" % (len(y_test), sum(y_test)))
```
