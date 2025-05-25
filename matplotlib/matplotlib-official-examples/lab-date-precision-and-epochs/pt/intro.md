# Introdução

Este é um laboratório passo a passo que demonstra como lidar com a precisão de datas e épocas no Matplotlib. O Matplotlib pode trabalhar com objetos `.datetime` e objetos `numpy.datetime64` usando um conversor de unidades que reconhece essas datas e as converte em números de ponto flutuante. Antes do Matplotlib 3.3, o padrão para esta conversão retornava um float que representava os dias desde "0000-12-31T00:00:00". A partir do Matplotlib 3.3, o padrão são os dias a partir de "1970-01-01T00:00:00". Isso permite mais resolução para datas modernas.

## Dicas para a VM

Após a inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** e acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos o problema prontamente para você.
