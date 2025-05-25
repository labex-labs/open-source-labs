# Introdução

Este tutorial irá guiá-lo sobre como desenhar uma curva com uma faixa de erro usando Python Matplotlib. Uma faixa de erro é usada para indicar a incerteza da curva. Neste exemplo, assumimos que o erro pode ser dado como um escalar _err_ que descreve a incerteza perpendicular à curva em cada ponto. Visualizamos este erro como uma faixa colorida ao redor do caminho usando um `.PathPatch`. O patch é criado a partir de dois segmentos de caminho _(xp, yp)_, e _(xn, yn)_ que são deslocados por +/- _err_ perpendicularmente à curva _(x, y)_.

## Dicas para a VM

Após a inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos o problema prontamente para você.
