# Introdução

Neste laboratório, utilizaremos o conjunto de dados Ames Housing para comparar diferentes métodos de lidar com características categóricas em estimadores de Gradient Boosting. O conjunto de dados contém características numéricas e categóricas, e a variável-alvo é o preço de venda das casas. Compararemos o desempenho de quatro pipelines diferentes:

- Remover as características categóricas
- Codificação one-hot das características categóricas
- Tratar as características categóricas como valores ordinais
- Utilizar o suporte nativo para características categóricas no estimador Gradient Boosting

Avaliaremos os pipelines em termos de seus tempos de ajuste e desempenho de previsão usando validação cruzada.

## Dicas da Máquina Virtual

Após o arranque da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para si.
