# 未知のインスタンスのクラスタ所属を予測する

このステップでは、帰納的学習モデルを使って、生成した新しいサンプルのクラスタ所属を予測します。`InductiveClusterer`クラスの`predict`関数を使い、新しいサンプルとそのおそらくのクラスタをプロットします。

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```
