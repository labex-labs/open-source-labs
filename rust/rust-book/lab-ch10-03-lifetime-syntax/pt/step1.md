# Validando Referências com Lifetimes

_Lifetimes_ (Tempos de vida) são outro tipo de genérico que já estamos usando. Em vez de garantir que um tipo tenha o comportamento que queremos, os _lifetimes_ garantem que as referências sejam válidas pelo tempo que precisarmos.

Um detalhe que não discutimos em "Referências e Empréstimos" é que toda referência em Rust tem um _*lifetime*_, que é o escopo para o qual essa referência é válida. Na maioria das vezes, os _lifetimes_ são implícitos e inferidos, assim como na maioria das vezes, os tipos são inferidos. Devemos anotar os tipos somente quando múltiplos tipos são possíveis. De forma semelhante, devemos anotar os _lifetimes_ quando os _lifetimes_ das referências podem estar relacionados de algumas maneiras diferentes. Rust exige que anotemos os relacionamentos usando parâmetros genéricos de _lifetime_ para garantir que as referências reais usadas em tempo de execução sejam definitivamente válidas.

Anotar _lifetimes_ nem mesmo é um conceito que a maioria das outras linguagens de programação possui, então isso vai parecer estranho. Embora não abordemos os _lifetimes_ em sua totalidade neste capítulo, discutiremos as formas comuns com que você pode encontrar a sintaxe de _lifetime_ para que possa se sentir confortável com o conceito.
