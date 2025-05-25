# pointers/ref

포인터의 경우, 구조 분해 (destructuring) 와 참조 해제 (dereferencing) 는 C/C++ 와는 다른 개념으로 다르게 사용되므로 구분해야 합니다.

- 참조 해제는 `*`를 사용합니다.
- 구조 분해는 `&`, `ref`, `ref mut`를 사용합니다.

```rust
fn main() {
    // `i32` 타입의 참조를 할당합니다. `&` 는 참조가 할당되었음을 나타냅니다.
    let reference = &4;

    match reference {
        // 만약 `reference` 가 `&val` 과 패턴 일치하면, 다음과 같은 비교가 이루어집니다.
        // `&i32`
        // `&val`
        // ^ 일치하는 `&` 를 제거하면 `i32` 가 `val` 에 할당되어야 합니다.
        &val => println!("구조 분해를 통해 값 가져오기: {:?}", val),
    }

    // `&` 를 피하려면 일치하기 전에 참조를 해제합니다.
    match *reference {
        val => println!("참조 해제를 통해 값 가져오기: {:?}", val),
    }

    // 참조로 시작하지 않으면 어떻게 될까요? `reference` 가 `&` 였던 이유는 오른쪽이 이미 참조였기 때문입니다. 오른쪽이 참조가 아니므로 이것은 참조가 아닙니다.
    let _not_a_reference = 3;

    // 바로 이 목적을 위해 Rust 는 `ref` 를 제공합니다. 이것은 요소에 대한 참조가 생성되도록 할당을 수정합니다. 이 참조가 할당됩니다.
    let ref _is_a_reference = 3;

    // 따라서 참조 없이 2 개의 값을 정의하면 `ref` 와 `ref mut`를 통해 참조를 가져올 수 있습니다.
    let value = 5;
    let mut mut_value = 6;

    // 참조를 생성하기 위해 `ref` 키워드를 사용합니다.
    match value {
        ref r => println!("값에 대한 참조 가져오기: {:?}", r),
    }

    // 유사하게 `ref mut`를 사용합니다.
    match mut_value {
        ref mut m => {
            // 참조를 가져왔습니다. 추가하기 전에 참조를 해제해야 합니다.
            *m += 10;
            println!("10 을 더했습니다. `mut_value`: {:?}", m);
        },
    }
}
```
