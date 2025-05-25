# 기본 제네릭 타입 매개변수 및 연산자 오버로딩

제네릭 타입 매개변수를 사용할 때, 제네릭 타입에 대한 기본 구체적인 타입을 지정할 수 있습니다. 이렇게 하면 기본 타입이 작동하는 경우 트레이트를 구현하는 사람이 구체적인 타입을 지정할 필요가 없습니다. `<`PlaceholderType`=`ConcreteType`>` 구문을 사용하여 제네릭 타입을 선언할 때 기본 타입을 지정합니다.

이 기술이 유용한 상황의 훌륭한 예는 *연산자 오버로딩*입니다. 특정 상황에서 연산자 (예: `+`) 의 동작을 사용자 정의할 수 있습니다.

Rust 는 사용자 정의 연산자를 만들거나 임의의 연산자를 오버로딩하는 것을 허용하지 않습니다. 그러나 연산자와 관련된 트레이트를 구현하여 `std::ops`에 나열된 연산과 해당 트레이트를 오버로딩할 수 있습니다. 예를 들어, Listing 19-14 에서 `+` 연산자를 오버로딩하여 두 개의 `Point` 인스턴스를 더합니다. `Point` 구조체에 `Add` 트레이트를 구현하여 이를 수행합니다.

Filename: `src/main.rs`

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

Listing 19-14: `Point` 인스턴스에 대한 `+` 연산자를 오버로딩하기 위해 `Add` 트레이트 구현

`add` 메서드는 두 `Point` 인스턴스의 `x` 값과 두 `Point` 인스턴스의 `y` 값을 더하여 새로운 `Point`를 생성합니다. `Add` 트레이트에는 `add` 메서드에서 반환되는 타입을 결정하는 `Output`이라는 연관 타입이 있습니다.

이 코드의 기본 제네릭 타입은 `Add` 트레이트 내에 있습니다. 다음은 해당 정의입니다.

    trait Add<Rhs=Self> {
        type Output;

        fn add(self, rhs: Rhs) -> Self::Output;
    }

이 코드는 일반적으로 익숙해야 합니다. 하나의 메서드와 연관 타입을 가진 트레이트입니다. 새로운 부분은 `Rhs=Self`입니다. 이 구문은 *기본 타입 매개변수*라고 합니다. `Rhs` 제네릭 타입 매개변수 ("right-hand side"의 약자) 는 `add` 메서드의 `rhs` 매개변수의 타입을 정의합니다. `Add` 트레이트를 구현할 때 `Rhs`에 대한 구체적인 타입을 지정하지 않으면, `Rhs`의 타입은 기본적으로 `Self`가 되며, 이는 `Add`를 구현하는 타입이 됩니다.

`Point`에 대해 `Add`를 구현했을 때, 두 개의 `Point` 인스턴스를 더하고 싶었기 때문에 `Rhs`에 대한 기본값을 사용했습니다. 기본값을 사용하는 대신 `Rhs` 타입을 사용자 정의하려는 `Add` 트레이트 구현의 예를 살펴보겠습니다.

`Millimeters`와 `Meters`라는 두 개의 구조체가 있으며, 서로 다른 단위로 값을 저장합니다. 다른 구조체에서 기존 타입을 얇게 감싸는 것을 *newtype 패턴*이라고 하며, "Using the Newtype Pattern to Implement External Traits on External Types"에서 자세히 설명합니다. 밀리미터 단위의 값을 미터 단위의 값에 더하고 `Add`의 구현이 변환을 올바르게 수행하도록 하려고 합니다. Listing 19-15 와 같이 `Meters`를 `Rhs`로 사용하여 `Millimeters`에 대해 `Add`를 구현할 수 있습니다.

Filename: `src/lib.rs`

```rust
use std::ops::Add;

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

Listing 19-15: `Millimeters`와 `Meters`를 더하기 위해 `Millimeters`에 `Add` 트레이트 구현

`Millimeters`와 `Meters`를 더하려면, `Self`의 기본값을 사용하는 대신 `impl Add<Meters>`를 지정하여 `Rhs` 타입 매개변수의 값을 설정합니다.

기본 타입 매개변수는 주로 두 가지 방식으로 사용합니다.

1.  기존 코드를 손상시키지 않고 타입을 확장하기 위해
2.  대부분의 사용자가 필요하지 않은 특정 경우에 사용자 정의를 허용하기 위해

표준 라이브러리의 `Add` 트레이트는 두 번째 목적의 예입니다. 일반적으로 두 개의 동일한 타입을 더하지만, `Add` 트레이트는 그 이상으로 사용자 정의할 수 있는 기능을 제공합니다. `Add` 트레이트 정의에서 기본 타입 매개변수를 사용하면 대부분의 경우 추가 매개변수를 지정할 필요가 없습니다. 즉, 약간의 구현 보일러플레이트가 필요하지 않아 트레이트를 사용하기가 더 쉬워집니다.

첫 번째 목적은 두 번째 목적과 유사하지만 반대입니다. 기존 트레이트에 타입 매개변수를 추가하려는 경우, 기존 구현 코드를 손상시키지 않고 트레이트의 기능을 확장할 수 있도록 기본값을 제공할 수 있습니다.
