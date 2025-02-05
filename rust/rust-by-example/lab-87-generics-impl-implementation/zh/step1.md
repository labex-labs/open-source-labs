# 实现

与函数类似，实现也需要注意保持泛型。

```rust
struct S; // 具体类型 `S`
struct GenericVal<T>(T); // 泛型类型 `GenericVal`

// GenericVal 的实现，我们在这里显式指定类型参数：
impl GenericVal<f32> {} // 指定 `f32`
impl GenericVal<S> {} // 指定上面定义的 `S`

// `<T>` 必须在类型之前，以保持泛型
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Val 的实现
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// 泛型类型 `T` 的 GenVal 的实现
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
