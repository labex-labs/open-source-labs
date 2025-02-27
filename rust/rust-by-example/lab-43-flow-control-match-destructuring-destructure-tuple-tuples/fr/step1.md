# tuples

Les tuples peuvent être déstructurés dans une instruction `match` comme suit :

```rust
fn main() {
    let triple = (0, -2, 3);
    // TODO ^ Essayez différentes valeurs pour `triple`

    println!("Dites-moi ce que contient {:?}", triple);
    // L'instruction `match` peut être utilisée pour déstructurer un tuple
    match triple {
        // Découpez les deuxième et troisième éléments
        (0, y, z) => println!("Le premier est `0`, `y` vaut {:?} et `z` vaut {:?}", y, z),
        (1,..)  => println!("Le premier est `1` et le reste n'a pas d'importance"),
        (.., 2)  => println!("Le dernier est `2` et le reste n'a pas d'importance"),
        (3,.., 4)  => println!("Le premier est `3`, le dernier est `4` et le reste n'a pas d'importance"),
        // `..` peut être utilisé pour ignorer le reste du tuple
        _      => println!("Il n'importe pas ce que sont les autres éléments"),
        // `_` signifie ne pas lier la valeur à une variable
    }
}
```
