# `cfg`

구성 조건 검사는 두 가지 다른 연산자를 통해 가능합니다.

- `cfg` 속성: 속성 위치의 `#[cfg(...)]`
- `cfg!` 매크로: 부울 표현식의 `cfg!(...)`

전자는 조건부 컴파일을 활성화하는 반면, 후자는 런타임 검사를 허용하는 `true` 또는 `false` 리터럴로 조건부로 평가됩니다. 두 가지 모두 동일한 인수 구문을 사용합니다.

`cfg!`는 `#[cfg]`와 달리 코드를 제거하지 않고 오직 참 또는 거짓으로 평가됩니다. 예를 들어, `cfg!`가 조건으로 사용되는 경우 if/else 표현식의 모든 블록은 `cfg!`의 평가 결과와 관계없이 유효해야 합니다.

```rust
// 대상 OS 가 linux 인 경우에만 이 함수가 컴파일됩니다.
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!");
}

// 대상 OS 가 linux 가 *아닌* 경우에만 이 함수가 컴파일됩니다.
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux!");
}

fn main() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* linux!");
    }
}
```
