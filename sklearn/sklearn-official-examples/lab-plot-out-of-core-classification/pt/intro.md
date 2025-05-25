# Introdução

Este laboratório fornece um exemplo de como usar o scikit-learn para classificação de texto utilizando aprendizado fora da memória principal. O objetivo é aprender com dados que não cabem na memória principal. Para isso, utilizamos um classificador online que suporta o método `partial_fit`, que será alimentado com lotes de exemplos. Para garantir que o espaço de características permaneça o mesmo ao longo do tempo, utilizamos um `HashingVectorizer` que projetará cada exemplo no mesmo espaço de características. Isto é especialmente útil no caso de classificação de texto, onde novas características (palavras) podem aparecer em cada lote.

## Dicas da Máquina Virtual

Após o arranque da máquina virtual, clique no canto superior esquerdo para mudar para a aba **Notebook** para aceder ao [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Por vezes, pode ser necessário esperar alguns segundos para o Jupyter Notebook terminar de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se tiver problemas durante o aprendizado, não hesite em contactar o Labby. Forneça feedback após a sessão e resolveremos o problema rapidamente.
