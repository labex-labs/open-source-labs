# 제네릭 타입 매개변수, 트레이트 바운드, 그리고 생명주기를 함께 사용하기

제네릭 타입 매개변수, 트레이트 바운드, 그리고 생명주기를 모두 하나의 함수에서 지정하는 구문을 간략하게 살펴보겠습니다!

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

이것은 Listing 10-21 의 `longest` 함수로, 두 개의 문자열 슬라이스 중 더 긴 것을 반환합니다. 하지만 이제 `T`라는 제네릭 타입의 `ann`이라는 추가 매개변수가 있으며, `where` 절에 지정된 대로 `Display` 트레이트를 구현하는 모든 타입으로 채울 수 있습니다. 이 추가 매개변수는 `{}`를 사용하여 출력되므로, `Display` 트레이트 바운드가 필요합니다. 생명주기는 일종의 제네릭이므로, 생명주기 매개변수 `'a`와 제네릭 타입 매개변수 `T`의 선언은 함수 이름 뒤의 꺾쇠 괄호 안의 동일한 목록에 들어갑니다.
