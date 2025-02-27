# Literaux

Les littéraux numériques peuvent être annotés avec un type en ajoutant le type en tant que suffixe. Par exemple, pour spécifier que le littéral `42` doit avoir le type `i32`, écrivez `42i32`.

Le type des littéraux numériques non suffixés dépendra de la manière dont ils sont utilisés. Si aucune contrainte n'existe, le compilateur utilisera `i32` pour les entiers et `f64` pour les nombres à virgule flottante.

```rust
fn main() {
    // Littéraux suffixés, leur type est connu lors de l'initialisation
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Littéraux non suffixés, leur type dépend de la manière dont ils sont utilisés
    let i = 1;
    let f = 1.0;

    // `size_of_val` renvoie la taille d'une variable en octets
    println!("taille de `x` en octets : {}", std::mem::size_of_val(&x));
    println!("taille de `y` en octets : {}", std::mem::size_of_val(&y));
    println!("taille de `z` en octets : {}", std::mem::size_of_val(&z));
    println!("taille de `i` en octets : {}", std::mem::size_of_val(&i));
    println!("taille de `f` en octets : {}", std::mem::size_of_val(&f));
}
```

Il y a quelques concepts utilisés dans le code précédent qui n'ont pas été expliqués encore. Voici une brève explication pour les lecteurs impatients :

- `std::mem::size_of_val` est une fonction, mais appelée avec son _chemin complet_. Le code peut être divisé en unités logiques appelées _modules_. Dans ce cas, la fonction `size_of_val` est définie dans le module `mem`, et le module `mem` est défini dans la _boîte à outils_ `std`. Pour plus de détails, consultez les modules et les boîtes à outils.
