# while

A palavra-chave `while` pode ser usada para executar um loop enquanto uma condição for verdadeira.

Vamos escrever o famoso FizzBuzz usando um loop `while`.

```rust
fn main() {
    // Uma variável contadora
    let mut n = 1;

    // Loop enquanto `n` for menor que 101
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // Incrementa o contador
        n += 1;
    }
}
```
