# Implementação

Assim como as funções, as implementações exigem cuidado para permanecer genéricas.

```rust
struct S; // Tipo concreto `S`
struct GenericVal<T>(T); // Tipo genérico `GenericVal`

// Implementação de GenericVal onde especificamos explicitamente os parâmetros de tipo:
impl GenericVal<f32> {} // Especificar `f32`
impl GenericVal<S> {} // Especificar `S` como definido acima

// `<T>` Deve preceder o tipo para permanecer genérico
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Implementação de Val
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// Implementação de GenVal para um tipo genérico `T`
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
