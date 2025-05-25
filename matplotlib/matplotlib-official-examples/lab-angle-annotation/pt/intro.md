# Introdução

Neste tutorial, você aprenderá como criar um rótulo de ângulo invariante à escala usando Matplotlib. A anotação de ângulo é frequentemente usada para marcar ângulos entre linhas ou dentro de formas com um arco circular. Embora o Matplotlib forneça um `~.patches.Arc`, um problema inerente ao usá-lo diretamente para tais propósitos é que um arco sendo circular no espaço de dados não é necessariamente circular no espaço de exibição. Além disso, o raio do arco é frequentemente melhor definido em um sistema de coordenadas que é independente das coordenadas reais dos dados - pelo menos se você quiser poder ampliar livremente seu gráfico sem que a anotação cresça até o infinito. Isso exige uma solução onde o centro do arco é definido no espaço de dados, mas seu raio em uma unidade física como pontos ou pixels, ou como uma proporção da dimensão dos Eixos (Axes).

## Dicas para a VM (VM Tips)

Após a inicialização da VM, clique no canto superior esquerdo para mudar para a aba **Notebook** e acessar o [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter) para praticar.

Às vezes, pode ser necessário aguardar alguns segundos para que o Jupyter Notebook termine de carregar. A validação das operações não pode ser automatizada devido a limitações no Jupyter Notebook.

Se você enfrentar problemas durante o aprendizado, sinta-se à vontade para perguntar ao Labby. Forneça feedback após a sessão, e resolveremos o problema prontamente para você.
