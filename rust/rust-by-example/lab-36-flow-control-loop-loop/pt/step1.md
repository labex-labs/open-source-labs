# loop

Rust fornece a palavra-chave `loop` para indicar um loop infinito.

A instrução `break` pode ser usada para sair de um loop a qualquer momento, enquanto a instrução `continue` pode ser usada para pular o restante da iteração e iniciar uma nova.

```rust
fn main() {
    let mut count = 0u32;

    println!("Vamos contar até o infinito!");

    // Loop infinito
    loop {
        count += 1;

        if count == 3 {
            println!("três");

            // Pular o restante desta iteração
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, chega por hoje");

            // Sair deste loop
            break;
        }
    }
}
```
