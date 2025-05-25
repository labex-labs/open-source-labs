# ref 패턴

`let` 바인딩을 통해 패턴 매칭 또는 구조 분해를 수행할 때, `ref` 키워드를 사용하여 구조체/튜플의 필드에 대한 참조를 가져올 수 있습니다. 아래 예제는 이 기능이 유용한 몇 가지 경우를 보여줍니다.

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // 할당의 왼쪽에서 `ref` 차용은
    // 오른쪽에서 `&` 차용과 동일합니다.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 equals ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` 는 구조체를 구조 분해할 때도 유효합니다.
    let _copy_of_x = {
        // `ref_to_x` 는 `point` 의 `x` 필드에 대한 참조입니다.
        let Point { x: ref ref_to_x, y: _ } = point;

        // `point` 의 `x` 필드의 복사본을 반환합니다.
        *ref_to_x
    };

    // `point` 의 가변 복사본
    let mut mutable_point = point;

    {
        // `ref` 는 `mut` 와 함께 사용하여 가변 참조를 가져올 수 있습니다.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // 가변 참조를 통해 `mutable_point` 의 `y` 필드를 변경합니다.
        *mut_ref_to_y = 1;
    }

    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);

    // 포인터를 포함하는 가변 튜플
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // `mutable_tuple` 을 구조 분해하여 `last` 의 값을 변경합니다.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple is {:?}", mutable_tuple);
}
```
