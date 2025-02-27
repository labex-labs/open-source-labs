# loop

Rust fournit un mot clé `loop` pour indiquer une boucle infinie.

L'instruction `break` peut être utilisée pour sortir d'une boucle à tout moment, tandis que l'instruction `continue` peut être utilisée pour sauter le reste de l'itération et en démarrer une nouvelle.

```rust
fn main() {
    let mut count = 0u32;

    println!("Commençons à compter jusqu'à l'infini!");

    // Boucle infinie
    loop {
        count += 1;

        if count == 3 {
            println!("trois");

            // Sauter le reste de cette itération
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("OK, c'est assez");

            // Sortir de cette boucle
            break;
        }
    }
}
```
