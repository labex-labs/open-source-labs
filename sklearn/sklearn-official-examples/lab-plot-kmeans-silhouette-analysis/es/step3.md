# Determinar el número óptimo de clusters

Usaremos el Método Silueta para determinar el número óptimo de clusters para el algoritmo KMeans. Iteraremos a través de una serie de valores para `n_clusters` y graficaremos las puntuaciones de silueta para cada valor.

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Crea un subgráfico con 1 fila y 2 columnas
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # El primer subgráfico es la gráfica de silueta
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Inicializa el clusterizador con el valor de n_clusters y una semilla
    # aleatoria de 10 para la reproducibilidad.
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # La puntuación de silueta da el valor promedio para todas las muestras.
    silhouette_avg = silhouette_score(X, cluster_labels)

    # Calcula las puntuaciones de silueta para cada muestra
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Agrupa las puntuaciones de silueta para las muestras pertenecientes a
        # el cluster i, y las ordena
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

        # Etiqueta las gráficas de silueta con sus números de cluster en el centro
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Calcula el nuevo y_lower para la siguiente gráfica
        y_lower = y_upper + 10  # 10 para las 0 muestras

    ax1.set_title("La gráfica de silueta para los diversos clusters.")
    ax1.set_xlabel("Los valores del coeficiente de silueta")
    ax1.set_ylabel("Etiqueta de cluster")

    # La línea vertical para la puntuación de silueta promedio de todos los valores
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Limpia las etiquetas / marcas del eje y
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # Segunda gráfica que muestra los clusters reales formados
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # Etiquetando los clusters
    centers = clusterer.cluster_centers_
    # Dibuja círculos blancos en los centros de los clusters
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

    ax2.set_title("La visualización de los datos agrupados.")
    ax2.set_xlabel("Espacio de características para la primera característica")
    ax2.set_ylabel("Espacio de características para la segunda característica")

    plt.suptitle(
        "Análisis de silueta para el clustering KMeans en datos de muestra con n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
