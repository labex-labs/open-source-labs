# 반환 값과 범위

반환 값도 소유권을 이전할 수 있습니다. 목록 4-4 는 목록 4-3 과 유사한 주석이 있는, 일부 값을 반환하는 함수의 예제를 보여줍니다.

```rust
    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownership 는 반환 값을
                                            // s1 으로 이동시킴

        let s2 = String::from("hello");     // s2 가 범위에 들어옴

        let s3 = takes_and_gives_back(s2);  // s2 가
                                            // takes_and_gives_back 으로 이동하며,
                                            // 또한 반환 값을 s3 으로 이동시킴
    } // 여기서 s3 은 범위를 벗어나고 삭제됩니다. s2 는 이동되었으므로 아무 일도
      // 일어나지 않습니다. s1 은 범위를 벗어나고 삭제됩니다.

    fn gives_ownership() -> String {             // gives_ownership 는 반환 값을
                                                 // 호출하는 함수로 이동시킴

        let some_string = String::from("yours"); // some_string 이 범위에 들어옴

        some_string                              // some_string 이 반환되고
                                                 // 호출하는 함수로 이동
    }

    // 이 함수는 String 을 받아 String 을 반환합니다.
    fn takes_and_gives_back(a_string: String) -> String { // a_string 이
                                                          // 범위에 들어옴

        a_string  // a_string 이 반환되고 호출하는 함수로 이동
    }
```

목록 4-4: 반환 값의 소유권 이전

변수의 소유권은 매번 동일한 패턴을 따릅니다. 값을 다른 변수에 할당하면 이동합니다. 힙에 데이터를 포함하는 변수가 범위를 벗어나면 데이터의 소유권이 다른 변수로 이동하지 않는 한 `drop`에 의해 값이 정리됩니다.

이것은 작동하지만, 모든 함수마다 소유권을 가져와 반환하는 것은 약간 번거롭습니다. 함수가 값을 사용하도록 하고 소유권을 가져가지 않도록 하려면 어떻게 해야 할까요? 함수 본문에서 반환하려는 데이터 외에도 다시 사용하려면 전달하는 모든 것을 다시 전달해야 한다는 것은 매우 귀찮습니다.

Rust 는 목록 4-5 에 표시된 것처럼 튜플을 사용하여 여러 값을 반환할 수 있습니다.

파일 이름: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() 은 String 의 길이를 반환합니다.

    (s, length)
}
```

목록 4-5: 매개변수의 소유권 반환

그러나 이것은 너무 많은 형식적인 절차이며 일반적인 개념에 비해 많은 작업입니다. 다행히도 Rust 에는 소유권을 이전하지 않고 값을 사용하는 기능인 *참조 (reference)*가 있습니다.
