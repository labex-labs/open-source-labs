# Referências Pendentes (Dangling References)

Em linguagens com ponteiros, é fácil criar erroneamente um _ponteiro pendente_ (dangling pointer) — um ponteiro que referencia um local na memória que pode ter sido dado a outra pessoa — liberando alguma memória enquanto preserva um ponteiro para essa memória. Em Rust, por outro lado, o compilador garante que as referências nunca serão referências pendentes: se você tem uma referência a alguns dados, o compilador garantirá que os dados não sairão do escopo antes que a referência aos dados o faça.

Vamos tentar criar uma referência pendente para ver como o Rust as impede com um erro em tempo de compilação:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

Aqui está o erro:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

Esta mensagem de erro se refere a um recurso que ainda não abordamos: tempos de vida (lifetimes). Discutiremos os tempos de vida em detalhes no Capítulo 10. Mas, se você desconsiderar as partes sobre tempos de vida, a mensagem contém a chave para o porquê esse código é um problema:

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

Vamos analisar mais de perto exatamente o que está acontecendo em cada estágio do nosso código `dangle`:

    // src/main.rs
    fn dangle() -> &String { // dangle retorna uma referência a uma String

        let s = String::from("hello"); // s é uma nova String

        &s // nós retornamos uma referência à String, s
    } // Aqui, s sai do escopo e é descartada, então sua memória desaparece
      // Perigo!

Como `s` é criado dentro de `dangle`, quando o código de `dangle` é finalizado, `s` será desalocado. Mas tentamos retornar uma referência a ela. Isso significa que essa referência estaria apontando para uma `String` inválida. Isso não é bom! Rust não nos deixará fazer isso.

A solução aqui é retornar a `String` diretamente:

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

Isso funciona sem problemas. A propriedade é movida para fora e nada é desalocado.
