# Expressões `if`

Uma expressão `if` permite que você ramifique seu código dependendo de condições. Você fornece uma condição e então declara: "Se esta condição for atendida, execute este bloco de código. Se a condição não for atendida, não execute este bloco de código."

Crie um novo projeto chamado `branches` no seu diretório `project` para explorar a expressão `if`. No arquivo `src/main.rs`, insira o seguinte:

```bash
cd ~/project
cargo new branches
```

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```

Todas as expressões `if` começam com a palavra-chave `if`, seguida por uma condição. Neste caso, a condição verifica se a variável `number` tem um valor menor que 5. Colocamos o bloco de código a ser executado se a condição for `true` imediatamente após a condição dentro de chaves. Blocos de código associados às condições em expressões `if` são, às vezes, chamados de _braços_ (arms), assim como os braços nas expressões `match` que discutimos em "Comparando o Palpite ao Número Secreto".

Opcionalmente, também podemos incluir uma expressão `else`, que escolhemos fazer aqui, para dar ao programa um bloco de código alternativo para executar caso a condição seja avaliada como `false`. Se você não fornecer uma expressão `else` e a condição for `false`, o programa simplesmente pulará o bloco `if` e passará para o próximo trecho de código.

Tente executar este código; você deve ver a seguinte saída:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was true
```

Vamos tentar mudar o valor de `number` para um valor que torne a condição `false` para ver o que acontece:

```rust
    let number = 7;
```

Execute o programa novamente e observe a saída:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
condition was false
```

Também vale a pena notar que a condição neste código _deve_ ser um `bool`. Se a condição não for um `bool`, obteremos um erro. Por exemplo, tente executar o seguinte código:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

A condição `if` é avaliada como o valor `3` desta vez, e Rust lança um erro:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ expected `bool`, found integer
```

O erro indica que Rust esperava um `bool`, mas encontrou um inteiro. Ao contrário de linguagens como Ruby e JavaScript, Rust não tentará automaticamente converter tipos não-Booleanos em um Booleano. Você deve ser explícito e sempre fornecer `if` com um Booleano como sua condição. Se quisermos que o bloco de código `if` seja executado somente quando um número não for igual a `0`, por exemplo, podemos alterar a expressão `if` para o seguinte:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let number = 3;

    if number != 0 {
        println!("number was something other than zero");
    }
}
```

A execução deste código imprimirá `number was something other than zero`.
