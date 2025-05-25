# Elisão de _Lifetime_

Você aprendeu que toda referência tem um _lifetime_ e que você precisa especificar parâmetros de _lifetime_ para funções ou structs que usam referências. No entanto, tínhamos uma função na Listagem 4-9, mostrada novamente na Listagem 10-25, que compilava sem anotações de _lifetime_.

Nome do arquivo: `src/lib.rs`

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Listagem 10-25: Uma função que definimos na Listagem 4-9 que compilou sem anotações de _lifetime_, embora o parâmetro e o tipo de retorno sejam referências

A razão pela qual esta função compila sem anotações de _lifetime_ é histórica: em versões anteriores (pré-1.0) do Rust, este código não teria compilado porque cada referência precisava de um _lifetime_ explícito. Naquela época, a assinatura da função teria sido escrita assim:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Depois de escrever muito código Rust, a equipe Rust descobriu que os programadores Rust estavam inserindo as mesmas anotações de _lifetime_ repetidamente em situações específicas. Essas situações eram previsíveis e seguiam alguns padrões determinísticos. Os desenvolvedores programaram esses padrões no código do compilador para que o verificador de empréstimo pudesse inferir os _lifetimes_ nessas situações e não precisasse de anotações explícitas.

Este pedaço da história do Rust é relevante porque é possível que mais padrões determinísticos surjam e sejam adicionados ao compilador. No futuro, ainda menos anotações de _lifetime_ podem ser necessárias.

Os padrões programados na análise de referências do Rust são chamados de _regras de elisão de *lifetime*_. Estas não são regras para os programadores seguirem; são um conjunto de casos particulares que o compilador considerará, e se seu código se encaixa nesses casos, você não precisa escrever os _lifetimes_ explicitamente.

As regras de elisão não fornecem inferência completa. Se o Rust aplicar as regras de forma determinística, mas ainda houver ambiguidade quanto aos _lifetimes_ que as referências têm, o compilador não adivinhará qual deve ser o _lifetime_ das referências restantes. Em vez de adivinhar, o compilador fornecerá um erro que você pode resolver adicionando as anotações de _lifetime_.

_Lifetimes_ em parâmetros de função ou método são chamados de _*lifetimes* de entrada_, e _lifetimes_ em valores de retorno são chamados de _*lifetimes* de saída_.

O compilador usa três regras para descobrir os _lifetimes_ das referências quando não há anotações explícitas. A primeira regra se aplica aos _lifetimes_ de entrada, e a segunda e a terceira regras se aplicam aos _lifetimes_ de saída. Se o compilador chegar ao final das três regras e ainda houver referências para as quais não consegue descobrir os _lifetimes_, o compilador parará com um erro. Essas regras se aplicam a definições `fn`, bem como a blocos `impl`.

A primeira regra é que o compilador atribui um parâmetro de _lifetime_ a cada parâmetro que é uma referência. Em outras palavras, uma função com um parâmetro recebe um parâmetro de _lifetime_: `fn foo<'a>(x: &'a i32)`; uma função com dois parâmetros recebe dois parâmetros de _lifetime_ separados: `fn foo<'a, 'b>(x: &'a i32, y: &'b i32)`; e assim por diante.

A segunda regra é que, se houver exatamente um parâmetro de _lifetime_ de entrada, esse _lifetime_ é atribuído a todos os parâmetros de _lifetime_ de saída: `fn foo<'a>(x: &'a i32) -> &'a i32`.

A terceira regra é que, se houver vários parâmetros de _lifetime_ de entrada, mas um deles for `&self` ou `&mut self` porque este é um método, o _lifetime_ de `self` é atribuído a todos os parâmetros de _lifetime_ de saída. Esta terceira regra torna os métodos muito mais agradáveis de ler e escrever porque menos símbolos são necessários.

Vamos fingir que somos o compilador. Aplicaremos essas regras para descobrir os _lifetimes_ das referências na assinatura da função `first_word` na Listagem 10-25. A assinatura começa sem nenhum _lifetime_ associado às referências:

```rust
fn first_word(s: &str) -> &str {
```

Então, o compilador aplica a primeira regra, que especifica que cada parâmetro recebe seu próprio _lifetime_. Vamos chamá-lo de `'a` como de costume, então agora a assinatura é esta:

```rust
fn first_word<'a>(s: &'a str) -> &str {
```

A segunda regra se aplica porque há exatamente um _lifetime_ de entrada. A segunda regra especifica que o _lifetime_ do único parâmetro de entrada é atribuído ao _lifetime_ de saída, então a assinatura agora é esta:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Agora, todas as referências nesta assinatura de função têm _lifetimes_, e o compilador pode continuar sua análise sem que o programador precise anotar os _lifetimes_ nesta assinatura de função.

Vamos analisar outro exemplo, desta vez usando a função `longest` que não tinha parâmetros de _lifetime_ quando começamos a trabalhar com ela na Listagem 10-20:

```rust
fn longest(x: &str, y: &str) -> &str {
```

Vamos aplicar a primeira regra: cada parâmetro recebe seu próprio _lifetime_. Desta vez, temos dois parâmetros em vez de um, então temos dois _lifetimes_:

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str {
```

Você pode ver que a segunda regra não se aplica porque há mais de um _lifetime_ de entrada. A terceira regra também não se aplica, porque `longest` é uma função em vez de um método, então nenhum dos parâmetros é `self`. Depois de trabalhar com todas as três regras, ainda não descobrimos qual é o _lifetime_ do tipo de retorno. É por isso que recebemos um erro ao tentar compilar o código na Listagem 10-20: o compilador trabalhou com as regras de elisão de _lifetime_, mas ainda não conseguiu descobrir todos os _lifetimes_ das referências na assinatura.

Como a terceira regra realmente só se aplica em assinaturas de métodos, analisaremos os _lifetimes_ nesse contexto a seguir para ver por que a terceira regra significa que não precisamos anotar _lifetimes_ em assinaturas de métodos com muita frequência.
