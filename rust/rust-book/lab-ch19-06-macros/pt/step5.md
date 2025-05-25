# Como Escrever uma Macro `derive` Customizada

Vamos criar um crate chamado `hello_macro` que define um trait chamado `HelloMacro` com uma função associada chamada `hello_macro`. Em vez de fazer com que nossos usuários implementem o trait `HelloMacro` para cada um de seus tipos, forneceremos uma macro procedural para que os usuários possam anotar seu tipo com `#[derive(HelloMacro)]` para obter uma implementação padrão da função `hello_macro`. A implementação padrão imprimirá `Hello, Macro! My name is` TypeName`!` onde TypeName é o nome do tipo no qual este trait foi definido. Em outras palavras, escreveremos um crate que permite que outro programador escreva código como a Listagem 19-30 usando nosso crate.

Nome do arquivo: `src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

Listagem 19-30: O código que um usuário de nosso crate poderá escrever ao usar nossa macro procedural

Este código imprimirá `Hello, Macro! My name is Pancakes!` quando terminarmos. O primeiro passo é criar um novo crate de biblioteca, assim:

```bash
cargo new hello_macro --lib
```

Em seguida, definiremos o trait `HelloMacro` e sua função associada:

Nome do arquivo: `src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

Temos um trait e sua função. Neste ponto, o usuário do nosso crate poderia implementar o trait para obter a funcionalidade desejada, assim:

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("Hello, Macro! My name is Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

No entanto, eles precisariam escrever o bloco de implementação para cada tipo que desejassem usar com `hello_macro`; queremos poupá-los de ter que fazer esse trabalho.

Além disso, ainda não podemos fornecer a função `hello_macro` com uma implementação padrão que imprimirá o nome do tipo no qual o trait é implementado: Rust não possui recursos de reflexão, portanto, não pode procurar o nome do tipo em tempo de execução. Precisamos de uma macro para gerar código em tempo de compilação.

O próximo passo é definir a macro procedural. No momento em que este artigo foi escrito, as macros procedurais precisam estar em seu próprio crate. Eventualmente, essa restrição pode ser removida. A convenção para estruturar crates e macros crates é a seguinte: para um crate chamado foo, um crate de macro procedural `derive` customizado é chamado foo`_derive`. Vamos iniciar um novo crate chamado `hello_macro_derive` dentro do nosso projeto `hello_macro`:

```bash
cargo new hello_macro_derive --lib
```

Nossos dois crates estão intimamente relacionados, então criamos o crate de macro procedural dentro do diretório do nosso crate `hello_macro`. Se alterarmos a definição do trait em `hello_macro`, também teremos que alterar a implementação da macro procedural em `hello_macro_derive`. Os dois crates precisarão ser publicados separadamente, e os programadores que usam esses crates precisarão adicionar ambos como dependências e trazê-los para o escopo. Em vez disso, poderíamos fazer com que o crate `hello_macro` usasse `hello_macro_derive` como uma dependência e reexportasse o código da macro procedural. No entanto, a forma como estruturamos o projeto torna possível para os programadores usarem `hello_macro` mesmo que não queiram a funcionalidade `derive`.

Precisamos declarar o crate `hello_macro_derive` como um crate de macro procedural. Também precisaremos de funcionalidade dos crates `syn` e `quote`, como você verá em um momento, então precisamos adicioná-los como dependências. Adicione o seguinte ao arquivo `Cargo.toml` para `hello_macro_derive`:

Nome do arquivo: `hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

Para começar a definir a macro procedural, coloque o código na Listagem 19-31 em seu arquivo `src/lib.rs` para o crate `hello_macro_derive`. Observe que este código não compilará até que adicionemos uma definição para a função `impl_hello_macro`.

Nome do arquivo: `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Construct a representation of Rust code as a syntax tree
    // that we can manipulate
    let ast = syn::parse(input).unwrap();

    // Build the trait implementation
    impl_hello_macro(&ast)
}
```

Listagem 19-31: Código que a maioria dos crates de macro procedural exigirá para processar o código Rust

Observe que dividimos o código na função `hello_macro_derive`, que é responsável por analisar o `TokenStream`, e na função `impl_hello_macro`, que é responsável por transformar a árvore de sintaxe: isso torna a escrita de uma macro procedural mais conveniente. O código na função externa (`hello_macro_derive` neste caso) será o mesmo para quase todos os crates de macro procedural que você vir ou criar. O código que você especifica no corpo da função interna (`impl_hello_macro` neste caso) será diferente dependendo do propósito da sua macro procedural.

Apresentamos três novos crates: `proc_macro`, `syn` (disponível em *https://crates.io/crates/syn*) e `quote` (disponível em *https://crates.io/crates/quote*). O crate `proc_macro` vem com Rust, então não precisamos adicioná-lo às dependências em `Cargo.toml`. O crate `proc_macro` é a API do compilador que nos permite ler e manipular o código Rust do nosso código.

O crate `syn` analisa o código Rust de uma string em uma estrutura de dados na qual podemos realizar operações. O crate `quote` transforma as estruturas de dados `syn` de volta em código Rust. Esses crates tornam muito mais simples analisar qualquer tipo de código Rust que possamos querer manipular: escrever um analisador completo para o código Rust não é uma tarefa simples.

A função `hello_macro_derive` será chamada quando um usuário de nossa biblioteca especificar `#[derive(HelloMacro)]` em um tipo. Isso é possível porque anotamos a função `hello_macro_derive` aqui com `proc_macro_derive` e especificamos o nome `HelloMacro`, que corresponde ao nome do nosso trait; esta é a convenção que a maioria das macros procedurais segue.

