# Introdução

O Gradiente Descendente Estocástico é uma técnica de otimização popular usada para minimizar uma função de perda. A técnica executa passos de descida de gradiente de forma estocástica, ou seja, selecionando aleatoriamente amostras para cada iteração. O método é eficiente, especialmente para ajustar modelos lineares. No entanto, a convergência não é garantida em cada iteração, e a função de perda pode não diminuir necessariamente em cada iteração. Neste caso, monitorar a convergência na função de perda pode ser difícil. Neste laboratório, exploraremos a estratégia de parada antecipada, que é uma abordagem para monitorar a convergência em uma pontuação de validação. Usaremos o modelo `SGDClassifier` da biblioteca scikit-learn e o conjunto de dados MNIST para ilustrar como a parada antecipada pode ser usada para atingir quase a mesma precisão em comparação com um modelo construído sem parada antecipada, e reduzir significativamente o tempo de treinamento.

## Dicas da Máquina Virtual

Após o início da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário esperar alguns segundos para que o Jupyter Notebook termine de carregar. A validação de operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos prontamente o problema para você.
