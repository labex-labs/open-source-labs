# Introdução

Este laboratório ilustra a aproximação do mapa de características de um kernel RBF usando RBFSampler e Nystroem para aproximar o mapa de características de um kernel RBF para classificação com uma SVM no conjunto de dados de dígitos. Os resultados usando uma SVM linear no espaço original, uma SVM linear usando as mapeamentos aproximados e usando uma SVM kernel são comparados. Os tempos de execução e a precisão para diferentes quantidades de amostras de Monte Carlo (no caso de RBFSampler, que usa recursos de Fourier aleatórios) e diferentes tamanhos de subconjuntos do conjunto de treinamento (para Nystroem) para o mapeamento aproximado são mostrados.

## Dicas da Máquina Virtual

Após o início da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário esperar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e nós resolveremos prontamente o problema para você.
