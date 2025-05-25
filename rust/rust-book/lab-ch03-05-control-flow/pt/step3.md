# Lidando com Múltiplas Condições com `else if`

Você pode usar múltiplas condições combinando `if` e `else` em uma expressão `else if`. Por exemplo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

Este programa tem quatro caminhos possíveis que pode seguir. Após executá-lo, você deve ver a seguinte saída:

```bash
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/branches`
number is divisible by 3
```

Quando este programa é executado, ele verifica cada expressão `if` por sua vez e executa o primeiro corpo para o qual a condição é avaliada como `true`. Observe que, embora 6 seja divisível por 2, não vemos a saída `number is divisible by 2`, nem vemos o texto `number is not divisible by 4, 3, or 2` do bloco `else`. Isso ocorre porque Rust executa apenas o bloco para a primeira condição `true`, e assim que encontra uma, nem sequer verifica o restante.

Usar muitas expressões `else if` pode sobrecarregar seu código, então, se você tiver mais de uma, pode querer refatorar seu código. O Capítulo 6 descreve uma poderosa construção de ramificação do Rust chamada `match` para esses casos.
