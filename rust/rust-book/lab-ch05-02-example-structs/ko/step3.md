# 구조체를 사용한 리팩토링: 더 많은 의미 추가

데이터에 레이블을 지정하여 의미를 추가하기 위해 구조체를 사용합니다. Listing 5-10 과 같이 전체 이름과 부분 이름을 사용하여 사용 중인 튜플을 구조체로 변환할 수 있습니다.

파일 이름: `src/main.rs`

```rust
1 struct Rectangle {
  2 width: u32,
    height: u32,
}

fn main() {
  3 let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );
}

4 fn area(rectangle: &Rectangle) -> u32 {
  5 rectangle.width * rectangle.height
}
```

Listing 5-10: `Rectangle` 구조체 정의

여기서 구조체를 정의하고 이름을 `Rectangle`로 지정했습니다 \[1]. 중괄호 안에서 필드를 `width`와 `height`로 정의했으며, 둘 다 `u32` 타입입니다 \[2]. 그런 다음 `main`에서 너비가 `30`이고 높이가 `50`인 `Rectangle`의 특정 인스턴스를 생성했습니다 \[3].

이제 `area` 함수는 하나의 매개변수로 정의되었으며, 이를 `rectangle`이라고 명명했으며, 해당 타입은 `Rectangle` 인스턴스의 불변 차용 (immutable borrow) 입니다 \[4]. 4 장에서 언급했듯이, 소유권을 가져가는 대신 구조체를 차용하려고 합니다. 이렇게 하면 `main`이 소유권을 유지하고 `rect1`을 계속 사용할 수 있으며, 이것이 함수 시그니처에서 `&`를 사용하고 함수를 호출하는 이유입니다.

`area` 함수는 `Rectangle` 인스턴스의 `width` 및 `height` 필드에 접근합니다 \[5] (차용된 구조체 인스턴스의 필드에 접근해도 필드 값이 이동하지 않음에 유의하세요. 이것이 구조체의 차용을 자주 볼 수 있는 이유입니다). 이제 `area`에 대한 함수 시그니처는 우리가 의미하는 바를 정확히 말합니다. 즉, `Rectangle`의 `width` 및 `height` 필드를 사용하여 면적을 계산합니다. 이는 너비와 높이가 서로 관련되어 있음을 전달하고, 튜플 인덱스 값 `0`과 `1`을 사용하는 대신 값에 대한 설명적인 이름을 제공합니다. 이는 명확성을 위한 승리입니다.
