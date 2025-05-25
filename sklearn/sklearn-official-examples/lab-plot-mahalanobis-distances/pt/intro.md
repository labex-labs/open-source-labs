# Introdução

Neste laboratório, exploraremos o uso da estimativa robusta de covariância com distâncias de Mahalanobis em dados distribuídos gaussianamente. A distância de Mahalanobis é uma medida da distância entre um ponto e uma distribuição. É definida como a distância entre um ponto e a média da distribuição, escalonada pelo inverso da matriz de covariância da distribuição. Para dados distribuídos gaussianamente, a distância de Mahalanobis pode ser usada para calcular a distância de uma observação à moda da distribuição. Compararemos o desempenho do estimador Minimum Covariance Determinant (MCD), um estimador robusto de covariância, com o estimador padrão de máxima verossimilhança (MLE) de covariância no cálculo das distâncias de Mahalanobis de um conjunto de dados contaminado.

## Dicas da Máquina Virtual

Após o término do arranque da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
