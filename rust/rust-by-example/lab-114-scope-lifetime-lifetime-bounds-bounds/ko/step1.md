# 바운드 (Bounds)

제네릭 타입이 바운드될 수 있는 것처럼, 라이프타임 (자체적으로 제네릭) 도 바운드를 사용합니다. `:` 문자는 여기에서 약간 다른 의미를 가지지만, `+`는 동일합니다. 다음을 어떻게 읽는지 주목하십시오:

1.  `T: 'a`: `T` 내의 _모든_ 참조는 라이프타임 `'a`보다 오래 지속되어야 합니다.
2.  `T: Trait + 'a`: 타입 `T`는 트레이트 `Trait`를 구현해야 하며, `T` 내의 _모든_ 참조는 `'a`보다 오래 지속되어야 합니다.

아래 예제는 `where` 키워드 뒤에 사용된 위의 구문을 보여줍니다:

```rust
use std::fmt::Debug; // Trait to bound with.

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` contains a reference to a generic type `T` that has
// an unknown lifetime `'a`. `T` is bounded such that any
// *references* in `T` must outlive `'a`. Additionally, the lifetime
// of `Ref` may not exceed `'a`.

// A generic function which prints using the `Debug` trait.
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t is {:?}", t);
}

// Here a reference to `T` is taken where `T` implements
// `Debug` and all *references* in `T` outlive `'a`. In
// addition, `'a` must outlive the function.
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t is {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}
```
