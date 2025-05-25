# 분류 파이프라인

데이터셋에서 특징을 추출하고, 이들을 결합하여 결합된 특징 집합에 대한 분류기를 학습하는 파이프라인을 생성할 것입니다. Scikit-Learn 의 `Pipeline`과 `ColumnTransformer`를 사용하여 이를 달성할 것입니다.

```python
pipeline = Pipeline(
    [
        # 제목 및 본문 추출
        ("subjectbody", subject_body_transformer),
        # ColumnTransformer 를 사용하여 제목 및 본문 특징 결합
        (
            "union",
            ColumnTransformer(
                [
                    # 제목에 대한 bag-of-words (열 0)
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # 본문에 대한 bag-of-words 와 차원 축소 (열 1)
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
                    # 게시물 본문에서 텍스트 통계를 추출하는 파이프라인
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # 사전 -> 특징 행렬 변환
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # 사전 -> 특징 행렬 변환
                            ]
                        ),
                        1,
                    ),
                ],
                # 위 ColumnTransformer 특징의 가중치
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # 결합된 특징에 SVC 분류기 사용
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```
