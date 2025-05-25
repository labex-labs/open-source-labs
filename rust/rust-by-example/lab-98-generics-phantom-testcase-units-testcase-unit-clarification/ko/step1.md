# 테스트 케이스: 단위 명확화

단위 변환의 유용한 방법은 Phantom 타입 매개변수를 사용하여 `Add` 트레이트를 구현함으로써 살펴볼 수 있습니다. 아래에서 `Add` 트레이트를 살펴봅니다.

```rust
// 이 구조는 다음을 강제합니다: `Self + RHS = Output`
// 여기서 RHS 는 구현에서 명시되지 않으면 기본적으로 Self 로 간주됩니다.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` 은 `T<U> + T<U> = T<U>`가 되도록 `T<U>` 여야 합니다.
impl<U> Add for T<U> {
    type Output = T<U>;
    ...
}
```

전체 구현:

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// 단위 유형을 정의하기 위해 빈 열거형을 만듭니다.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` 는 Phantom 타입 매개변수 `Unit` 을 가진 유형이며, 길이 유형 (즉, `f64`) 에 대해 일반적이지 않습니다.
///
/// `f64` 는 이미 `Clone` 및 `Copy` 트레이트를 구현합니다.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// `Add` 트레이트는 `+` 연산자의 동작을 정의합니다.
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() 는 합계를 포함하는 새 `Length` 구조체를 반환합니다.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` 는 `f64` 에 대한 `Add` 구현을 호출합니다.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // `one_foot` 는 Phantom 타입 매개변수 `Inch` 를 갖도록 지정합니다.
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` 는 Phantom 타입 매개변수 `Mm` 를 갖습니다.
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` 는 `Length<Unit>` 에 대해 구현한 `add()` 메서드를 호출합니다.
    //
    // `Length` 가 `Copy` 를 구현하기 때문에 `add()` 는 `one_foot` 와 `one_meter` 를 소비하지 않고 복사하여 `self` 와 `rhs` 에 넣습니다.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // 덧셈이 작동합니다.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // 의미 없는 연산은 예상대로 실패합니다.
    // 컴파일 타임 오류: 형식 불일치.
    //let one_feter = one_foot + one_meter;
}
```
