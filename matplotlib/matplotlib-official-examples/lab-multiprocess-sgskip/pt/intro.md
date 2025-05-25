# Introdução

Neste laboratório, você aprenderá como usar a biblioteca `multiprocessing` e o Matplotlib para plotar dados gerados a partir de um processo separado. Criaremos duas classes - `ProcessPlotter` e `NBPlot` - para lidar com a plotagem e a geração de dados, respectivamente. A classe `NBPlot` gerará dados aleatórios e os enviará para a classe `ProcessPlotter` através de um pipe, que então plotará os dados em tempo real.

## Dicas para a VM

Após a inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** e acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos o problema prontamente para você.
