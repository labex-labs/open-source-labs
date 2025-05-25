# Exportando uma API Pública Conveniente com `pub use`

A estrutura da sua API pública é uma consideração importante ao publicar uma crate. As pessoas que usam sua crate estão menos familiarizadas com a estrutura do que você e podem ter dificuldade em encontrar as partes que desejam usar se sua crate tiver uma grande hierarquia de módulos.

No Capítulo 7, abordamos como tornar os itens públicos usando a palavra-chave `pub` e como trazer itens para um escopo com a palavra-chave `use`. No entanto, a estrutura que faz sentido para você enquanto está desenvolvendo uma crate pode não ser muito conveniente para seus usuários. Você pode querer organizar suas structs em uma hierarquia contendo vários níveis, mas então as pessoas que desejam usar um tipo que você definiu profundamente na hierarquia podem ter problemas para descobrir que esse tipo existe. Elas também podem ficar irritadas por ter que inserir `use` `my_crate::`some_module`::`another_module`::`UsefulType`;` em vez de `use` `my_crate::`UsefulType`;`.

A boa notícia é que, se a estrutura _não_ for conveniente para outros usarem de outra biblioteca, você não precisa reorganizar sua organização interna: em vez disso, você pode reexportar itens para criar uma estrutura pública que seja diferente da sua estrutura privada usando `pub use`. _Reexportar_ pega um item público em um local e o torna público em outro local, como se fosse definido no outro local.

Por exemplo, digamos que criamos uma biblioteca chamada `art` para modelar conceitos artísticos. Dentro desta biblioteca, existem dois módulos: um módulo `kinds` contendo dois enums chamados `PrimaryColor` e `SecondaryColor` e um módulo `utils` contendo uma função chamada `mix`, conforme mostrado na Listagem 14-3.

Nome do arquivo: `src/lib.rs`

```rust
//! # Art
//!
//! A library for modeling artistic concepts.

pub mod kinds {
    /// The primary colors according to the RYB color model.
    pub enum PrimaryColor {
        Red,
        Yellow,
        Blue,
    }

    /// The secondary colors according to the RYB color model.
    pub enum SecondaryColor {
        Orange,
        Green,
        Purple,
    }
}

pub mod utils {
    use crate::kinds::*;

    /// Combines two primary colors in equal amounts to create
    /// a secondary color.
    pub fn mix(
        c1: PrimaryColor,
        c2: PrimaryColor,
    ) -> SecondaryColor {
        --snip--
    }
}
```

Listagem 14-3: Uma biblioteca `art` com itens organizados em módulos `kinds` e `utils`

A Figura 14-3 mostra como seria a página inicial da documentação para esta crate gerada por `cargo doc`.

Figura 14-3: Página inicial da documentação para `art` que lista os módulos `kinds` e `utils`

Observe que os tipos `PrimaryColor` e `SecondaryColor` não estão listados na página inicial, nem a função `mix`. Precisamos clicar em `kinds` e `utils` para vê-los.

Outra crate que depende desta biblioteca precisaria de declarações `use` que trouxessem os itens de `art` para o escopo, especificando a estrutura do módulo que está atualmente definida. A Listagem 14-4 mostra um exemplo de uma crate que usa os itens `PrimaryColor` e `mix` da crate `art`.

Nome do arquivo: `src/main.rs`

```rust
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}
```

Listagem 14-4: Uma crate usando os itens da crate `art` com sua estrutura interna exportada

O autor do código na Listagem 14-4, que usa a crate `art`, teve que descobrir que `PrimaryColor` está no módulo `kinds` e `mix` está no módulo `utils`. A estrutura do módulo da crate `art` é mais relevante para os desenvolvedores que trabalham na crate `art` do que para aqueles que a usam. A estrutura interna não contém nenhuma informação útil para alguém que tenta entender como usar a crate `art`, mas sim causa confusão porque os desenvolvedores que a usam precisam descobrir onde procurar e devem especificar os nomes dos módulos nas declarações `use`.

Para remover a organização interna da API pública, podemos modificar o código da crate `art` na Listagem 14-3 para adicionar declarações `pub use` para reexportar os itens no nível superior, conforme mostrado na Listagem 14-5.

Nome do arquivo: `src/lib.rs`

```rust
//! # Art
//!
//! A library for modeling artistic concepts.

pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    --snip--
}

pub mod utils {
    --snip--
}
```

Listagem 14-5: Adicionando declarações `pub use` para reexportar itens

A documentação da API que `cargo doc` gera para esta crate agora listará e vinculará as reexportações na página inicial, conforme mostrado na Figura 14-4, tornando os tipos `PrimaryColor` e `SecondaryColor` e a função `mix` mais fáceis de encontrar.

Figura 14-4: A página inicial da documentação para `art` que lista as reexportações

Os usuários da crate `art` ainda podem ver e usar a estrutura interna da Listagem 14-3, conforme demonstrado na Listagem 14-4, ou podem usar a estrutura mais conveniente na Listagem 14-5, conforme mostrado na Listagem 14-6.

Nome do arquivo: `src/main.rs`

```rust
use art::mix;
use art::PrimaryColor;

fn main() {
    --snip--
}
```

Listagem 14-6: Um programa usando os itens reexportados da crate `art`

Em casos em que há muitos módulos aninhados, reexportar os tipos no nível superior com `pub use` pode fazer uma diferença significativa na experiência das pessoas que usam a crate. Outro uso comum de `pub use` é reexportar definições de uma dependência na crate atual para tornar as definições dessa crate parte da API pública da sua crate.

Criar uma estrutura de API pública útil é mais uma arte do que uma ciência, e você pode iterar para encontrar a API que funciona melhor para seus usuários. Escolher `pub use` oferece flexibilidade na forma como você estrutura sua crate internamente e desacopla essa estrutura interna do que você apresenta aos seus usuários. Observe algum código de crates que você instalou para ver se sua estrutura interna difere de sua API pública.
