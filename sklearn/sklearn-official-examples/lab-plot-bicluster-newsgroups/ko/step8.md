# 최적의 이분 클러스터 찾기

정규화된 절단 값을 계산하여 최적의 이분 클러스터를 찾고, 상위 5 개를 선택합니다.

```python
feature_names = vectorizer.get_feature_names_out()
document_names = list(newsgroups.target_names[i] for i in newsgroups.target)

def bicluster_ncut(i):
    rows, cols = cocluster.get_indices(i)
    if not (np.any(rows) and np.any(cols)):
        import sys
        return sys.float_info.max
    row_complement = np.nonzero(np.logical_not(cocluster.rows_[i]))[0]
    col_complement = np.nonzero(np.logical_not(cocluster.columns_[i]))[0]
    weight = X[rows][:, cols].sum()
    cut = X[row_complement][:, cols].sum() + X[rows][:, col_complement].sum()
    return cut / weight

bicluster_ncuts = list(bicluster_ncut(i) for i in range(len(newsgroups.target_names)))
best_idx = np.argsort(bicluster_ncuts)[:5]
```
