# Packages e Crates

As primeiras partes do sistema de módulos que abordaremos são packages e crates.

Um _crate_ é a menor quantidade de código que o compilador Rust considera de cada vez. Mesmo que você execute `rustc` em vez de `cargo` e passe um único arquivo de código-fonte (como fizemos em "Escrevendo e Executando um Programa Rust"), o compilador considera esse arquivo como um crate. Crates podem conter módulos, e os módulos podem ser definidos em outros arquivos que são compilados com o crate, como veremos nas próximas seções.

Um crate pode vir em uma de duas formas: um crate binário ou um crate de biblioteca. _Crates binários_ são programas que você pode compilar em um executável que você pode executar, como um programa de linha de comando ou um servidor. Cada um deve ter uma função chamada `main` que define o que acontece quando o executável é executado. Todos os crates que criamos até agora foram crates binários.

_Crates de biblioteca_ não têm uma função `main` e não são compilados em um executável. Em vez disso, eles definem funcionalidades destinadas a serem compartilhadas com vários projetos. Por exemplo, o crate `rand` que usamos no Capítulo 2 fornece funcionalidade que gera números aleatórios. Na maioria das vezes, quando os Rustaceans dizem "crate", eles se referem a um crate de biblioteca, e usam "crate" de forma intercambiável com o conceito geral de programação de uma "biblioteca".

O _crate root_ é um arquivo de origem de onde o compilador Rust começa e constitui o módulo raiz do seu crate (explicaremos os módulos em profundidade em "Definindo Módulos para Controlar Escopo e Privacidade").

Um _package_ é um conjunto de um ou mais crates que fornece um conjunto de funcionalidades. Um package contém um arquivo `Cargo.toml` que descreve como construir esses crates. Cargo é, na verdade, um package que contém o crate binário para a ferramenta de linha de comando que você tem usado para construir seu código. O package Cargo também contém um crate de biblioteca do qual o crate binário depende. Outros projetos podem depender do crate de biblioteca Cargo para usar a mesma lógica que a ferramenta de linha de comando Cargo usa.

Um crate pode vir em uma de duas formas: um crate binário ou um crate de biblioteca. Um package pode conter quantos crates binários você quiser, mas no máximo apenas um crate de biblioteca. Um package deve conter pelo menos um crate, seja um crate de biblioteca ou binário.

Vamos analisar o que acontece quando criamos um package. Primeiro, inserimos o comando `cargo new my-project`:

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

Depois de executarmos `cargo new my-project`, usamos `ls` para ver o que o Cargo cria. No diretório do projeto, há um arquivo `Cargo.toml`, nos dando um package. Há também um diretório `src` que contém `main.rs`. Abra `Cargo.toml` em seu editor de texto e observe que não há menção de `src/main.rs`. Cargo segue uma convenção de que `src/main.rs` é o crate root de um crate binário com o mesmo nome do package. Da mesma forma, Cargo sabe que, se o diretório do package contiver `src/lib.rs`, o package contém um crate de biblioteca com o mesmo nome do package, e `src/lib.rs` é seu crate root. Cargo passa os arquivos crate root para `rustc` para construir a biblioteca ou o binário.

Aqui, temos um package que contém apenas `src/main.rs`, o que significa que ele contém apenas um crate binário chamado `my-project`. Se um package contiver `src/main.rs` e `src/lib.rs`, ele terá dois crates: um binário e uma biblioteca, ambos com o mesmo nome do package. Um package pode ter vários crates binários, colocando arquivos no diretório `src/bin`: cada arquivo será um crate binário separado.

> **Folha de Dicas de Módulos**
>
> Antes de entrarmos nos detalhes de módulos e caminhos, aqui fornecemos uma referência rápida sobre como módulos, caminhos, a palavra-chave `use` e a palavra-chave `pub` funcionam no compilador e como a maioria dos desenvolvedores organiza seu código. Passaremos por exemplos de cada uma dessas regras ao longo deste capítulo, mas este é um ótimo lugar para consultar como um lembrete de como os módulos funcionam.
>
> - **Comece do crate root**: Ao compilar um crate, o compilador primeiro procura no arquivo crate root (geralmente `src/lib.rs` para um crate de biblioteca ou `src/main.rs` para um crate binário) o código a ser compilado.
> - **Declarando módulos**: No arquivo crate root, você pode declarar novos módulos; digamos que você declare um módulo "garden" com `mod garden;`. O compilador procurará o código do módulo nestes lugares:
>   - Inline, dentro de chaves que substituem o ponto e vírgula após `mod garden`
>   - No arquivo `src/garden.rs`
>   - No arquivo `src/garden/mod.rs`
> - **Declarando submódulos**: Em qualquer arquivo diferente do crate root, você pode declarar submódulos. Por exemplo, você pode declarar `mod vegetables;` em `src/garden.rs`. O compilador procurará o código do submódulo dentro do diretório nomeado para o módulo pai nestes lugares:
>   - Inline, diretamente após `mod vegetables`, dentro de chaves em vez do ponto e vírgula
>   - No arquivo `src/garden/vegetables.rs`
>   - No arquivo `src/garden/vegetables/mod.rs`
> - **Caminhos para código em módulos**: Uma vez que um módulo faz parte do seu crate, você pode se referir ao código nesse módulo de qualquer outro lugar no mesmo crate, desde que as regras de privacidade permitam, usando o caminho para o código. Por exemplo, um tipo `Asparagus` no módulo de vegetais do jardim seria encontrado em `crate::garden::vegetables::Asparagus`.
> - **Privado vs. público**: O código dentro de um módulo é privado de seus módulos pai por padrão. Para tornar um módulo público, declare-o com `pub mod` em vez de `mod`. Para tornar os itens dentro de um módulo público também públicos, use `pub` antes de suas declarações.
> - **A palavra-chave use**: Dentro de um escopo, a palavra-chave `use` cria atalhos para itens para reduzir a repetição de caminhos longos. Em qualquer escopo que possa se referir a `crate::garden::vegetables::Asparagus`, você pode criar um atalho com `use crate::garden::vegetables::Asparagus;` e, a partir daí, você só precisa escrever `Asparagus` para usar esse tipo no escopo.
>
> Aqui, criamos um crate binário chamado `backyard` que ilustra essas regras. O diretório do crate, também chamado `backyard`, contém estes arquivos e diretórios:
>
> ```bash
> backyard
> ├── Cargo.lock
> ├── Cargo.toml
> └── src
> ├── garden
> │ └── vegetables.rs
> ├── garden.rs
> └── main.rs
> ```
>
> O arquivo crate root neste caso é `src/main.rs`, e ele contém:
>
> ```rust
> use crate::garden::vegetables::Asparagus;
>
> pub mod garden;
>
> fn main() {
>     let plant = Asparagus {};
>     println!("I'm growing {:?}!", plant);
> }
> ```
>
> A linha `pub mod garden;` diz ao compilador para incluir o código que ele encontra em `src/garden.rs`, que é:
>
> ```rust
> pub mod vegetables;
> ```
>
> Aqui, `pub mod vegetables;` significa que o código em `src/garden/vegetables.rs` também está incluído. Esse código é:
>
> ```rust
> #[derive(Debug)]
> pub struct Asparagus {}
> ```
>
> Agora, vamos entrar nos detalhes dessas regras e demonstrá-las em ação!
