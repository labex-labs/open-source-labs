# `Option`

Parfois, il est souhaitable de capturer l'échec de certaines parties d'un programme plutôt que d'appeler `panic!` ; cela peut être accompli en utilisant l'enum `Option`.

L'enum `Option<T>` a deux variantes :

- `None`, pour indiquer l'échec ou l'absence de valeur, et
- `Some(value)`, une struct tuple qui encapsule une `value` de type `T`.

```rust
// Une division entière qui ne `panic!` pas
fn checked_division(dividende: i32, diviseur: i32) -> Option<i32> {
    if diviseur == 0 {
        // L'échec est représenté par la variante `None`
        None
    } else {
        // Le résultat est encapsulé dans une variante `Some`
        Some(dividende / diviseur)
    }
}

// Cette fonction gère une division qui peut ne pas réussir
fn try_division(dividende: i32, diviseur: i32) {
    // Les valeurs `Option` peuvent être comparées par motif, tout comme les autres enums
    match checked_division(dividende, diviseur) {
        None => println!("{} / {} a échoué!", dividende, diviseur),
        Some(quotient) => {
            println!("{} / {} = {}", dividende, diviseur, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // Lier `None` à une variable nécessite une annotation de type
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // Décapsuler une variante `Some` extraira la valeur encapsulée.
    println!("{:?} se décapsule en {:?}", optional_float, optional_float.unwrap());

    // Décapsuler une variante `None` provoquera un `panic!`
    println!("{:?} se décapsule en {:?}", none, none.unwrap());
}
```
