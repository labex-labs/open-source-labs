# Определение оптимального числа кластеров

Мы будем использовать метод силуэта для определения оптимального числа кластеров для алгоритма KMeans. Мы будем перебирать диапазон значений для `n_clusters` и строить графики значений силуэта для каждого значения.

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Создаем подграфик с 1 строкой и 2 столбцами
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # Первый подграфик - это график силуэта
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Инициализируем кластеризатор значением n_clusters и случайным
    # генератором случайных чисел с семенем 10 для воспроизводимости.
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # Функция silhouette_score возвращает среднее значение для всех образцов.
    silhouette_avg = silhouette_score(X, cluster_labels)

    # Вычисляем значения силуэта для каждого образца
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Агрегируем значения силуэта для образцов, принадлежащих
        # кластеру i, и сортируем их
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

        # Метка графиков силуэта их номерами кластеров посередине
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Вычисляем новое y_lower для следующего графика
        y_lower = y_upper + 10  # 10 для 0 образцов

    ax1.set_title("График силуэта для различных кластеров.")
    ax1.set_xlabel("Значения коэффициента силуэта")
    ax1.set_ylabel("Номер кластера")

    # Вертикальная линия для среднего значения силуэта для всех значений
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Очищаем метки и деления по оси y
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # Второй график показывает фактически образованные кластеры
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # Метка кластеров
    centers = clusterer.cluster_centers_
    # Рисуем белые круги в центрах кластеров
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

    ax2.set_title("Визуализация сгруппированных данных.")
    ax2.set_xlabel("Пространство признаков для первого признака")
    ax2.set_ylabel("Пространство признаков для второго признака")

    plt.suptitle(
        "Анализ силуэта для кластеризации KMeans на выборочных данных с n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
