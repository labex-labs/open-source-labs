# Introdução

Em aprendizagem de máquina, frequentemente avaliamos o desempenho de um modelo de classificação usando uma pontuação. No entanto, também precisamos testar a significância da pontuação para garantir que o desempenho do modelo não seja apenas por acaso. É aqui que entra o teste de permutação de pontuação. Ele gera uma distribuição nula calculando a precisão do classificador em 1000 permutações diferentes do conjunto de dados. Um valor p empírico é então calculado como a percentagem de permutações para as quais a pontuação obtida é maior que a pontuação obtida usando os dados originais. Neste laboratório, usaremos a função `permutation_test_score` de `sklearn.model_selection` para avaliar a significância de uma pontuação validada cruzadamente usando permutações.

## Dicas da Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante a aprendizagem, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
