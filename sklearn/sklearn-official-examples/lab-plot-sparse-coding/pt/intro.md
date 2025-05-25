# Introdução

Neste laboratório, aprenderemos a transformar um sinal como uma combinação esparsa de ondas de Ricker usando métodos de codificação esparsa. A onda de Ricker (também conhecida como chapéu mexicano ou a segunda derivada de uma gaussiana) não é um núcleo particularmente bom para representar sinais de partes constantes como este. Portanto, pode-se ver o quanto adicionar diferentes larguras de átomos importa e, portanto, motiva a aprendizagem do dicionário para melhor se ajustar ao seu tipo de sinais.

Vamos comparar visualmente diferentes métodos de codificação esparsa usando o estimador `SparseCoder`. O dicionário mais rico à direita não é maior em tamanho, uma subamostragem mais pesada é realizada para permanecer na mesma ordem de grandeza.

## Dicas de Máquina Virtual

Após o início da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** para acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário esperar alguns segundos para que o Jupyter Notebook termine de carregar. A validação de operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão e resolveremos prontamente o problema para você.
