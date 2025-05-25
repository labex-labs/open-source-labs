# 소유권과 함수

값을 함수에 전달하는 메커니즘은 값을 변수에 할당하는 경우와 유사합니다. 변수를 함수에 전달하면 할당과 마찬가지로 이동하거나 복사됩니다. 목록 4-3 에는 변수가 범위에 들어가고 나가는 위치를 보여주는 몇 가지 주석이 있는 예가 있습니다.

```rust
    // src/main.rs
    fn main() {
        let s = String::from("hello");  // s 가 범위에 들어옴

        takes_ownership(s);             // s 의 값이 함수로 이동...
                                        // ... 따라서 여기서는 더 이상 유효하지 않음

        let x = 5;                      // x 가 범위에 들어옴

        makes_copy(x);                  // x 는 함수로 이동하지만,
                                        // i32 는 Copy 이므로,
                                        // 그 후에도 x 를 사용하는 것이 괜찮음

    } // 여기서 x 는 범위를 벗어나고, s 도 범위를 벗어납니다. 그러나 s 의 값이 이동되었으므로,
      // 특별한 일은 발생하지 않음

    fn takes_ownership(some_string: String) { // some_string 이 범위에 들어옴
        println!("{some_string}");
    } // 여기서 some_string 은 범위를 벗어나고 `drop` 이 호출됩니다. 백업
      // 메모리가 해제됨

    fn makes_copy(some_integer: i32) { // some_integer 가 범위에 들어옴
        println!("{some_integer}");
    } // 여기서 some_integer 는 범위를 벗어납니다. 특별한 일은 발생하지 않음
```

목록 4-3: 소유권과 범위가 주석 처리된 함수

`takes_ownership` 호출 후 `s`를 사용하려고 하면 Rust 는 컴파일 타임 오류를 발생시킵니다. 이러한 정적 검사는 실수로부터 우리를 보호합니다. `s`와 `x`를 사용하는 코드를 `main`에 추가하여 어디에서 사용할 수 있는지, 소유권 규칙이 이를 방지하는 위치를 확인해 보십시오.
