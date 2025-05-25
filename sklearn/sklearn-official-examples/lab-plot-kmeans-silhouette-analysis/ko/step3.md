# 최적 클러스터 개수 결정

KMeans 알고리즘에 대한 최적 클러스터 개수를 결정하기 위해 실루엣 방법을 사용합니다. `n_clusters` 값의 범위를 반복하여 각 값에 대한 실루엣 점수를 플롯합니다.

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # 1 행 2 열의 서브플롯 생성
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # 첫 번째 서브플롯은 실루엣 플롯
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # n_clusters 값과 재현성을 위해 10 의 랜덤 생성자 시드를 사용하여 클러스터러 초기화
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # silhouette_score 는 모든 샘플에 대한 평균 값을 제공합니다.
    silhouette_avg = silhouette_score(X, cluster_labels)

    # 각 샘플에 대한 실루엣 점수 계산
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # 클러스터 i 에 속하는 샘플의 실루엣 점수를 집계하고 정렬
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

        # 중앙에 실루엣 플롯에 클러스터 번호 레이블 표시
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # 다음 플롯을 위한 새로운 y_lower 계산
        y_lower = y_upper + 10  # 0 샘플에 대한 10

    ax1.set_title("다양한 클러스터에 대한 실루엣 플롯.")
    ax1.set_xlabel("실루엣 계수 값")
    ax1.set_ylabel("클러스터 레이블")

    # 모든 값의 평균 실루엣 점수에 대한 수직선
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # y 축 레이블/눈금 제거
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 형성된 실제 클러스터를 보여주는 2 번째 플롯
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # 클러스터 레이블 표시
    centers = clusterer.cluster_centers_
    # 클러스터 중심에 흰색 원 그리기
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

    ax2.set_title("클러스터된 데이터 시각화.")
    ax2.set_xlabel("첫 번째 특성에 대한 특성 공간")
    ax2.set_ylabel("두 번째 특성에 대한 특성 공간")

    plt.suptitle(
        "n_clusters = %d에 대한 샘플 데이터의 KMeans 클러스터링에 대한 실루엣 분석"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
