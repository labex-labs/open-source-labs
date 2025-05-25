# 클러스터링 알고리즘 학습

이 단계에서는 생성된 학습 데이터에 클러스터링 알고리즘을 학습시켜 클러스터 레이블을 얻습니다. scikit-learn 의 `AgglomerativeClustering`을 사용하여 3 개의 클러스터로 알고리즘을 학습시킵니다.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
