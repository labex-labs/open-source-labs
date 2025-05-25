# 구조체 가시성

구조체는 필드와 함께 추가적인 가시성 수준을 갖습니다. 기본적으로 필드의 가시성은 비공개 (private) 이며, `pub` 수정자를 사용하여 재정의할 수 있습니다. 이 가시성은 구조체가 정의된 모듈 외부에서 접근될 때만 중요하며, 정보를 숨기는 목적 (캡슐화) 을 가지고 있습니다.

```rust
mod my {
    // 제네릭 타입 `T` 의 공개 필드를 가진 공개 구조체
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // 제네릭 타입 `T` 의 비공개 필드를 가진 공개 구조체
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // 공개 생성자 메서드
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // 공개 필드를 가진 공개 구조체는 일반적으로 생성할 수 있습니다.
    let open_box = my::OpenBox { contents: "공개 정보" };

    // 그리고 그 필드는 일반적으로 접근할 수 있습니다.
    println!("열린 상자에는 다음이 들어 있습니다: {}", open_box.contents);

    // 비공개 필드를 가진 공개 구조체는 필드 이름을 사용하여 생성할 수 없습니다.
    // 오류! `ClosedBox` 에는 비공개 필드가 있습니다.
    //let closed_box = my::ClosedBox { contents: "기밀 정보" };
    // TODO ^ 이 줄을 주석 해제해 보세요

    // 그러나 비공개 필드를 가진 구조체는
    // 공개 생성자를 사용하여 만들 수 있습니다.
    let _closed_box = my::ClosedBox::new("기밀 정보");

    // 그리고 공개 구조체의 비공개 필드에 접근할 수 없습니다.
    // 오류! `contents` 필드는 비공개입니다.
    //println!("닫힌 상자에는 다음이 들어 있습니다: {}", _closed_box.contents);
    // TODO ^ 이 줄을 주석 해제해 보세요
}
```
