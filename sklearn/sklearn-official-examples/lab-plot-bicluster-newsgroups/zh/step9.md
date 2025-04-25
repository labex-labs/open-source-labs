# 打印结果

我们将打印在步骤 8 中找到的最佳双聚类的结果。

```python
for idx, cluster in enumerate(best_idx):
    n_rows, n_cols = cocluster.get_shape(cluster)
    cluster_docs, cluster_words = cocluster.get_indices(cluster)
    if not len(cluster_docs) or not len(cluster_words):
        continue

    # 类别
    counter = defaultdict(int)
    for i in cluster_docs:
        counter[document_names[i]] += 1
    cat_string = ", ".join(
        "{:.0f}% {}".format(float(c) / n_rows * 100, name)
        for name, c in most_common(counter)[:3]
    )

    # 单词
    不在聚类中的文档 = cocluster.row_labels_!= cluster
    不在聚类中的文档 = np.where(不在聚类中的文档)[0]
    单词列 = X[:, cluster_words]
    单词得分 = np.array(
        单词列[cluster_docs, :].sum(axis=0)
        - 单词列[不在聚类中的文档, :].sum(axis=0)
    )
    单词得分 = 单词得分.ravel()
    重要单词 = list(
        feature_names[cluster_words[i]] for i in word_scores.argsort()[:-11:-1]
    )

    print("双聚类 {} : {} 个文档，{} 个单词".format(idx, n_rows, n_cols))
    print("类别   : {}".format(cat_string))
    print("单词   : {}\n".format(", ".join(重要单词)))
```
