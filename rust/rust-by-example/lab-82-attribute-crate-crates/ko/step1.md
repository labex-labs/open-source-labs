# 크레이트

`crate_type` 속성은 컴파일러에게 크레이트가 바이너리인지 라이브러리인지 (그리고 어떤 종류의 라이브러리인지) 알려주는 데 사용되고, `crate_name` 속성은 크레이트의 이름을 설정하는 데 사용됩니다.

그러나 Cargo(Rust 패키지 관리자) 를 사용할 때 `crate_type` 및 `crate_name` 속성은 **전혀** 효과가 없다는 점에 유의하는 것이 중요합니다. Cargo 는 대부분의 Rust 프로젝트에서 사용되기 때문에 `crate_type` 및 `crate_name`의 실제 사용 사례는 상대적으로 제한적입니다.

```rust
// 이 크레이트는 라이브러리입니다.
#![crate_type = "lib"]
// 라이브러리의 이름은 "rary"입니다.
#![crate_name = "rary"]

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

`crate_type` 속성이 사용되면 `rustc`에 `--crate-type` 플래그를 전달할 필요가 없습니다.

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
