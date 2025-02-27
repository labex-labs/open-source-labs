# 評価指標

生成されたクラスタの品質を定量化するために、評価指標を使用することができます。同質性、完全性、V尺度、調整ランド指数、調整相互情報、およびシルエット係数指標を使用します。これらの指標はsklearn.metricsモジュールからアクセスします。真のラベルがわからない場合、評価はモデル結果自体を使用してのみ行うことができます。その場合、シルエット係数が役に立ちます。

```python
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Adjusted Mutual Information: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")
```
