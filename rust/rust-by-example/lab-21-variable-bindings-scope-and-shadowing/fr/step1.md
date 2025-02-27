# Portée et ombrage

Les liaisons de variables ont une portée et sont contraintes à exister dans un _bloc_. Un bloc est une collection d'instructions entourées de parenthèses `{}`.

```rust
fn main() {
    // Cette liaison existe dans la fonction principale
    let long_lived_binding = 1;

    // Ceci est un bloc, et a une portée plus restreinte que la fonction principale
    {
        // Cette liaison n'existe que dans ce bloc
        let short_lived_binding = 2;

        println!("inner short: {}", short_lived_binding);
    }
    // Fin du bloc

    // Erreur! `short_lived_binding` n'existe pas dans cette portée
    println!("outer short: {}", short_lived_binding);
    // FIXME ^ Commenter cette ligne

    println!("outer long: {}", long_lived_binding);
}
```

De plus, l'ombrage de variables est autorisé.

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("before being shadowed: {}", shadowed_binding);

        // Cette liaison *ombrage* la liaison externe
        let shadowed_binding = "abc";

        println!("shadowed in inner block: {}", shadowed_binding);
    }
    println!("outside inner block: {}", shadowed_binding);

    // Cette liaison *ombrage* la liaison précédente
    let shadowed_binding = 2;
    println!("shadowed in outer block: {}", shadowed_binding);
}
```
