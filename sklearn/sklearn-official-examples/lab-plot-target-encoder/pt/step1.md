# Carregamento de Dados do OpenML

Primeiro, carregamos o conjunto de dados de avaliações de vinho usando a função `fetch_openml` do módulo `scikit-learn.datasets`. Usaremos apenas um subconjunto de características numéricas e categóricas nos dados. Usaremos o seguinte subconjunto de características numéricas e categóricas nos dados: `numerical_features = ["price"]` e `categorical_features = ["country", "province", "region_1", "region_2", "variety", "winery"]`.
