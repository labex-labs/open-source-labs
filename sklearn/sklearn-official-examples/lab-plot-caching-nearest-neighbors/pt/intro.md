# Introdução

Este laboratório demonstra como pré-calcular os k vizinhos mais próximos antes de utilizá-los em KNeighborsClassifier. O KNeighborsClassifier pode calcular os vizinhos mais próximos internamente, mas pré-calculá-los pode apresentar várias vantagens, como um controlo mais preciso dos parâmetros, armazenamento em cache para múltiplos usos ou implementações personalizadas. Aqui, utilizamos a propriedade de armazenamento em cache de pipelines para armazenar em cache o grafo dos vizinhos mais próximos entre múltiplas adaptações de KNeighborsClassifier.

## Dicas de Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante a aprendizagem, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente.
