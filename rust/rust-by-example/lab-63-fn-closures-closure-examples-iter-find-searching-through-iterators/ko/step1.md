# 반복자를 통한 검색

`Iterator::find`는 반복자를 반복하고 특정 조건을 만족하는 첫 번째 값을 검색하는 함수입니다. 어떤 값도 조건을 만족하지 않으면 `None`을 반환합니다. 함수 시그니처는 다음과 같습니다.

```rust
pub trait Iterator {
    // 반복되는 타입.
    type Item;

    // `find` 는 `&mut self`를 받아 호출자는 참조 및 수정될 수 있지만 소비될 수는 없습니다.
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` 는 캡처된 변수가 최대 수정될 수 있지만 소비될 수는 없습니다. `&Self::Item` 은 클로저에 인수를 참조로 전달한다는 것을 나타냅니다.
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` 는 `&i32` 를 반환합니다.
    let mut iter = vec1.iter();
    // `into_iter()` 는 `i32` 를 반환합니다.
    let mut into_iter = vec2.into_iter();

    // `iter()` 는 `&i32` 를 반환하고, 항목 중 하나를 참조하려면 `&&i32` 를 `i32` 로 해체해야 합니다.
    println!("vec1 에서 2 찾기: {:?}", iter.find(|&&x| x == 2));
    // `into_iter()` 는 `i32` 를 반환하고, 항목 중 하나를 참조하려면 `&i32` 를 `i32` 로 해체해야 합니다.
    println!("vec2 에서 2 찾기: {:?}", into_iter.find(|&x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` 는 `&&i32` 를 반환합니다.
    println!("array1 에서 2 찾기: {:?}", array1.iter().find(|&&x| x == 2));
    // `into_iter()` 는 `&i32` 를 반환합니다.
    println!("array2 에서 2 찾기: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find`는 항목에 대한 참조를 제공합니다. 하지만 항목의 *인덱스*를 원한다면 `Iterator::position`을 사용하십시오.

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // `iter()` 는 `&i32` 를 반환하고 `position()` 은 참조를 받지 않으므로 `&i32` 를 `i32` 로 해체해야 합니다.
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // `into_iter()` 는 `i32` 를 반환하고 `position()` 은 참조를 받지 않으므로 해체할 필요가 없습니다.
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```
