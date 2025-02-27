# Interpretar los resultados

Podemos ver en la gráfica que `k-means++` tiene un buen desempeño tanto en cuanto al tiempo de inicialización bajo como al bajo número de iteraciones del GaussianMixture para converger. Cuando se inicializa con `random_from_data` o `random`, el modelo toma más iteraciones para converger. Los tres métodos alternativos toman menos tiempo para inicializar en comparación con `kmeans`.
