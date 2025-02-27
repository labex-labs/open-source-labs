# Линейка классификации

Мы создадим линейку, которая извлекает признаки из набора данных, объединяет их и обучает классификатор на объединенном наборе признаков. Для этого мы используем `Pipeline` и `ColumnTransformer` из Scikit-Learn.

```python
pipeline = Pipeline(
    [
        # Извлечение темы и тела
        ("subjectbody", subject_body_transformer),
        # Использование ColumnTransformer для объединения признаков темы и тела
        (
            "union",
            ColumnTransformer(
                [
                    # мешок слов для темы (колонка 0)
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # мешок слов с декомпозицией для тела (колонка 1)
                    (
                        "body_bow",
                        Pipeline(
                            [
                                ("tfidf", TfidfVectorizer()),
                                ("best", TruncatedSVD(n_components=50)),
                            ]
                        ),
                        1,
                    ),
                    # Линейка для извлечения статистик текста из тела поста
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # возвращает список словарей
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # список словарей -> матрица признаков
                            ]
                        ),
                        1,
                    ),
                ],
                # веса для признаков выше ColumnTransformer
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # Использование классификатора SVC на объединенных признаках
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```
