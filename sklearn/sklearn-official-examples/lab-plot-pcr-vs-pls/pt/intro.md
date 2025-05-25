# Introdução

A Regressão de Componentes Principais (PCR) e a Regressão de Mínimos Quadrados Parciais (PLS) são dois métodos utilizados na análise de regressão. A PCR envolve a aplicação da PCA aos dados de treino, seguida do treino de um regressor nas amostras transformadas. A transformação PCA é não supervisionada, o que significa que nenhuma informação sobre as variáveis-alvo é utilizada. Como resultado, a PCR pode ter um desempenho fraco em alguns conjuntos de dados onde a variável-alvo está fortemente correlacionada com direções que têm baixa variância.

A PLS é simultaneamente um transformador e um regressor, e é bastante semelhante à PCR. Também aplica uma redução de dimensionalidade às amostras antes de aplicar um regressor linear aos dados transformados. A principal diferença em relação à PCR é que a transformação PLS é supervisionada. Portanto, não sofre do problema mencionado acima.

Neste laboratório, vamos comparar a PCR e a PLS num conjunto de dados de exemplo.

## Dicas da Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
