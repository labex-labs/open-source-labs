# Unsafe 함수 또는 메서드 호출

unsafe 블록에서 수행할 수 있는 두 번째 유형의 작업은 unsafe 함수를 호출하는 것입니다. Unsafe 함수와 메서드는 일반 함수 및 메서드와 정확히 동일하게 보이지만 정의의 나머지 부분 앞에 추가적인 `unsafe`가 있습니다. 이 컨텍스트에서 `unsafe` 키워드는 Rust 가 이러한 요구 사항을 충족했는지 보장할 수 없기 때문에 이 함수를 호출할 때 준수해야 하는 요구 사항이 함수에 있음을 나타냅니다. `unsafe` 블록 내에서 unsafe 함수를 호출함으로써, 우리는 이 함수의 문서를 읽었고 함수의 계약을 준수할 책임을 진다고 말하는 것입니다.

다음은 본문에서 아무것도 하지 않는 `dangerous`라는 unsafe 함수입니다.

    unsafe fn dangerous() {}

    unsafe {
        dangerous();
    }

별도의 `unsafe` 블록 내에서 `dangerous` 함수를 호출해야 합니다. `unsafe` 블록 없이 `dangerous`를 호출하려고 하면 오류가 발생합니다.

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

`unsafe` 블록을 사용하면 Rust 에 함수의 문서를 읽었고, 이를 적절하게 사용하는 방법을 이해했으며, 함수의 계약을 이행하고 있음을 확인했다고 주장하는 것입니다.

Unsafe 함수의 본문은 효과적으로 `unsafe` 블록이므로, unsafe 함수 내에서 다른 unsafe 작업을 수행하기 위해 다른 `unsafe` 블록을 추가할 필요가 없습니다.
