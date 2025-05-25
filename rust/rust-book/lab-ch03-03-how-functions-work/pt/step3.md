# Declarações e Expressões

Os corpos das funções são compostos por uma série de declarações, opcionalmente terminando em uma expressão. Até agora, as funções que cobrimos não incluíram uma expressão final, mas você viu uma expressão como parte de uma declaração. Como Rust é uma linguagem baseada em expressões, esta é uma distinção importante de entender. Outras linguagens não têm as mesmas distinções, então vamos ver o que são declarações e expressões e como suas diferenças afetam os corpos das funções.

- **Declarações**: são instruções que executam alguma ação e não retornam um valor.
- **Expressões**: avaliam para um valor resultante. Vamos ver alguns exemplos.

Na verdade, já usamos declarações e expressões. Criar uma variável e atribuir um valor a ela com a palavra-chave `let` é uma declaração. Na Listagem 3-1, `let y = 6;` é uma declaração.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let y = 6;
}
```

Listagem 3-1: Uma declaração de função `main` contendo uma declaração

Definições de funções também são declarações; todo o exemplo anterior é uma declaração em si.

Declarações não retornam valores. Portanto, você não pode atribuir uma declaração `let` a outra variável, como o código a seguir tenta fazer; você receberá um erro:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = (let y = 6);
}
```

Quando você executa este programa, o erro que você receberá se parece com isto:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for
more information
```

A declaração `let y = 6` não retorna um valor, então não há nada para `x` associar. Isso é diferente do que acontece em outras linguagens, como C e Ruby, onde a atribuição retorna o valor da atribuição. Nessas linguagens, você pode escrever `x = y = 6` e fazer com que tanto `x` quanto `y` tenham o valor `6`; esse não é o caso em Rust.

Expressões avaliam para um valor e compõem a maior parte do restante do código que você escreverá em Rust. Considere uma operação matemática, como `5 + 6`, que é uma expressão que avalia para o valor `11`. Expressões podem fazer parte de declarações: na Listagem 3-1, o `6` na declaração `let y = 6;` é uma expressão que avalia para o valor `6`. Chamar uma função é uma expressão. Chamar uma macro é uma expressão. Um novo bloco de escopo criado com chaves é uma expressão, por exemplo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
  1 let y = {2
        let x = 3;
      3 x + 1
    };

    println!("The value of y is: {y}");
}
```

A expressão \[2] é um bloco que, neste caso, avalia para `4`. Esse valor é associado a `y` como parte da declaração `let` \[1]. Observe a linha sem ponto e vírgula no final \[3], que é diferente da maioria das linhas que você viu até agora. Expressões não incluem pontos e vírgulas finais. Se você adicionar um ponto e vírgula ao final de uma expressão, você a transforma em uma declaração, e ela não retornará um valor. Tenha isso em mente ao explorar os valores de retorno de funções e expressões a seguir.
