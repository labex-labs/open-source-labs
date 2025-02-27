# Klassifizierungspipeline

Wir werden eine Pipeline erstellen, die Features aus dem Dataset extrahiert, kombiniert und einen Klassifizierer auf der kombinierten Featuremenge trainiert. Wir werden dazu Scikit-Learn's `Pipeline` und `ColumnTransformer` verwenden.

```python
pipeline = Pipeline(
    [
        # Extract subject & body
        ("subjectbody", subject_body_transformer),
        # Use ColumnTransformer to combine the subject and body features
        (
            "union",
            ColumnTransformer(
                [
                    # bag-of-words for subject (col 0)
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # bag-of-words with decomposition for body (col 1)
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
                    # Pipeline for pulling text stats from post's body
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # returns a list of dicts
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # list of dicts -> feature matrix
                            ]
                        ),
                        1,
                    ),
                ],
                # weight above ColumnTransformer features
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # Use a SVC classifier on the combined features
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```
