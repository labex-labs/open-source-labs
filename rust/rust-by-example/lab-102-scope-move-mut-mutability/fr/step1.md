# Mutabilité

La mutabilité des données peut être modifiée lorsque la propriété est transférée.

```rust
fn main() {
    let immutable_box = Box::new(5u32);

    println!("immutable_box contains {}", immutable_box);

    // Erreur de mutabilité
    //*immutable_box = 4;

    // *Déplacez* la boîte, modifiant la propriété (et la mutabilité)
    let mut mutable_box = immutable_box;

    println!("mutable_box contains {}", mutable_box);

    // Modifiez le contenu de la boîte
    *mutable_box = 4;

    println!("mutable_box now contains {}", mutable_box);
}
```
