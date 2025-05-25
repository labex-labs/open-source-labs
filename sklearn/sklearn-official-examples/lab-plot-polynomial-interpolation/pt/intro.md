# Introdução

Neste laboratório, aprenderemos a aproximar uma função com polinómios até um determinado grau utilizando regressão de ridge. Apresentaremos duas formas diferentes de o fazer, dados `n_samples` de pontos 1D `x_i`:

1. `PolynomialFeatures`: gera todos os monómios até um grau especificado. Isto fornece-nos a matriz de Vandermonde com `n_samples` linhas e `degree + 1` colunas.
2. `SplineTransformer`: gera funções de base B-spline. Uma função de base de uma B-spline é uma função polinomial por partes de grau `degree` que é não nula apenas entre `degree+1` nós consecutivos.

Utilizaremos a função `make_pipeline` para adicionar características não lineares e mostrar como estes transformadores são adequados para modelar efeitos não lineares com um modelo linear. Desenvolveremos o gráfico da função, dos pontos de treino e da interpolação utilizando características polinomiais e B-splines. Também representaremos separadamente todas as colunas de ambos os transformadores e demonstraremos os nós da spline. Finalmente, demonstraremos o uso de splines periódicas.

## Dicas de Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para a prática.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente para si.
