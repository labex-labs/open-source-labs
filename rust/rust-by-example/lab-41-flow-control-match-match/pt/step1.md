# match

O Rust fornece correspondência de padrões através da palavra-chave `match`, que pode ser usada como um `switch` em C. O primeiro ramo correspondente é avaliado e todos os valores possíveis devem ser cobertos.

```rust
fn main() {
    let number = 13;
    // TODO ^ Tente diferentes valores para `number`

    println!("Tell me about {}", number);
    match number {
        // Correspondência a um único valor
        1 => println!("Um!"),
        // Correspondência a vários valores
        2 | 3 | 5 | 7 | 11 => println!("Este é um número primo"),
        // TODO ^ Tente adicionar 13 à lista de valores primos
        // Correspondência a um intervalo inclusivo
        13..=19 => println!("Um número dos adolescentes"),
        // Lidar com o restante dos casos
        _ => println!("Não é especial"),
        // TODO ^ Tente comentar este ramo de captura-todos
    }

    let boolean = true;
    // Match também é uma expressão
    let binary = match boolean {
        // Os ramos de um match devem cobrir todos os valores possíveis
        false => 0,
        true => 1,
        // TODO ^ Tente comentar um destes ramos
    };

    println!("{} -> {}", boolean, binary);
}
```
