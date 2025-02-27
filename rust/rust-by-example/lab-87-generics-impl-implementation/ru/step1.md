# Реализация

Похоже на функции, реализации требуют тщательного подхода, чтобы оставаться обобщенными.

```rust
struct S; // Конкретный тип `S`
struct GenericVal<T>(T); // Обобщенный тип `GenericVal`

// Реализация GenericVal, где мы явно указываем параметры типа:
impl GenericVal<f32> {} // Указываем `f32`
impl GenericVal<S> {} // Указываем `S`, определенный выше

// `<T>` должен предшествовать типу, чтобы оставаться обобщенным
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Реализация Val
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// Реализация GenVal для обобщенного типа `T`
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
