# Ignorando Valores em um Padrão

Você viu que, às vezes, é útil ignorar valores em um padrão, como no último braço de um `match`, para obter um "catchall" (pega-tudo) que, na verdade, não faz nada, mas considera todos os valores restantes possíveis. Existem algumas maneiras de ignorar valores inteiros ou partes de valores em um padrão: usando o padrão `_` (que você já viu), usando o padrão `_` dentro de outro padrão, usando um nome que começa com um sublinhado ou usando `..` para ignorar as partes restantes de um valor. Vamos explorar como e por que usar cada um desses padrões.
