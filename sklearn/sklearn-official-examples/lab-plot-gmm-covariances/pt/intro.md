# Introdução

Este tutorial demonstra o uso de diferentes tipos de covariância para modelos de mistura gaussiana (GMMs). Os GMMs são frequentemente usados para agrupamento, e podemos comparar os clusters obtidos com as classes reais do conjunto de dados. Inicializamos as médias das gaussianas com as médias das classes do conjunto de treinamento para tornar esta comparação válida. Plotamos as etiquetas previstas nos dados de treinamento e nos dados de teste mantidos de fora usando uma variedade de tipos de covariância GMM no conjunto de dados iris. Comparamos GMMs com matrizes de covariância esférica, diagonal, completa e ligada em ordem crescente de desempenho.

Embora se espere que a covariância completa tenha melhor desempenho em geral, ela é propensa a superajuste em conjuntos de dados pequenos e não generaliza bem para dados de teste mantidos de fora.

Nos gráficos, os dados de treinamento são mostrados como pontos, enquanto os dados de teste são mostrados como cruzes. O conjunto de dados iris é quadridimensional. Apenas as duas primeiras dimensões são mostradas aqui, e portanto alguns pontos são separados em outras dimensões.

## Dicas de Máquina Virtual

Após o término do inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário esperar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos prontamente o problema para você.
