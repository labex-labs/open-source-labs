# Determinar o Número Ótimo de Clusters

Usaremos o Método Silhouette para determinar o número ótimo de clusters para o algoritmo KMeans. Irá iterar através de um intervalo de valores para `n_clusters` e plotar as pontuações silhouette para cada valor.

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Cria um subplot com 1 linha e 2 colunas
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # O primeiro subplot é o gráfico silhouette
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Inicializa o clusterer com o valor n_clusters e uma semente aleatória
    # de 10 para reprodutibilidade.
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # A silhouette_score fornece o valor médio para todas as amostras.
    silhouette_avg = silhouette_score(X, cluster_labels)

    # Calcula as pontuações silhouette para cada amostra
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Agrega as pontuações silhouette para amostras pertencentes ao
        # cluster i e ordena-as
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

        # Rótula os gráficos silhouette com os seus números de cluster no meio
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Calcula o novo y_lower para o próximo gráfico
        y_lower = y_upper + 10  # 10 para as amostras 0

    ax1.set_title("O gráfico silhouette para os vários clusters.")
    ax1.set_xlabel("Valores do coeficiente silhouette")
    ax1.set_ylabel("Etiqueta do cluster")

    # A linha vertical para a pontuação silhouette média de todos os valores
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Limpa as etiquetas/marcas do eixo y
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2º Gráfico mostrando os clusters reais formados
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # Rotulando os clusters
    centers = clusterer.cluster_centers_
    # Desenha círculos brancos nos centros dos clusters
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

    ax2.set_title("Visualização dos dados agrupados.")
    ax2.set_xlabel("Espaço de características para a 1ª característica")
    ax2.set_ylabel("Espaço de características para a 2ª característica")

    plt.suptitle(
        "Análise Silhouette para agrupamento KMeans em dados de amostra com n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
