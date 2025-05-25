# Resumo

Neste laboratório, aprendemos como usar a biblioteca `multiprocessing` e Matplotlib para plotar dados gerados a partir de um processo separado. Criamos duas classes - `ProcessPlotter` e `NBPlot` - para lidar com a plotagem e a geração de dados, respectivamente. A classe `NBPlot` gerou dados aleatórios e os enviou para a classe `ProcessPlotter` através de um pipe, que então plotou os dados em tempo real.
