# Pipeline de Classificação

Criaremos um pipeline que extrai características do conjunto de dados, as combina e treina um classificador no conjunto combinado de características. Usaremos o `Pipeline` e o `ColumnTransformer` do Scikit-Learn para isso.

```python
pipeline = Pipeline(
    [
        # Extrair assunto e corpo
        ("subjectbody", subject_body_transformer),
        # Usar ColumnTransformer para combinar as características de assunto e corpo
        (
            "union",
            ColumnTransformer(
                [
                    # vetorização bag-of-words para o assunto (coluna 0)
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # vetorização bag-of-words com decomposição para o corpo (coluna 1)
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
                    # Pipeline para extrair estatísticas de texto do corpo da mensagem
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # retorna uma lista de dicionários
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # lista de dicionários -> matriz de características
                            ]
                        ),
                        1,
                    ),
                ],
                # pesos das características do ColumnTransformer
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # Usar um classificador SVC nas características combinadas
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```
