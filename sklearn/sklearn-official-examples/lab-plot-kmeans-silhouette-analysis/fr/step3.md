# Déterminer le nombre optimal de grappes

Nous utiliserons la méthode de silhouette pour déterminer le nombre optimal de grappes pour l'algorithme KMeans. Nous allons itérer sur une plage de valeurs pour `n_clusters` et tracer les scores de silhouette pour chaque valeur.

```python
range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Crée un sous-graphique avec 1 ligne et 2 colonnes
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # Le premier sous-graphique est le graphique de silhouette
    ax1.set_xlim([-0.1, 1])
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Initialise le clusterer avec la valeur de n_clusters et un générateur
    # de graines aléatoires de 10 pour la reproductibilité.
    clusterer = KMeans(n_clusters=n_clusters, n_init="auto", random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # Le silhouette_score donne la valeur moyenne pour tous les échantillons.
    silhouette_avg = silhouette_score(X, cluster_labels)

    # Calcule les scores de silhouette pour chaque échantillon
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Agrège les scores de silhouette pour les échantillons appartenant à
        # au cluster i, et les trie
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

        # Affiche les numéros de cluster au milieu des graphiques de silhouette
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Calcule la nouvelle y_lower pour le prochain graphique
        y_lower = y_upper + 10  # 10 pour les 0 échantillons

    ax1.set_title("Le graphique de silhouette pour les différents clusters.")
    ax1.set_xlabel("Les valeurs du coefficient de silhouette")
    ax1.set_ylabel("Étiquette de cluster")

    # La ligne verticale pour le score de silhouette moyen de toutes les valeurs
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Efface les étiquettes / les repères de l'axe y
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2ème graphique montrant les grappes réelles formées
    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(
        X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
    )

    # Étiquetage des grappes
    centers = clusterer.cluster_centers_
    # Dessine des cercles blancs au centre des grappes
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

    ax2.set_title("La visualisation des données regroupées.")
    ax2.set_xlabel("Espace de caractéristiques pour la première caractéristique")
    ax2.set_ylabel("Espace de caractéristiques pour la deuxième caractéristique")

    plt.suptitle(
        "Analyse de silhouette pour le regroupement KMeans sur des données d'échantillonnage avec n_clusters = %d"
        % n_clusters,
        fontsize=14,
        fontweight="bold",
    )

plt.show()
```
