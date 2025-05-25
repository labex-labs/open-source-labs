# Constantes

Como variáveis imutáveis, as _constantes_ são valores que são vinculados a um nome e não podem ser alterados, mas existem algumas diferenças entre constantes e variáveis.

Primeiro, você não pode usar `mut` com constantes. As constantes não são apenas imutáveis por padrão - elas são sempre imutáveis. Você declara constantes usando a palavra-chave `const` em vez da palavra-chave `let`, e o tipo do valor _deve_ ser anotado. Abordaremos tipos e anotações de tipo em "Tipos de Dados", então não se preocupe com os detalhes agora. Apenas saiba que você sempre deve anotar o tipo.

As constantes podem ser declaradas em qualquer escopo, incluindo o escopo global, o que as torna úteis para valores que muitas partes do código precisam conhecer.

A última diferença é que as constantes podem ser definidas apenas para uma expressão constante, não para o resultado de um valor que só pode ser computado em tempo de execução.

Aqui está um exemplo de uma declaração de constante:

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

O nome da constante é `THREE_HOURS_IN_SECONDS` e seu valor é definido como o resultado da multiplicação de 60 (o número de segundos em um minuto) por 60 (o número de minutos em uma hora) por 3 (o número de horas que queremos contar neste programa). A convenção de nomenclatura do Rust para constantes é usar tudo em maiúsculas com sublinhados entre as palavras. O compilador é capaz de avaliar um conjunto limitado de operações em tempo de compilação, o que nos permite escolher escrever este valor de uma forma que seja mais fácil de entender e verificar, em vez de definir esta constante para o valor `10.800`. Consulte a seção de avaliação de constantes da Referência do Rust em *https://doc.rust-lang.org/reference/const_eval.html* para obter mais informações sobre quais operações podem ser usadas ao declarar constantes.

As constantes são válidas durante todo o tempo de execução de um programa, dentro do escopo em que foram declaradas. Essa propriedade torna as constantes úteis para valores no seu domínio de aplicação que várias partes do programa podem precisar conhecer, como o número máximo de pontos que qualquer jogador de um jogo pode ganhar ou a velocidade da luz.

Nomear valores codificados usados em todo o seu programa como constantes é útil para transmitir o significado desse valor aos futuros mantenedores do código. Também ajuda ter apenas um lugar no seu código que você precisaria alterar se o valor codificado precisasse ser atualizado no futuro.
