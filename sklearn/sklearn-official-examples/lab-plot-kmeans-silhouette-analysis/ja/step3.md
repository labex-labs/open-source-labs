# 最適なクラスタ数を決定する

KMeans アルゴリズムの最適なクラスタ数を決定するために、シルエット法を使用します。`n_clusters` の値の範囲を反復し、各値に対するシルエットスコアをプロットします。

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # 1行2列のサブプロットを作成
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # 1つ目のサブプロットはシルエットプロット
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # 再現性のために、n_clusters の値と乱数生成器のシード値10でクラスタリングアルゴリズムを初期化
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # silhouette_score はすべてのサンプルの平均値を返す
    silhouette_avg = silhouette_score(X, cluster_labels)

    # 各サンプルのシルエットスコアを計算
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # クラスタ i に属するサンプルのシルエットスコアを集計し、ソート
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        ax1.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )

        # シルエットプロットの中央にクラスタ番号を付ける
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # 次のプロット用の新しい y_lower を計算
        y_lower = y_upper + 10  # 0 サンプル用の 10

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    # すべての値の平均シルエットスコアの垂直線
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # y 軸のラベル / 目盛りをクリア
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2番目のプロットは形成された実際のクラスタを表示
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # クラスタにラベルを付ける
    centers = clusterer.cluster_centers_
    # クラスタ中心に白い円を描く
    ax2.scatter(
        centers[:, 0],
        centers[:, 1],
        marker="o",
        c="white",
        alpha=1,
        s=200,
        edgecolor="k",
    )

    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker="$%d$" % i, alpha=1, s=50, edgecolor="k")

    ax2.set_title("The visualization of the clustered data.")
    ax2.set_xlabel("Feature space for the 1st feature")
    ax2.set_ylabel("Feature space for the 2nd feature")

    plt.suptitle(
        "Silhouette analysis for KMeans clustering on sample data with n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
