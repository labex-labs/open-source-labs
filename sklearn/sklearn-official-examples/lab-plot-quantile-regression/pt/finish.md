# Resumo

Neste tutorial, aprendemos como realizar regressão de quantis usando o scikit-learn. Geramos dois conjuntos de dados sintéticos para ilustrar como a regressão de quantis pode prever quantis condicionais não triviais. Usamos a classe `QuantileRegressor` para estimar a mediana, bem como um quantil baixo e um quantil alto fixados em 5% e 95%, respectivamente. Comparamos `QuantileRegressor` com `LinearRegression` e avaliamos seu desempenho usando o erro absoluto médio (MAE) e o erro quadrático médio (MSE).
