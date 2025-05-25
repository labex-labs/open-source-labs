# 라이브러리 생성

라이브러리를 생성하고 다른 크레이트에 연결하는 방법을 살펴봅니다.

`rary.rs` 파일에서:

```rust
pub fn public_function() {
    println!("called rary's `public_function()`");
}

fn private_function() {
    println!("called rary's `private_function()`");
}

pub fn indirect_access() {
    print!("called rary's `indirect_access()`, that\n> ");

    private_function();
}
```

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

라이브러리는 "lib" 접두사로 시작하며, 기본적으로 크레이트 파일 이름으로 명명됩니다. 하지만 `rustc`에 `--crate-name` 옵션을 전달하거나 [`crate_name` 속성]을 사용하여 이 기본 이름을 변경할 수 있습니다.
