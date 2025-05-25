# Por que Geradores

- Muitos problemas são expressos de forma muito mais clara em termos de iteração.
  - Iterar sobre uma coleção de itens e realizar algum tipo de operação (pesquisa, substituição, modificação, etc.).
  - Pipelines de processamento podem ser aplicados a uma ampla gama de problemas de processamento de dados.
- Melhor eficiência de memória.
  - Produzem valores apenas quando necessário.
  - Contraste com a construção de listas gigantes.
  - Podem operar em dados de streaming.
- Geradores incentivam a reutilização de código.
  - Separa a _iteração_ do código que usa a iteração.
  - Você pode construir uma caixa de ferramentas de funções de iteração interessantes e _misturar e combinar_ (mix-n-match).
