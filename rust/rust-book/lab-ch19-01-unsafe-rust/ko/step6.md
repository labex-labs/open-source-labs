# extern 함수를 사용하여 외부 코드 호출

때로는 Rust 코드가 다른 언어로 작성된 코드와 상호 작용해야 할 수 있습니다. 이를 위해 Rust 에는 *Foreign Function Interface (FFI, 외부 함수 인터페이스)*를 생성하고 사용하는 것을 용이하게 하는 `extern` 키워드가 있습니다. FFI 는 프로그래밍 언어가 함수를 정의하고 다른 (외부) 프로그래밍 언어가 해당 함수를 호출할 수 있도록 하는 방법입니다.

Listing 19-8 은 C 표준 라이브러리의 `abs` 함수와의 통합을 설정하는 방법을 보여줍니다. `extern` 블록 내에서 선언된 함수는 Rust 코드에서 호출하기 항상 unsafe 합니다. 그 이유는 다른 언어는 Rust 의 규칙과 보장을 적용하지 않으며 Rust 는 이를 확인할 수 없으므로 안전을 보장하는 책임은 프로그래머에게 있기 때문입니다.

Filename: `src/main.rs`

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!(
            "Absolute value of -3 according to C: {}",
            abs(-3)
        );
    }
}
```

Listing 19-8: 다른 언어로 정의된 `extern` 함수 선언 및 호출

`extern "C"` 블록 내에서 호출하려는 다른 언어의 외부 함수의 이름과 시그니처를 나열합니다. `"C"` 부분은 외부 함수가 사용하는 *application binary interface (ABI, 응용 프로그램 바이너리 인터페이스)*를 정의합니다. ABI 는 어셈블리 수준에서 함수를 호출하는 방법을 정의합니다. `"C"` ABI 는 가장 일반적이며 C 프로그래밍 언어의 ABI 를 따릅니다.

> **다른 언어에서 Rust 함수 호출**
>
> 또한 `extern`을 사용하여 다른 언어가 Rust 함수를 호출할 수 있도록 하는 인터페이스를 만들 수 있습니다. 전체 `extern` 블록을 생성하는 대신, `extern` 키워드를 추가하고 관련 함수의 `fn` 키워드 바로 앞에 사용할 ABI 를 지정합니다. 또한 Rust 컴파일러에게 이 함수의 이름을 망글링하지 않도록 지시하기 위해 `#[no_mangle]` 어노테이션을 추가해야 합니다. *Mangling (맹글링)*은 컴파일러가 함수에 부여한 이름을 다른 이름으로 변경하여 컴파일 프로세스의 다른 부분에서 사용할 수 있도록 더 많은 정보를 포함하지만 사람이 읽기 어렵게 만드는 것입니다. 모든 프로그래밍 언어 컴파일러는 이름을 약간 다르게 맹글링하므로 다른 언어에서 Rust 함수를 명명할 수 있도록 하려면 Rust 컴파일러의 이름 맹글링을 비활성화해야 합니다.
>
> 다음 예제에서는 C 코드로 컴파일되어 C 에서 링크된 후 `call_from_c` 함수를 C 코드에서 접근할 수 있도록 합니다.
>
>     #[no_mangle]
>     pub extern "C" fn call_from_c() {
>         println!("Just called a Rust function from C!");
>     }
>
> 이 `extern` 사용법은 `unsafe`를 필요로 하지 않습니다.
