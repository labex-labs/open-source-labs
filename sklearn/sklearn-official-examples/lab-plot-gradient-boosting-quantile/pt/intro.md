# Introdução

Este laboratório demonstra como usar regressão quantile para criar intervalos de previsão usando o scikit-learn. Vamos gerar dados sintéticos para um problema de regressão, aplicar a função a eles e criar observações do alvo usando uma distribuição lognormal. Em seguida, dividiremos os dados em conjuntos de treinamento e teste, ajustaremos regressores quantile não lineares e de mínimos quadrados e criaremos um conjunto de avaliação com valores de entrada espaçados uniformemente, abrangendo a faixa [0, 10]. Compararemos a mediana prevista com a média prevista, analisaremos as métricas de erro e calibraremos o intervalo de confiança. Finalmente, ajustaremos os hiperparâmetros dos regressores quantile.

## Dicas da Máquina Virtual

Após o término do inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você encontrar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para você.
