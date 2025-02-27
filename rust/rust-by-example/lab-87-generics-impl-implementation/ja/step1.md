# 実装

関数と同様に、実装には汎用性を維持するために注意が必要です。

```rust
struct S; // 具体的な型 `S`
struct GenericVal<T>(T); // 汎用型 `GenericVal`

// 型パラメータを明示的に指定する GenericVal の impl:
impl GenericVal<f32> {} // `f32` を指定
impl GenericVal<S> {} // 上で定義された `S` を指定

// `<T>` は汎用性を維持するために型の前に置かなければなりません
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Val の impl
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// 汎用型 `T` の GenVal の impl
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
