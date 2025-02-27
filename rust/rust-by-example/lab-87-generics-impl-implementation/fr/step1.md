# Implémentation

De manière similaire aux fonctions, les implémentations nécessitent des précautions pour rester génériques.

```rust
struct S; // Type concret `S`
struct GenericVal<T>(T); // Type générique `GenericVal`

// Impl de GenericVal où nous spécifions explicitement les paramètres de type :
impl GenericVal<f32> {} // Spécifier `f32`
impl GenericVal<S> {} // Spécifier `S` tel que défini ci-dessus

// `<T>` Doit précéder le type pour rester générique
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Impl de Val
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// Impl de GenVal pour un type générique `T`
impl<T> GenVal<T> {
    fn value(&self) -> &T {
        &self.gen_val
    }
}

fn main() {
    let x = Val { val: 3.0 };
    let y = GenVal { gen_val: 3i32 };

    println!("{}, {}", x.value(), y.value());
}
```
