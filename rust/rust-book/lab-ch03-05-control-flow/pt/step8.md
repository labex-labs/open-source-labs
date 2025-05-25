# Rótulos de Loop para Desambiguar Entre Múltiplos Loops

Se você tiver loops dentro de loops, `break` e `continue` se aplicam ao loop mais interno naquele ponto. Você pode, opcionalmente, especificar um _rótulo de loop_ em um loop que você pode então usar com `break` ou `continue` para especificar que essas palavras-chave se aplicam ao loop rotulado em vez do loop mais interno. Rótulos de loop devem começar com uma aspa simples. Aqui está um exemplo com dois loops aninhados:

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

O loop externo tem o rótulo `'counting_up`, e ele contará de 0 a 2. O loop interno sem um rótulo conta de 10 a 9. O primeiro `break` que não especifica um rótulo sairá apenas do loop interno. A instrução `break 'counting_up;` sairá do loop externo. Este código imprime:

       Compiling loops v0.1.0 (file:///projects/loops)
        Finished dev [unoptimized + debuginfo] target(s) in 0.58s
         Running `target/debug/loops`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
