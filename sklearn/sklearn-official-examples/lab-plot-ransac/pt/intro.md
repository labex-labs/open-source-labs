# Introdução

Neste laboratório, demonstraremos como ajustar robustamente um modelo linear a dados com falhas utilizando o algoritmo RANSAC no scikit-learn. O regressor linear ordinário é sensível a valores discrepantes, e a linha ajustada pode facilmente ser desviada da verdadeira relação subjacente dos dados. O regressor RANSAC automaticamente divide os dados em inliers e outliers, e a linha ajustada é determinada apenas pelos inliers identificados. Usaremos o conjunto de dados `make_regression` do scikit-learn para gerar dados aleatórios com valores discrepantes e, em seguida, ajustaremos tanto um modelo linear quanto um regressor RANSAC aos dados.

## Dicas da Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para si.
