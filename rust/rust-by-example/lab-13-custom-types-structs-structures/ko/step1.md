# 구조체 (Structures)

`struct` 키워드를 사용하여 생성할 수 있는 구조체는 세 가지 유형이 있습니다.

- 튜플 구조체 (Tuple structs): 기본적으로 명명된 튜플입니다.
- 클래식 C 구조체 (classic C structs)
- 유닛 구조체 (Unit structs): 필드가 없으며 제네릭 (generics) 에 유용합니다.

```rust
// 사용하지 않는 코드에 대한 경고를 숨기는 속성입니다.
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// 유닛 구조체
struct Unit;

// 튜플 구조체
struct Pair(i32, f32);

// 두 개의 필드를 가진 구조체
struct Point {
    x: f32,
    y: f32,
}

// 구조체는 다른 구조체의 필드로 재사용될 수 있습니다.
struct Rectangle {
    // 사각형은 공간에서 왼쪽 상단과 오른쪽 하단 모서리가 어디에 있는지 지정하여 정의할 수 있습니다.
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // 필드 초기화 축약 (field init shorthand) 으로 구조체 생성
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // 디버그 구조체 출력
    println!("{:?}", peter);

    // `Point` 인스턴스화
    let point: Point = Point { x: 10.3, y: 0.4 };

    // point 의 필드에 접근
    println!("point coordinates: ({}, {})", point.x, point.y);

    // 다른 point 의 필드를 사용하여 구조체 업데이트 구문을 사용하여 새로운 point 를 만듭니다.
    let bottom_right = Point { x: 5.2, ..point };

    // `bottom_right.y` 는 `point.y` 와 동일합니다. 왜냐하면 `point` 에서 해당 필드를 사용했기 때문입니다.
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // `let` 바인딩을 사용하여 point 를 분해 (destructure) 합니다.
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // 구조체 인스턴스화도 표현식입니다.
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // 유닛 구조체 인스턴스화
    let _unit = Unit;

    // 튜플 구조체 인스턴스화
    let pair = Pair(1, 0.1);

    // 튜플 구조체의 필드에 접근
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // 튜플 구조체 분해
    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal);
}
```

## 활동 (Activity)

1.  `Rectangle`의 면적을 계산하는 함수 `rect_area`를 추가합니다 (중첩 분해 (nested destructuring) 를 사용해 보세요).
2.  `Point`와 `f32`를 인수로 받아 왼쪽 상단 모서리가 해당 지점에 있고 너비와 높이가 `f32`에 해당하는 `Rectangle`을 반환하는 함수 `square`를 추가합니다.
