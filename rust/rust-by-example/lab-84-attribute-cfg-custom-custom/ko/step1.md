# 사용자 정의 조건

`target_os`와 같은 일부 조건은 `rustc`에서 암시적으로 제공되지만, 사용자 정의 조건은 `--cfg` 플래그를 사용하여 `rustc`에 전달해야 합니다.

```rust
#[cfg(some_condition)]
fn conditional_function() {
    println!("조건 충족!");
}

fn main() {
    conditional_function();
}
```

사용자 정의 `cfg` 플래그 없이 이 코드를 실행해보세요.

사용자 정의 `cfg` 플래그를 사용하면:

```shell
$ rustc --cfg some_condition custom.rs && ./custom
조건 충족!
```
