# Interpréter les résultats

On peut voir sur le tracé que `k-means++` est performant tant en termes de temps d'initialisation faible qu'en termes de nombre d'itérations du GaussianMixture pour converger. Lorsqu'il est initialisé avec `random_from_data` ou `random`, le modèle prend plus d'itérations pour converger. Les trois autres méthodes alternatives prennent moins de temps pour s'initialiser par rapport à `kmeans`.
