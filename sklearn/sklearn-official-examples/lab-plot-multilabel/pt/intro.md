# Introdução

Este laboratório demonstra um problema de classificação de documentos multi-rótulo utilizando o scikit-learn. O conjunto de dados é gerado aleatoriamente com base no seguinte processo:

- Escolher o número de rótulos: n ~ Poisson(n_labels)
- N vezes, escolher uma classe c: c ~ Multinomial(theta)
- Escolher o comprimento do documento: k ~ Poisson(length)
- K vezes, escolher uma palavra: w ~ Multinomial(theta_c)

Neste processo, a amostragem por rejeição é utilizada para garantir que n seja maior que 2 e que o comprimento do documento nunca seja zero. Da mesma forma, as classes que já foram escolhidas são rejeitadas. Os documentos que são atribuídos a ambas as classes são plotados rodeados por dois círculos coloridos.

## Dicas da Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante a aprendizagem, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para si.
