# Introdução

A detecção de novidades e de valores discrepantes são técnicas utilizadas para identificar se uma nova observação pertence à mesma distribuição que as observações existentes ou se deve ser considerada diferente. Estas técnicas são frequentemente utilizadas para limpar conjuntos de dados reais, identificando observações anormais ou incomuns.

Existem duas distinções importantes neste contexto:

1. Detecção de valores discrepantes: Os dados de treino contêm valores discrepantes, que são observações que estão distantes das outras. Os estimadores de detecção de valores discrepantes tentam ajustar as regiões onde os dados de treino estão mais concentrados, ignorando as observações desviantes.
2. Detecção de novidades: Os dados de treino não estão contaminados por valores discrepantes, e o objetivo é detectar se uma nova observação é um valor discrepante. Neste contexto, um valor discrepante também é chamado de novidade.

O projeto scikit-learn fornece um conjunto de ferramentas de aprendizagem de máquina que podem ser utilizadas para detecção de novidades e de valores discrepantes. Estas ferramentas são implementadas utilizando algoritmos de aprendizagem não supervisionada, o que significa que aprendem padrões dos dados sem a necessidade de exemplos rotulados.

## Dicas de Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Por vezes, pode ser necessário esperar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante a aprendizagem, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
