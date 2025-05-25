# 별칭

`type` 문을 사용하여 기존 타입에 새로운 이름을 줄 수 있습니다. 타입은 `UpperCamelCase` 이름을 가져야 하며, 그렇지 않으면 컴파일러가 경고를 발생시킵니다. 이 규칙의 예외는 기본 타입 (`usize`, `f32` 등) 입니다.

```rust
// `NanoSecond`, `Inch`, `U64` 는 `u64` 의 새로운 이름입니다.
type NanoSecond = u64;
type Inch = u64;
type U64 = u64;

fn main() {
    // `NanoSecond` = `Inch` = `U64` = `u64`.
    let nanoseconds: NanoSecond = 5 as U64;
    let inches: Inch = 2 as U64;

    // 별칭은 *새로운 타입*이 아니므로 추가적인 타입 안전성을 제공하지 않습니다.
    println!("{} 나노초 + {} 인치 = {} 단위?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

별칭의 주요 용도는 반복적인 코드를 줄이는 것입니다. 예를 들어, `io::Result<T>` 타입은 `Result<T, io::Error>` 타입의 별칭입니다.
