# Clone (복제)

리소스를 다룰 때, 기본 동작은 할당 또는 함수 호출 중에 리소스를 이전하는 것입니다. 하지만 때로는 리소스의 복사본을 만들어야 할 필요가 있습니다.

`Clone` 트레이트는 바로 이 작업을 수행하는 데 도움을 줍니다. 가장 일반적으로, `Clone` 트레이트에 의해 정의된 `.clone()` 메서드를 사용할 수 있습니다.

```rust
// 리소스가 없는 유닛 구조체
#[derive(Debug, Clone, Copy)]
struct Unit;

// `Clone` 트레이트를 구현하는 리소스가 있는 튜플 구조체
#[derive(Clone, Debug)]
struct Pair(Box<i32>, Box<i32>);

fn main() {
    // `Unit` 인스턴스화
    let unit = Unit;
    // `Unit` 복사, 이동할 리소스가 없음
    let copied_unit = unit;

    // 두 `Unit` 모두 독립적으로 사용 가능
    println!("original: {:?}", unit);
    println!("copy: {:?}", copied_unit);

    // `Pair` 인스턴스화
    let pair = Pair(Box::new(1), Box::new(2));
    println!("original: {:?}", pair);

    // `pair` 를 `moved_pair` 로 이동, 리소스 이동
    let moved_pair = pair;
    println!("moved: {:?}", moved_pair);

    // 오류! `pair` 는 리소스를 잃었습니다.
    //println!("original: {:?}", pair);
    // TODO ^ 이 줄의 주석을 해제해 보세요

    // `moved_pair` 를 `cloned_pair` 로 복제 (리소스 포함)
    let cloned_pair = moved_pair.clone();
    // std::mem::drop 을 사용하여 원래 pair 를 삭제
    drop(moved_pair);

    // 오류! `moved_pair` 가 삭제되었습니다.
    //println!("copy: {:?}", moved_pair);
    // TODO ^ 이 줄의 주석을 해제해 보세요

    // .clone() 의 결과는 여전히 사용 가능합니다!
    println!("clone: {:?}", cloned_pair);
}
```
