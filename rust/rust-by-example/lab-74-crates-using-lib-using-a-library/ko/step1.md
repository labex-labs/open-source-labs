# 라이브러리 사용

이 새로운 라이브러리에 크레이트를 연결하려면 `rustc`의 `--extern` 플래그를 사용할 수 있습니다. 그러면 라이브러리와 이름이 같은 모듈 아래에 모든 항목이 가져와집니다. 이 모듈은 일반적으로 다른 모듈과 동일한 방식으로 작동합니다.

```rust
// extern crate rary; // Rust 2015 버전 또는 이전 버전에서 필요할 수 있습니다.

fn main() {
    rary::public_function();

    // 오류! `private_function` 은 private 입니다.
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# 여기서 library.rlib 은 컴파일된 라이브러리의 경로이며,
# 같은 디렉토리에 있다고 가정합니다.
$ rustc executable.rs --extern rary=library.rlib && ./executable
rary 의 `public_function()` 호출
rary 의 `indirect_access()` 호출, 그
> rary 의 `private_function()` 호출
```
