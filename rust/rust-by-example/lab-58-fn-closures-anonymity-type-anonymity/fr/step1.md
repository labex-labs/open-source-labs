# Anonymat de type

Les closures capturent succinctement les variables des portées entourantes. Est-ce que cela a des conséquences? C'est certainement le cas. Observez comment utiliser une closure comme paramètre de fonction nécessite des \[types génériques\], ce qui est nécessaire en raison de la manière dont elles sont définies :

```rust
// `F` doit être générique.
fn apply<F>(f: F) where
    F: FnOnce() {
    f();
}
```

Lorsqu'une closure est définie, le compilateur crée implicitement une nouvelle structure anonyme pour stocker les variables capturées à l'intérieur, tout en implémentant la fonctionnalité via l'un des `traits` : `Fn`, `FnMut` ou `FnOnce` pour ce type inconnu. Ce type est assigné à la variable qui est stockée jusqu'à l'appel.

Puisque ce nouveau type est de type inconnu, toute utilisation dans une fonction nécessitera des types génériques. Cependant, un paramètre de type non borné `<T>` serait toujours ambigu et ne serait pas autorisé. Ainsi, être limité par l'un des `traits` : `Fn`, `FnMut` ou `FnOnce` (qu'il implémente) est suffisant pour spécifier son type.

```rust
// `F` doit implémenter `Fn` pour une closure qui ne prend
// pas d'entrées et ne renvoie rien - exactement ce qui est
// requis pour `print`.
fn apply<F>(f: F) where
    F: Fn() {
    f();
}

fn main() {
    let x = 7;

    // Capture `x` dans un type anonyme et implémente
    // `Fn` pour lui. Stocke-le dans `print`.
    let print = || println!("{}", x);

    apply(print);
}
```
