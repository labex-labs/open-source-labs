# Introdução

Este tutorial demonstrará como realizar regressão por quantis usando o scikit-learn. Geraremos dois conjuntos de dados sintéticos para ilustrar como a regressão por quantis pode prever quantis condicionais não triviais. Usaremos a classe `QuantileRegressor` para estimar a mediana, bem como um quantil baixo e um quantil alto fixados em 5% e 95%, respectivamente. Compararemos `QuantileRegressor` com `LinearRegression` e avaliaremos seu desempenho usando o erro absoluto médio (MAE) e o erro quadrático médio (MSE).

## Dicas da Máquina Virtual

Após o término da inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para você.
