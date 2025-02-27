# Vérifications de correspondance

On peut ajouter une _vérification de correspondance_ (`match` _guard_) pour filtrer la branche.

```rust
#[allow(dead_code)]
enum Temperature {
    Celsius(i32),
    Fahrenheit(i32),
}

fn main() {
    let temperature = Temperature::Celsius(35);
    // ^ TODO essayez différentes valeurs pour `temperature`

    match temperature {
        Temperature::Celsius(t) if t > 30 => println!("{}C est au-dessus de 30 degrés Celsius", t),
        // La partie `if condition` ^ est une vérification de correspondance
        Temperature::Celsius(t) => println!("{}C est en-dessous de 30 degrés Celsius", t),

        Temperature::Fahrenheit(t) if t > 86 => println!("{}F est au-dessus de 86 degrés Fahrenheit", t),
        Temperature::Fahrenheit(t) => println!("{}F est en-dessous de 86 degrés Fahrenheit", t),
    }
}
```

Notez que le compilateur ne prendra pas en compte les conditions de vérification de correspondance lors de la vérification si tous les motifs sont couverts par l'expression `match`.

```rust
fn main() {
    let number: u8 = 4;

    match number {
        i if i == 0 => println!("Zero"),
        i if i > 0 => println!("Plus grand que zéro"),
        // _ => unreachable!("Ne devrait jamais arriver."),
        // TODO ^ décommentez pour corriger la compilation
    }
}
```
