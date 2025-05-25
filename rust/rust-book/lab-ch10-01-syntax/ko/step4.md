# 구조체 정의에서

`<>` 구문을 사용하여 하나 이상의 필드에서 제네릭 타입 매개변수를 사용하도록 구조체를 정의할 수도 있습니다. Listing 10-6 은 모든 타입의 `x` 및 `y` 좌표 값을 저장하기 위해 `Point<T>` 구조체를 정의합니다.

파일 이름: `src/main.rs`

```rust
1 struct Point<T> {
  2 x: T,
  3 y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
}
```

Listing 10-6: 타입 `T`의 `x` 및 `y` 값을 저장하는 `Point<T>` 구조체

구조체 정의에서 제네릭을 사용하는 구문은 함수 정의에서 사용되는 구문과 유사합니다. 먼저 구조체 이름 바로 뒤에 꺾쇠 괄호 안에 타입 매개변수의 이름을 선언합니다 \[1]. 그런 다음 구체적인 데이터 타입을 지정하는 대신 구조체 정의에서 제네릭 타입을 사용합니다 \[23].

`Point<T>`를 정의하기 위해 하나의 제네릭 타입만 사용했기 때문에, 이 정의는 `Point<T>` 구조체가 어떤 타입 `T`에 대해 제네릭이며, `x`와 `y` 필드는 _모두_ 동일한 타입, 즉 어떤 타입이든 될 수 있음을 의미합니다. Listing 10-7 과 같이 서로 다른 타입의 값을 갖는 `Point<T>`의 인스턴스를 생성하면 코드가 컴파일되지 않습니다.

파일 이름: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let wont_work = Point { x: 5, y: 4.0 };
}
```

Listing 10-7: `x`와 `y`는 모두 동일한 제네릭 데이터 타입 `T`를 가지므로 동일한 타입이어야 합니다.

이 예제에서 정수 값 `5`를 `x`에 할당하면, 컴파일러는 이 `Point<T>` 인스턴스에 대해 제네릭 타입 `T`가 정수가 될 것임을 알게 됩니다. 그런 다음 `y`에 대해 `4.0`을 지정하면, `x`와 동일한 타입을 갖도록 정의했으므로 다음과 같은 타입 불일치 오류가 발생합니다.

```bash
error[E0308]: mismatched types
 --> src/main.rs:7:38
  |
7 |     let wont_work = Point { x: 5, y: 4.0 };
  |                                      ^^^ expected integer, found floating-
point number
```

`x`와 `y`가 모두 제네릭이지만 서로 다른 타입을 가질 수 있는 `Point` 구조체를 정의하려면, 여러 제네릭 타입 매개변수를 사용할 수 있습니다. 예를 들어, Listing 10-8 에서 `Point`의 정의를 타입 `T`와 `U`에 대해 제네릭하도록 변경하여 `x`는 타입 `T`이고 `y`는 타입 `U`가 되도록 합니다.

파일 이름: `src/main.rs`

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
}
```

Listing 10-8: `x`와 `y`가 서로 다른 값의 타입이 될 수 있도록 두 개의 타입에 대해 제네릭인 `Point<T, U>`

이제 표시된 모든 `Point` 인스턴스가 허용됩니다! 정의에서 원하는 만큼 많은 제네릭 타입 매개변수를 사용할 수 있지만, 몇 개 이상 사용하면 코드를 읽기 어려워집니다. 코드에 많은 제네릭 타입이 필요하다는 것을 알게 되면, 코드를 더 작은 조각으로 재구성해야 함을 나타낼 수 있습니다.
