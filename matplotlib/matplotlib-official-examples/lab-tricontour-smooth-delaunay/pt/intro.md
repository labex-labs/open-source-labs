# Introdução

Este tutorial demonstra como gerar gráficos de tricontorno de alta resolução com Matplotlib. Tricontorno (tricontouring) é uma técnica utilizada para representar dados em uma malha triangular não estruturada. É frequentemente utilizada quando os dados são coletados em pontos espaçados irregularmente, ou quando os dados são inerentemente triangulares por natureza. O tutorial mostrará como gerar um conjunto aleatório de pontos, realizar uma triangulação de Delaunay nesses pontos, mascarar alguns dos triângulos na malha, refinar e interpolar os dados e, finalmente, plotar os dados refinados usando a função `tricontour` do Matplotlib.

## Dicas para a VM

Após a inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** e acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido às limitações do Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos o problema prontamente para você.
