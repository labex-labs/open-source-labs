# Implementación

Al igual que con las funciones, las implementaciones requieren atención para seguir siendo genéricas.

```rust
struct S; // Tipo concrete `S`
struct GenericVal<T>(T); // Tipo genérico `GenericVal`

// Implementación de GenericVal donde especificamos explícitamente los parámetros de tipo:
impl GenericVal<f32> {} // Especificar `f32`
impl GenericVal<S> {} // Especificar `S` como se definió anteriormente

// `<T>` Debe preceder al tipo para seguir siendo genérico
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Implementación de Val
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// Implementación de GenVal para un tipo genérico `T`
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
