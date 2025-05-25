# Introdução

Neste laboratório, exploraremos como a complexidade do modelo influencia tanto a precisão da previsão quanto o desempenho computacional. Usaremos dois conjuntos de dados - o Conjunto de Dados de Diabetes para regressão e o Conjunto de Dados 20newsgroups para classificação. Modelaremos a influência da complexidade em três estimadores diferentes:

- SGDClassifier (para dados de classificação), que implementa o aprendizado de descida de gradiente estocástico
- NuSVR (para dados de regressão), que implementa a regressão de vetores de suporte Nu
- GradientBoostingRegressor constrói um modelo aditivo de forma progressiva em estágios

Variar-emos a complexidade do modelo através da escolha de parâmetros de modelo relevantes em cada um dos modelos selecionados. Em seguida, mediremos a influência no desempenho computacional (latência) e no poder preditivo (MSE ou Hamming Loss).

## Dicas da Máquina Virtual

Após o início da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para você.
