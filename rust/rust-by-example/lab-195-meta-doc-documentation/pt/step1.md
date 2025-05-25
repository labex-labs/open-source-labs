# Documentação

Utilize `cargo doc` para construir a documentação em `target/doc`.

Utilize `cargo test` para executar todos os testes (incluindo testes de documentação) e `cargo test --doc` para executar apenas os testes de documentação.

Estes comandos invocarão apropriadamente `rustdoc` (e `rustc`) conforme necessário.

## Comentários de Documentação

Comentários de documentação são muito úteis para grandes projetos que exigem documentação. Quando o `rustdoc` é executado, estes são os comentários que são compilados na documentação. São denotados por `///` e suportam [Markdown].

````rust
#![crate_name = "doc"]

/// Um ser humano é representado aqui
pub struct Person {
    /// Uma pessoa deve ter um nome, não importa o quanto Julieta possa odiá-lo
    name: String,
}

impl Person {
    /// Retorna uma pessoa com o nome que lhe foi dado
    ///
    /// # Argumentos
    ///
    /// * `name` - Uma fatia de string que contém o nome da pessoa
    ///
    /// # Exemplos
    ///
    /// ```
    /// // Pode ter código Rust entre as delimitações dentro dos comentários
    /// // Se passar --test para `rustdoc`, ele até o testará para si!
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }

    /// Dá um cumprimento amigável!
    ///
    /// Diz "Olá, [nome](Person::name)" à `Person` em que é chamado.
    pub fn hello(&self) {
        println!("Olá, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}
````

Para executar os testes, primeiro compile o código como uma biblioteca e, em seguida, indique ao `rustdoc` onde encontrar a biblioteca para que possa ligá-la a cada programa de teste de documentação:

```shell
$ rustc doc.rs --crate-type lib
$ rustdoc --test --extern doc="libdoc.rlib" doc.rs
```

## Atributos de Documentação

Segue-se alguns exemplos dos atributos `#[doc]` mais comuns utilizados com `rustdoc`.

## `inline`

Utilizado para incorporar a documentação, em vez de ligar para uma página separada.

```rust
#[doc(inline)]
pub use bar::Bar;

/// Documentação de bar
mod bar {
    /// Documentação para Bar
    pub struct Bar;
}
```

## `no_inline`

Utilizado para evitar a ligação a uma página separada ou a qualquer lugar.

```rust
// Exemplo de libcore/prelude
#[doc(no_inline)]
pub use crate::mem::drop;
```

## `hidden`

Utilizar isto indica ao `rustdoc` que não deve incluir isto na documentação:

```rust
// Exemplo da biblioteca futures-rs
#[doc(hidden)]
pub use self::async_await::*;
```

Para documentação, o `rustdoc` é amplamente utilizado pela comunidade. É o que é usado para gerar a documentação da [biblioteca padrão](https://doc.rust-lang.org/std/).
