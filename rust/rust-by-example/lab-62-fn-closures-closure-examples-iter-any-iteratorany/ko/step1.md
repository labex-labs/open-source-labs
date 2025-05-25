# Iterator::any

`Iterator::any` 함수는 반복자를 인수로 받아, 반복자의 어떤 요소라도 주어진 조건을 만족하면 `true`를, 그렇지 않으면 `false`를 반환합니다. 함수 시그니처는 다음과 같습니다.

```rust
pub trait Iterator {
    // 반복되는 형식.
    type Item;

    // `any` 는 `&mut self`를 받아 호출자는 대출 및 수정될 수 있지만 소비될 수는 없습니다.
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` 은 캡처된 변수가 최대 수정될 수 있지만 소비될 수는 없습니다. `Self::Item` 은 클로저에 값으로 인수를 전달한다는 것을 나타냅니다.
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` 는 `vec` 에 대해 `&i32` 를 반환합니다. `&i32` 를 `i32` 로 분해합니다.
    println!("2 in vec1: {}", vec1.iter()     .any(|&x| x == 2));
    // `into_iter()` 는 `vec` 에 대해 `i32` 를 반환합니다. 분해가 필요 없습니다.
    println!("2 in vec2: {}", vec2.into_iter().any(|x| x == 2));

    // `iter()` 는 `vec1` 과 그 요소를 단순히 참조만 하므로 다시 사용할 수 있습니다.
    println!("vec1 len: {}", vec1.len());
    println!("vec1 의 첫 번째 요소는: {}", vec1[0]);
    // `into_iter()` 는 `vec2` 와 그 요소를 이동하므로 다시 사용할 수 없습니다.
    // println!("First element of vec2 is: {}", vec2[0]);
    // println!("vec2 len: {}", vec2.len());
    // 위 두 줄을 주석 해제하고 컴파일러 오류를 확인하세요.

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` 는 배열에 대해 `&i32` 를 반환합니다.
    println!("2 in array1: {}", array1.iter()     .any(|&x| x == 2));
    // `into_iter()` 는 배열에 대해 `i32` 를 반환합니다.
    println!("2 in array2: {}", array2.into_iter().any(|x| x == 2));
}
```
