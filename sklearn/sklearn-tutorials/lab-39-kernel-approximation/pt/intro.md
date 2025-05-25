# Introdução

Este tutorial guiará você pelo processo de utilização de técnicas de aproximação de kernel em scikit-learn.

Métodos de kernel, como máquinas de vetores de suporte (SVM), são técnicas poderosas para classificação não linear. Esses métodos dependem do conceito de uma função kernel que mapeia dados de entrada para um espaço de características de alta dimensão. No entanto, trabalhar com mapeamentos explícitos de características pode ser computacionalmente caro, especialmente para conjuntos de dados grandes. Métodos de aproximação de kernel fornecem uma solução gerando aproximações de baixa dimensão do espaço de características do kernel.

Neste tutorial, exploraremos várias técnicas de aproximação de kernel disponíveis em scikit-learn, incluindo o método Nystroem, aproximação de kernel Radial Basis Function (RBF), aproximação de kernel Additive Chi Squared (ACS), aproximação de kernel Skewed Chi Squared (SCS) e aproximação de kernel polinomial usando Tensor Sketch. Demonstraremos como utilizar essas técnicas e discutiremos suas vantagens e limitações.

## Dicas de Máquina Virtual

Após o término da inicialização da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação de operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para você.
