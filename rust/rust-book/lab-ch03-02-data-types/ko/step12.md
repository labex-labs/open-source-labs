# 잘못된 배열 요소 접근 (Invalid Array Element Access)

배열의 끝을 넘어선 배열의 요소에 접근하려고 하면 어떻게 되는지 살펴보겠습니다. 2 장에서의 숫자 맞추기 게임과 유사하게, 사용자로부터 배열 인덱스를 얻기 위해 이 코드를 실행한다고 가정해 봅시다.

파일 이름: `src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Please enter an array index.");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let index: usize = index
        .trim()
        .parse()
        .expect("Index entered was not a number");

    let element = a[index];

    println!(
        "The value of the element at index {index} is: {element}"
    );
}
```

이 코드는 성공적으로 컴파일됩니다. `cargo run`을 사용하여 이 코드를 실행하고 `0`, `1`, `2`, `3`, 또는 `4`를 입력하면 프로그램은 배열의 해당 인덱스에 있는 해당 값을 출력합니다. 대신 배열의 끝을 넘어선 숫자, 예를 들어 `10`을 입력하면 다음과 같은 출력을 볼 수 있습니다.

    thread 'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

프로그램은 인덱싱 연산에서 잘못된 값을 사용하여 _런타임 (runtime)_ 오류가 발생했습니다. 프로그램은 오류 메시지와 함께 종료되었고 마지막 `println!` 문을 실행하지 않았습니다. 인덱싱을 사용하여 요소에 접근하려고 할 때, Rust 는 지정한 인덱스가 배열 길이보다 작은지 확인합니다. 인덱스가 길이보다 크거나 같으면 Rust 는 패닉 (panic) 합니다. 이 검사는 런타임에 발생해야 합니다. 특히 이 경우에는 컴파일러가 사용자가 나중에 코드를 실행할 때 어떤 값을 입력할지 알 수 없기 때문입니다.

이것은 Rust 의 메모리 안전 (memory safety) 원칙이 작동하는 예입니다. 많은 저수준 언어에서는 이러한 종류의 검사가 수행되지 않으며, 잘못된 인덱스를 제공하면 잘못된 메모리에 접근할 수 있습니다. Rust 는 메모리 접근을 허용하고 계속 진행하는 대신 즉시 종료하여 이러한 종류의 오류로부터 사용자를 보호합니다. 9 장에서는 Rust 의 오류 처리 (error handling) 에 대해 더 자세히 논의하고, 패닉하지 않고 잘못된 메모리 접근을 허용하지 않는 읽기 쉽고 안전한 코드를 작성하는 방법을 설명합니다.
