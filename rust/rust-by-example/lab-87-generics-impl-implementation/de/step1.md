# Implementierung

Ähnlich wie Funktionen erfordern Implementierungen Sorgfalt, um generisch zu bleiben.

```rust
struct S; // Konkreter Typ `S`
struct GenericVal<T>(T); // Generischer Typ `GenericVal`

// Implementierung von GenericVal, bei der wir die Typparameter explizit angeben:
impl GenericVal<f32> {} // Geben Sie `f32` an
impl GenericVal<S> {} // Geben Sie `S` wie oben definiert an

// `<T>` Muss dem Typ vorausgehen, um generisch zu bleiben
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Implementierung von Val
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// Implementierung von GenVal für einen generischen Typ `T`
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
