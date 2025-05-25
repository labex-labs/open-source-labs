# Loops Condicionais com `while`

Um programa frequentemente precisará avaliar uma condição dentro de um loop. Enquanto a condição for `true`, o loop é executado. Quando a condição deixa de ser `true`, o programa chama `break`, interrompendo o loop. É possível implementar um comportamento como este usando uma combinação de `loop`, `if`, `else` e `break`; você pode tentar isso agora em um programa, se desejar. No entanto, esse padrão é tão comum que o Rust tem uma construção de linguagem embutida para isso, chamada de loop `while`. Na Listagem 3-3, usamos `while` para executar o programa três vezes, contando regressivamente a cada vez e, em seguida, após o loop, imprimimos uma mensagem e saímos.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

Listagem 3-3: Usando um loop `while` para executar código enquanto uma condição é avaliada como `true`

Essa construção elimina muita aninhamento que seria necessário se você usasse `loop`, `if`, `else` e `break`, e é mais clara. Enquanto uma condição for avaliada como `true`, o código é executado; caso contrário, ele sai do loop.
