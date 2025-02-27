# Bestimme die optimale Anzahl von Clustern

Wir werden die Silhouettenmethode verwenden, um die optimale Anzahl von Clustern für den KMeans-Algorithmus zu bestimmen. Wir werden durch einen Bereich von Werten für `n_clusters` iterieren und die Silhouettenwerte für jeden Wert plotten.

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Erzeuge ein Subplot mit 1 Zeile und 2 Spalten
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # Der erste Subplot ist der Silhouettenplot
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Initialisiere den Clusterer mit dem n_clusters-Wert und einem Zufallszahlengenerator
    # mit dem Seed 10 für Wiederholbarkeit.
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # Der Silhouettenwert gibt den Durchschnittswert für alle Proben an.
    silhouette_avg = silhouette_score(X, cluster_labels)

    # Berechne die Silhouettenwerte für jede Probe
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Aggregiere die Silhouettenwerte für Proben, die zu
        # Cluster i gehören, und sortiere sie
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

        # Belege die Silhouettenplots mit ihren Clusternummern in der Mitte
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Berechne den neuen y_lower für den nächsten Plot
        y_lower = y_upper + 10  # 10 für die 0 Proben

    ax1.set_title("Der Silhouettenplot für die verschiedenen Cluster.")
    ax1.set_xlabel("Die Silhouettenkoeffizientenwerte")
    ax1.set_ylabel("Clusterbezeichnung")

    # Die vertikale Linie für den durchschnittlichen Silhouettenwert aller Werte
    ax1.axvline(x=silhouette_avg, color="rot", linestyle="--")

    ax1.set_yticks([])  # Lösche die y-Achsenbeschriftungen / -markierungen
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # Zweiter Plot, der die tatsächlich gebildeten Cluster zeigt
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # Belege die Cluster
    centers = clusterer.cluster_centers_
    # Zeichne weiße Kreise in den Clusterzentren
    ax2.scatter(
        centers[:, 0],
        centers[:, 1],
        marker="o",
        c="weiß",
        alpha=1,
        s=200,
        edgecolor="k",
    )

    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker="$%d$" % i, alpha=1, s=50, edgecolor="k")

    ax2.set_title("Die Visualisierung der gruppierten Daten.")
    ax2.set_xlabel("Feature-Raum für das erste Feature")
    ax2.set_ylabel("Feature-Raum für das zweite Feature")

    plt.suptitle(
        "Silhouettenanalyse für KMeans-Clustering auf Beispiel-Daten mit n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
