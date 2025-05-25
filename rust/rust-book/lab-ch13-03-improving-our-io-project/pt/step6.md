# Escolhendo entre Loops e Iteradores

A próxima pergunta lógica é qual estilo você deve escolher em seu próprio código e por quê: a implementação original na Listagem 13-21 ou a versão usando iteradores na Listagem 13-22. A maioria dos programadores Rust prefere usar o estilo de iterador. É um pouco mais difícil de entender no início, mas assim que você se familiarizar com os vários adaptadores de iterador e o que eles fazem, os iteradores podem ser mais fáceis de entender. Em vez de mexer com as várias partes do loop e construir novos vetores, o código se concentra no objetivo de alto nível do loop. Isso abstrai parte do código comum, tornando mais fácil ver os conceitos que são exclusivos deste código, como a condição de filtragem que cada elemento no iterador deve passar.

Mas as duas implementações são realmente equivalentes? A suposição intuitiva pode ser que o loop de nível inferior será mais rápido. Vamos falar sobre desempenho.
