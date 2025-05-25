# 배열/슬라이스

튜플과 마찬가지로 배열과 슬라이스도 이런 식으로 구조 분해할 수 있습니다.

```rust
fn main() {
    // 배열의 값을 변경하거나 슬라이스로 만들어 보세요!
    let array = [1, -2, 6];

    match array {
        // 두 번째와 세 번째 요소를 각 변수에 바인딩합니다.
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // _를 사용하여 단일 값을 무시할 수 있습니다.
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {}이고 array[1] 은 무시되었습니다",
            third
        ),

        // 일부 요소를 바인딩하고 나머지는 무시할 수도 있습니다.
        [-1, second, ..] => println!(
            "array[0] = -1, array[1] = {}이고 나머지 요소들은 무시되었습니다",
            second
        ),
        // 아래 코드는 컴파일되지 않습니다.
        // [-1, second] => ...

        // 또는 다른 배열/슬라이스에 저장할 수 있습니다 (타입은 일치 대상 값의 타입에 따라 달라집니다).
        [3, second, tail @ ..] => println!(
            "array[0] = 3, array[1] = {}이고 나머지 요소들은 {:?}입니다",
            second, tail
        ),

        // 이러한 패턴을 결합하여 예를 들어 첫 번째와 마지막 값을 바인딩하고 나머지 값을 하나의 배열에 저장할 수 있습니다.
        [first, middle @ .., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