A função `hello_macro_derive` primeiro converte o `input` de um `TokenStream` em uma estrutura de dados na qual podemos interpretar e realizar operações. É aqui que `syn` entra em jogo. A função `parse` em `syn` recebe um `TokenStream` e retorna uma struct `DeriveInput` representando o código Rust analisado. A Listagem 19-32 mostra as partes relevantes da struct `DeriveInput` que obtemos ao analisar a string `struct Pancakes;`.

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

Listagem 19-32: A instância `DeriveInput` que obtemos ao analisar o código que possui o atributo da macro na Listagem 19-30

Os campos desta struct mostram que o código Rust que analisamos é uma struct unit com o `ident` (_identificador_, significando o nome) de `Pancakes`. Existem mais campos nesta struct para descrever todos os tipos de código Rust; verifique a documentação `syn` para `DeriveInput` em *https://docs.rs/syn/1.0/syn/struct.DeriveInput.html* para obter mais informações.

Em breve, definiremos a função `impl_hello_macro`, que é onde construiremos o novo código Rust que queremos incluir. Mas antes de fazermos isso, observe que a saída para nossa macro `derive` também é um `TokenStream`. O `TokenStream` retornado é adicionado ao código que os usuários do nosso crate escrevem, então, quando eles compilarem seu crate, eles obterão a funcionalidade extra que fornecemos no `TokenStream` modificado.

Você pode ter notado que estamos chamando `unwrap` para fazer com que a função `hello_macro_derive` entre em pânico se a chamada para a função `syn::parse` falhar aqui. É necessário que nossa macro procedural entre em pânico em caso de erros porque as funções `proc_macro_derive` devem retornar `TokenStream` em vez de `Result` para se conformar à API da macro procedural. Simplificamos este exemplo usando `unwrap`; no código de produção, você deve fornecer mensagens de erro mais específicas sobre o que deu errado usando `panic!` ou `expect`.

Agora que temos o código para transformar o código Rust anotado de um `TokenStream` em uma instância `DeriveInput`, vamos gerar o código que implementa o trait `HelloMacro` no tipo anotado, conforme mostrado na Listagem 19-33.

Nome do arquivo: `hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "Hello, Macro! My name is {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

Listagem 19-33: Implementando o trait `HelloMacro` usando o código Rust analisado

Obtemos uma instância da struct `Ident` contendo o nome (identificador) do tipo anotado usando `ast.ident`. A struct na Listagem 19-32 mostra que, quando executamos a função `impl_hello_macro` no código na Listagem 19-30, o `ident` que obtemos terá o campo `ident` com um valor de `"Pancakes"`. Assim, a variável `name` na Listagem 19-33 conterá uma instância da struct `Ident` que, quando impressa, será a string `"Pancakes"`, o nome da struct na Listagem 19-30.

A macro `quote!` nos permite definir o código Rust que queremos retornar. O compilador espera algo diferente do resultado direto da execução da macro `quote!`, então precisamos convertê-lo em um `TokenStream`. Fazemos isso chamando o método `into`, que consome esta representação intermediária e retorna um valor do tipo `TokenStream` necessário.

A macro `quote!` também fornece algumas mecânicas de modelagem muito legais: podemos inserir `#name`, e `quote!` o substituirá pelo valor na variável `name`. Você pode até fazer alguma repetição semelhante à forma como as macros regulares funcionam. Consulte a documentação do crate `quote` em *https://docs.rs/quote* para uma introdução completa.

Queremos que nossa macro procedural gere uma implementação de nosso trait `HelloMacro` para o tipo que o usuário anotou, o que podemos obter usando `#name`. A implementação do trait tem a função `hello_macro`, cujo corpo contém a funcionalidade que queremos fornecer: imprimir `Hello, Macro! My name is` e, em seguida, o nome do tipo anotado.

A macro `stringify!` usada aqui é integrada ao Rust. Ele recebe uma expressão Rust, como `1 + 2`, e em tempo de compilação transforma a expressão em um literal de string, como `"1 + 2"`. Isso é diferente de `format!` ou `println!`, macros que avaliam a expressão e, em seguida, transformam o resultado em uma `String`. Existe a possibilidade de que a entrada `#name` possa ser uma expressão para imprimir literalmente, então usamos `stringify!`. Usar `stringify!` também economiza uma alocação convertendo `#name` em um literal de string em tempo de compilação.

Neste ponto, `cargo build` deve ser concluído com sucesso em `hello_macro` e `hello_macro_derive`. Vamos conectar esses crates ao código na Listagem 19-30 para ver a macro procedural em ação! Crie um novo projeto binário em seu diretório `project` usando `cargo new pancakes`. Precisamos adicionar `hello_macro` e `hello_macro_derive` como dependências no `Cargo.toml` do crate `pancakes`. Se você estiver publicando suas versões de `hello_macro` e `hello_macro_derive` em *https://crates.io*, elas seriam dependências regulares; caso contrário, você pode especificá-las como dependências `path` da seguinte forma:

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

Coloque o código na Listagem 19-30 em `src/main.rs` e execute `cargo run`: ele deve imprimir `Hello, Macro! My name is Pancakes!` A implementação do trait `HelloMacro` da macro procedural foi incluída sem que o crate `pancakes` precisasse implementá-lo; o `#[derive(HelloMacro)]` adicionou a implementação do trait.

Em seguida, vamos explorar como os outros tipos de macros procedurais diferem das macros `derive` customizadas.
