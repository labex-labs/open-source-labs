# 테스트 케이스: 빈 바운드

바운드가 작동하는 방식의 결과로, 특정 기능이 없는 트레이트라도 바운드로 사용할 수 있습니다. `Eq`와 `Copy`는 `std` 라이브러리에서 이러한 예시입니다.

```rust
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// 이러한 함수는 이러한 트레이트를 구현하는 타입에 대해서만 유효합니다.
// 트레이트가 비어 있다는 사실은 무관합니다.
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // `red()` 는 바운드 때문에 푸른제비나 그 반대의 경우에는 작동하지 않습니다.
    println!("빨간색 딱따구리는 {}", red(&cardinal));
    println!("푸른제비는 {}", blue(&blue_jay));
    //println!("칠면조는 {}", red(&_turkey));
    // ^ TODO: 이 줄을 주석 해제해 보세요.
}
```
