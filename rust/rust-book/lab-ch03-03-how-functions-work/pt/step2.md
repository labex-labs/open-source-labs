# Parâmetros

Podemos definir funções para ter _parâmetros_, que são variáveis especiais que fazem parte da assinatura de uma função. Quando uma função tem parâmetros, você pode fornecer a ela valores concretos para esses parâmetros. Tecnicamente, os valores concretos são chamados de _argumentos_, mas em conversas informais, as pessoas tendem a usar as palavras _parâmetro_ e _argumento_ de forma intercambiável, tanto para as variáveis na definição de uma função quanto para os valores concretos passados ​​quando você chama uma função.

Nesta versão de `another_function`, adicionamos um parâmetro:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```

Tente executar este programa; você deve obter a seguinte saída:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 1.21s
     Running `target/debug/functions`
The value of x is: 5
```

A declaração de `another_function` tem um parâmetro chamado `x`. O tipo de `x` é especificado como `i32`. Quando passamos `5` para `another_function`, a macro `println!` coloca `5` onde o par de chaves contendo `x` estava na string de formatação.

Nas assinaturas de funções, você _deve_ declarar o tipo de cada parâmetro. Esta é uma decisão deliberada no design do Rust: exigir anotações de tipo nas definições de funções significa que o compilador quase nunca precisa que você as use em outro lugar no código para descobrir qual tipo você quer dizer. O compilador também é capaz de fornecer mensagens de erro mais úteis se souber quais tipos a função espera.

Ao definir vários parâmetros, separe as declarações de parâmetro com vírgulas, assim:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

Este exemplo cria uma função chamada `print_labeled_measurement` com dois parâmetros. O primeiro parâmetro é chamado `value` e é um `i32`. O segundo é chamado `unit_label` e é do tipo `char`. A função então imprime texto contendo tanto o `value` quanto o `unit_label`.

Vamos tentar executar este código. Substitua o programa atualmente no arquivo `src/main.rs` do seu projeto _functions_ pelo exemplo anterior e execute-o usando `cargo run`:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/functions`
The measurement is: 5h
```

Como chamamos a função com `5` como o valor para `value` e `'h'` como o valor para `unit_label`, a saída do programa contém esses valores.
