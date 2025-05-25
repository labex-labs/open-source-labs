# Interpretar os resultados

Podemos observar no gráfico que o método `k-means++` apresenta um bom desempenho, tanto em tempo de inicialização baixo quanto em um baixo número de iterações do GaussianMixture para convergir. Quando inicializado com `random_from_data` ou `random`, o modelo leva mais iterações para convergir. Todos os três métodos alternativos levam menos tempo para inicializar em comparação com o `kmeans`.
