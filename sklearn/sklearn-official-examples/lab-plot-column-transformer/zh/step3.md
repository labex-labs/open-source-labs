# 分类管道

我们将创建一个管道，该管道从数据集中提取特征，将它们组合起来，并在组合后的特征集上训练一个分类器。我们将使用 Scikit-Learn 的 `Pipeline` 和 `ColumnTransformer` 来实现这一点。

```python
pipeline = Pipeline(
    [
        # 提取主题和正文
        ("subjectbody", subject_body_transformer),
        # 使用ColumnTransformer组合主题和正文特征
        (
            "union",
            ColumnTransformer(
                [
                    # 主题（第0列）的词袋模型
                    ("subject", TfidfVectorizer(min_df=50), 0),
                    # 正文（第1列）的带分解的词袋模型
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
                    # 从帖子正文中提取文本统计信息的管道
                    (
                        "body_stats",
                        Pipeline(
                            [
                                (
                                    "stats",
                                    text_stats_transformer,
                                ),  # 返回一个字典列表
                                (
                                    "vect",
                                    DictVectorizer(),
                                ),  # 字典列表 -> 特征矩阵
                            ]
                        ),
                        1,
                    ),
                ],
                # 上述ColumnTransformer特征的权重
                transformer_weights={
                    "subject": 0.8,
                    "body_bow": 0.5,
                    "body_stats": 1.0,
                },
            ),
        ),
        # 在组合特征上使用SVC分类器
        ("svc", LinearSVC(dual=False)),
    ],
    verbose=True,
)
```
