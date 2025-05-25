# 구현

함수와 마찬가지로, 제네릭 특성을 유지하기 위해 구현에도 주의가 필요합니다.

```rust
struct S; // 구체적인 타입 `S`
struct GenericVal<T>(T); // 제네릭 타입 `GenericVal`

// GenericVal 의 구현 (impl) 에서 타입 매개변수를 명시적으로 지정:
impl GenericVal<f32> {} // `f32` 지정
impl GenericVal<S> {} // 위에서 정의된 `S` 지정

// `<T>` 는 제네릭 특성을 유지하기 위해 타입 앞에 와야 함
impl<T> GenericVal<T> {}
```

```rust
struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

// Val 의 구현 (impl)
impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

// 제네릭 타입 `T` 에 대한 GenVal 의 구현 (impl)
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
