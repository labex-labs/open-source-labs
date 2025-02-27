# Drucke die Ergebnisse

Wir werden die Ergebnisse der besten Bicluster aus Schritt 8 ausgeben.

```python
for idx, cluster in enumerate(best_idx):
    n_rows, n_cols = cocluster.get_shape(cluster)
    cluster_docs, cluster_words = cocluster.get_indices(cluster)
    if not len(cluster_docs) or not len(cluster_words):
        continue

    # Kategorien
    counter = defaultdict(int)
    for i in cluster_docs:
        counter[document_names[i]] += 1
    cat_string = ", ".join(
        "{:.0f}% {}".format(float(c) / n_rows * 100, name)
        for name, c in most_common(counter)[:3]
    )

    # Wörter
    out_of_cluster_docs = cocluster.row_labels_!= cluster
    out_of_cluster_docs = np.where(out_of_cluster_docs)[0]
    word_col = X[:, cluster_words]
    word_scores = np.array(
        word_col[cluster_docs, :].sum(axis=0)
        - word_col[out_of_cluster_docs, :].sum(axis=0)
    )
    word_scores = word_scores.ravel()
    important_words = list(
        feature_names[cluster_words[i]] for i in word_scores.argsort()[:-11:-1]
    )

    print("bicluster {} : {} Dokumente, {} Wörter".format(idx, n_rows, n_cols))
    print("Kategorien   : {}".format(cat_string))
    print("Wörter        : {}\n".format(", ".join(important_words)))
```
