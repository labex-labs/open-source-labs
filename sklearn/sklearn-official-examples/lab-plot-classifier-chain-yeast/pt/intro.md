# Introdução

Este laboratório demonstra um exemplo de utilização de cadeias de classificadores num conjunto de dados multirótulo. O algoritmo de Cadeia de Classificadores é uma modificação do método de transformação de problemas para classificação multirótulo. Este método explora a correlação entre as classes construindo uma cadeia de classificadores binários. Cada modelo recebe as previsões dos modelos precedentes na cadeia como características. Usaremos o conjunto de dados `yeast`, que contém 2417 pontos de dados, cada um com 103 características e 14 rótulos possíveis. Cada ponto de dados tem pelo menos um rótulo. Como linha de base, primeiro treinamos um classificador de regressão logística para cada um dos 14 rótulos. Para avaliar o desempenho destes classificadores, prevemos num conjunto de teste reservado e calculamos a pontuação Jaccard para cada amostra.

## Dicas da Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante a aprendizagem, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
