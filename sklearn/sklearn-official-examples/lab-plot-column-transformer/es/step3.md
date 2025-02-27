# Pipeline de clasificación

Crearemos una pipeline que extraiga características del conjunto de datos, las combine y entrene un clasificador en el conjunto combinado de características. Usaremos `Pipeline` y `ColumnTransformer` de Scikit-Learn para lograr esto.

```python
pipeline = Pipeline(
    [
        # Extraer asunto y cuerpo
        ("subjectbody", subject_body_transformer),
        # Usar ColumnTransformer para combinar las características del asunto y el cuerpo
        (
            "union",
            ColumnTransformer(
                [
                    # bolsa de palabras para el asunto (col 0)
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # bolsa de palabras con descomposición para el cuerpo (col 1)
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
                    # Pipeline para extraer estadísticas de texto del cuerpo del mensaje
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # devuelve una lista de diccionarios
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # lista de diccionarios -> matriz de características
                            ]
                        ),
                        1,
                    ),
                ],
                # peso sobre las características de ColumnTransformer
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # Usar un clasificador SVC en las características combinadas
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```
