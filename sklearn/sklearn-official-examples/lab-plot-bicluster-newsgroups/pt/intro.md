# Introdução

Neste laboratório, utilizaremos o algoritmo de Co-agrupamento Espectral no conjunto de dados de 20 grupos de notícias para biclustering dos documentos. O conjunto de dados possui 20 categorias de documentos e excluiremos a categoria "comp.os.ms-windows.misc", pois contém mensagens sem dados. As mensagens vetorizadas usando TF-IDF formam uma matriz de frequência de palavras, que é então biclusterizada usando o algoritmo de Co-agrupamento Espectral de Dhillon. Os biclusters resultantes documento-palavra indicam subconjuntos de palavras usadas com mais frequência nesses subconjuntos de documentos. Também agruparemos os documentos usando MiniBatchKMeans para comparação.

## Dicas da Máquina Virtual

Após o arranque da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
