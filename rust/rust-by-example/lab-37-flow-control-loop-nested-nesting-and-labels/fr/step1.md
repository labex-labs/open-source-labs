# Imbrication et étiquettes

Il est possible de `break` ou de `continue` les boucles externes lorsqu'on traite de boucles imbriquées. Dans ces cas, les boucles doivent être annotées avec une `'étiquette`, et l'étiquette doit être passée à l'instruction `break`/`continue`.

```rust
#![allow(unreachable_code)]

fn main() {
    'outer: loop {
        println!("Entré dans la boucle externe");

        'inner: loop {
            println!("Entré dans la boucle interne");

            // Cela ne ferait que rompre la boucle interne
            //break;

            // Cela rompt la boucle externe
            break 'outer;
        }

        println!("Ce point ne sera jamais atteint");
    }

    println!("Sorti de la boucle externe");
}
```
