# Refutabilidade: Se um Padrão Pode Deixar de Corresponder

Padrões vêm em duas formas: refutáveis e irrefutáveis. Padrões que corresponderão a qualquer valor possível passado são _irrefutáveis_. Um exemplo seria `x` na declaração `let x = 5;` porque `x` corresponde a qualquer coisa e, portanto, não pode deixar de corresponder. Padrões que podem deixar de corresponder a algum valor possível são _refutáveis_. Um exemplo seria `Some(x)` na expressão `if let Some(x) = a_value` porque se o valor na variável `a_value` for `None` em vez de `Some`, o padrão `Some(x)` não corresponderá.

Parâmetros de função, declarações `let` e loops `for` só podem aceitar padrões irrefutáveis porque o programa não pode fazer nada significativo quando os valores não correspondem. As expressões `if let` e `while let` aceitam padrões refutáveis e irrefutáveis, mas o compilador avisa contra padrões irrefutáveis porque, por definição, eles se destinam a lidar com possíveis falhas: a funcionalidade de uma condicional está em sua capacidade de se comportar de maneira diferente dependendo do sucesso ou da falha.

Em geral, você não deve se preocupar com a distinção entre padrões refutáveis e irrefutáveis; no entanto, você precisa estar familiarizado com o conceito de refutabilidade para poder responder quando o vir em uma mensagem de erro. Nesses casos, você precisará alterar o padrão ou a construção que está usando com o padrão, dependendo do comportamento pretendido do código.

Vamos ver um exemplo do que acontece quando tentamos usar um padrão refutável onde o Rust exige um padrão irrefutável e vice-versa. A Listagem 18-8 mostra uma declaração `let`, mas para o padrão, especificamos `Some(x)`, um padrão refutável. Como você pode esperar, este código não compilará.

```rust
let Some(x) = some_option_value;
```

Listagem 18-8: Tentando usar um padrão refutável com `let`

Se `some_option_value` fosse um valor `None`, ele não corresponderia ao padrão `Some(x)`, o que significa que o padrão é refutável. No entanto, a declaração `let` só pode aceitar um padrão irrefutável porque não há nada válido que o código possa fazer com um valor `None`. No tempo de compilação, o Rust reclamará que tentamos usar um padrão refutável onde um padrão irrefutável é necessário:

```bash
error[E0005]: refutable pattern in local binding: `None` not covered
   --> src/main.rs:3:9
    |
3   |     let Some(x) = some_option_value;
    |         ^^^^^^^ pattern `None` not covered
    |
    = note: `let` bindings require an "irrefutable pattern", like a `struct` or
an `enum` with only one variant
    = note: for more information, visit
https://doc.rust-lang.org/book/ch18-02-refutability.html
    = note: the matched value is of type `Option<i32>`
help: you might want to use `if let` to ignore the variant that isn't matched
    |
3   |     let x = if let Some(x) = some_option_value { x } else { todo!() };
    |     ++++++++++                                 ++++++++++++++++++++++
```

Como não cobrimos (e não poderíamos cobrir!) todos os valores válidos com o padrão `Some(x)`, o Rust produz corretamente um erro do compilador.

Se tivermos um padrão refutável onde um padrão irrefutável é necessário, podemos corrigi-lo alterando o código que usa o padrão: em vez de usar `let`, podemos usar `if let`. Então, se o padrão não corresponder, o código simplesmente pulará o código nas chaves, dando a ele uma maneira de continuar validamente. A Listagem 18-9 mostra como corrigir o código na Listagem 18-8.

    if let Some(x) = some_option_value {
        println!("{x}");
    }

Listagem 18-9: Usando `if let` e um bloco com padrões refutáveis em vez de `let`

Demos ao código uma saída! Este código é perfeitamente válido, embora signifique que não podemos usar um padrão irrefutável sem receber um erro. Se dermos a `if let` um padrão que sempre corresponderá, como `x`, conforme mostrado na Listagem 18-10, o compilador emitirá um aviso.

    if let x = 5 {
        println!("{x}");
    };

Listagem 18-10: Tentando usar um padrão irrefutável com `if let`

Rust reclama que não faz sentido usar `if let` com um padrão irrefutável:

    warning: irrefutable `if let` pattern
     --> src/main.rs:2:8
      |
    2 |     if let x = 5 {
      |        ^^^^^^^^^
      |
      = note: `#[warn(irrefutable_let_patterns)]` on by default
      = note: this pattern will always match, so the `if let` is
    useless
      = help: consider replacing the `if let` with a `let`

Por esta razão, os braços de correspondência (match arms) devem usar padrões refutáveis, exceto para o último braço, que deve corresponder a quaisquer valores restantes com um padrão irrefutável. O Rust nos permite usar um padrão irrefutável em um `match` com apenas um braço, mas essa sintaxe não é particularmente útil e pode ser substituída por uma declaração `let` mais simples.

Agora que você sabe onde usar padrões e a diferença entre padrões refutáveis e irrefutáveis, vamos cobrir toda a sintaxe que podemos usar para criar padrões.
