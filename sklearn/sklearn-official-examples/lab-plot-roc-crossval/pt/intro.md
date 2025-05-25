# Introdução

Neste laboratório, aprenderemos a estimar e visualizar a variância da métrica Receiver Operating Characteristic (ROC) usando validação cruzada em Python. As curvas ROC são usadas na classificação binária para medir o desempenho de um modelo, plotando a taxa de verdadeiros positivos (TPR) contra a taxa de falsos positivos (FPR). Usaremos a biblioteca Scikit-learn para carregar o conjunto de dados iris, criar recursos ruidosos e classificar o conjunto de dados com a Máquina de Vetores de Suporte (SVM). Em seguida, plotaremos as curvas ROC com validação cruzada e calcularemos a média da Área Sob a Curva (AUC) para ver a variabilidade da saída do classificador quando o conjunto de treinamento é dividido em diferentes subconjuntos.

## Dicas da Máquina Virtual

Após o término do inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para você.
