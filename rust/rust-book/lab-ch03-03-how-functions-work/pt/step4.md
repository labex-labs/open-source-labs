# Funções com Valores de Retorno

As funções podem retornar valores para o código que as chama. Não nomeamos valores de retorno, mas devemos declarar seu tipo após uma seta (`->`). Em Rust, o valor de retorno da função é sinônimo do valor da expressão final no bloco do corpo de uma função. Você pode retornar antecipadamente de uma função usando a palavra-chave `return` e especificando um valor, mas a maioria das funções retorna a última expressão implicitamente. Aqui está um exemplo de uma função que retorna um valor:

Nome do arquivo: `src/main.rs`

```rust
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```

Não há chamadas de função, macros ou mesmo declarações `let` na função `five` --- apenas o número `5` por si só. Essa é uma função perfeitamente válida em Rust. Observe que o tipo de retorno da função também é especificado, como `-> i32`. Tente executar este código; a saída deve ser semelhante a esta:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/functions`
The value of x is: 5
```

O `5` em `five` é o valor de retorno da função, e é por isso que o tipo de retorno é `i32`. Vamos examinar isso com mais detalhes. Existem duas partes importantes: primeiro, a linha `let x = five();` mostra que estamos usando o valor de retorno de uma função para inicializar uma variável. Como a função `five` retorna um `5`, essa linha é a mesma que a seguinte:

```rust
let x = 5;
```

Segundo, a função `five` não tem parâmetros e define o tipo do valor de retorno, mas o corpo da função é um solitário `5` sem ponto e vírgula porque é uma expressão cujo valor queremos retornar.

Vamos ver outro exemplo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

Executar este código imprimirá `The value of x is: 6`. Mas se colocarmos um ponto e vírgula no final da linha contendo `x + 1`, mudando-o de uma expressão para uma declaração, receberemos um erro:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

Compilar este código produz um erro, como segue:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error[E0308]: mismatched types
 --> src/main.rs:7:24
  |
7 | fn plus_one(x: i32) -> i32 {
  |    --------            ^^^ expected `i32`, found `()`
  |    |
  |    implicitly returns `()` as its body has no tail or `return` expression
8 |     x + 1;
  |          - help: remove this semicolon
```

A principal mensagem de erro, `mismatched types` (tipos incompatíveis), revela o problema central com este código. A definição da função `plus_one` diz que ela retornará um `i32`, mas as declarações não avaliam para um valor, o que é expresso por `()`, o tipo unitário. Portanto, nada é retornado, o que contradiz a definição da função e resulta em um erro. Nesta saída, Rust fornece uma mensagem para possivelmente ajudar a corrigir este problema: ele sugere remover o ponto e vírgula, o que corrigiria o erro.
