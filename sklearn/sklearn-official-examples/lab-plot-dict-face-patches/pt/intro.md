# Introdução

Este laboratório demonstra como usar a API scikit-learn para processar um grande conjunto de dados de rostos e aprender um conjunto de patches de imagem de 20 x 20 que representam rostos. O aspecto chave deste laboratório é o uso de aprendizado online, onde carregamos e processamos imagens uma de cada vez e extraímos 50 patches aleatórios de cada imagem. Acumulamos 500 patches (de 10 imagens) e, em seguida, executamos o objeto KMeans online, o método partial_fit de MiniBatchKMeans.

## Dicas da Máquina Virtual

Após o término da inicialização da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para você.
