# Bounds

Lorsqu'on travaille avec des génériques, les paramètres de type doivent souvent utiliser des traits comme _bornes_ pour stipuler quelle fonctionnalité un type implémente. Par exemple, l'exemple suivant utilise le trait `Display` pour imprimer et donc il nécessite que `T` soit limité par `Display` ; c'est-à-dire que `T` _doit_ implémenter `Display`.

```rust
// Définit une fonction `printer` qui prend un type générique `T` qui
// doit implémenter le trait `Display`.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

La limitation restreint le générique aux types qui respectent les bornes. C'est-à-dire :

```rust
struct S<T: Display>(T);

// Erreur! `Vec<T>` n'implémente pas `Display`. Cette
// spécialisation échouera.
let s = S(vec![1]);
```

Un autre effet de la limitation est que les instances génériques sont autorisées à accéder aux \[méthodes\] des traits spécifiés dans les bornes. Par exemple :

```rust
// Un trait qui implémente le marqueur d'impression : `{:?}`.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// Le générique `T` doit implémenter `Debug`. Indépendamment
// du type, cela fonctionnera correctement.
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` doit implémenter `HasArea`. Tout type qui répond
// à la contrainte peut accéder à la fonction `area` de `HasArea`.
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Area: {}", area(&_triangle));
    // ^ TODO: Essayez de décommenter cela.
    // | Erreur : Ne implémente ni `Debug` ni `HasArea`.
}
```

Pour information supplémentaire, les clauses `where` peuvent également être utilisées pour appliquer des bornes dans certains cas pour être plus expressif.
