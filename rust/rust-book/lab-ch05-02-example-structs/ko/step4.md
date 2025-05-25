# 파생 트레이트를 사용하여 유용한 기능 추가

프로그램을 디버깅하는 동안 `Rectangle`의 인스턴스를 출력하고 모든 필드의 값을 볼 수 있으면 유용할 것입니다. Listing 5-11 은 이전 장에서 사용했던 것처럼 `println!` 매크로를 사용하려고 시도합니다. 그러나 이것은 작동하지 않습니다.

파일 이름: `src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {}", rect1);
}
```

Listing 5-11: `Rectangle` 인스턴스 출력을 시도

이 코드를 컴파일하면 다음과 같은 핵심 메시지가 포함된 오류가 발생합니다.

```bash
error[E0277]: `Rectangle` doesn't implement `std::fmt::Display`
```

`println!` 매크로는 다양한 종류의 형식을 지정할 수 있으며, 기본적으로 중괄호는 `println!`에게 `Display`라고 하는 형식을 사용하도록 지시합니다. 이는 최종 사용자에게 직접 소비하기 위한 출력입니다. 지금까지 살펴본 기본 타입은 기본적으로 `Display`를 구현합니다. `1` 또는 다른 기본 타입을 사용자에게 표시하는 방법이 하나뿐이기 때문입니다. 그러나 구조체의 경우 `println!`이 출력을 형식화하는 방법은 더 명확하지 않습니다. 표시 가능성이 더 많기 때문입니다. 쉼표를 원하십니까? 중괄호를 인쇄하시겠습니까? 모든 필드를 표시해야 합니까? 이러한 모호성 때문에 Rust 는 우리가 원하는 것을 추측하려고 하지 않으며, 구조체는 `println!` 및 `{}` 자리 표시자와 함께 사용할 `Display`의 구현을 제공하지 않습니다.

오류를 계속 읽으면 다음과 같은 유용한 메모를 찾을 수 있습니다.

    = help: the trait `std::fmt::Display` is not implemented for `Rectangle`
    = note: in format strings you may be able to use `{:?}` (or {:#?} for
    pretty-print) instead

해봅시다! `println!` 매크로 호출은 이제 `println!("rect1 is {:?}", rect1);`처럼 보일 것입니다. 중괄호 안에 `:?` 지정자를 넣으면 `println!`에게 `Debug`라는 출력 형식을 사용하도록 지시합니다. `Debug` 트레이트를 사용하면 코드를 디버깅하는 동안 값을 볼 수 있도록 개발자에게 유용한 방식으로 구조체를 출력할 수 있습니다.

이 변경 사항으로 코드를 컴파일합니다. 젠장! 여전히 오류가 발생합니다.

```bash
error[E0277]: `Rectangle` doesn't implement `Debug`
```

하지만 다시 컴파일러는 유용한 메모를 제공합니다.

```rust
= help: the trait `Debug` is not implemented for `Rectangle`
= note: add `#[derive(Debug)]` or manually implement `Debug`
```

Rust 는 디버깅 정보를 출력하는 기능을 *포함*하지만, 구조체에 해당 기능을 사용할 수 있도록 명시적으로 옵트인해야 합니다. 이를 위해 Listing 5-12 와 같이 구조체 정의 바로 앞에 외부 속성 `#[derive(Debug)]`를 추가합니다.

파일 이름: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

Listing 5-12: `Debug` 트레이트를 파생하고 디버그 형식을 사용하여 `Rectangle` 인스턴스를 출력하는 속성 추가

이제 프로그램을 실행하면 오류가 발생하지 않으며 다음과 같은 출력을 볼 수 있습니다.

```rust
rect1 is Rectangle { width: 30, height: 50 }
```

좋아요! 가장 예쁜 출력은 아니지만, 이 인스턴스의 모든 필드의 값을 표시하므로 디버깅 중에 확실히 도움이 될 것입니다. 더 큰 구조체가 있는 경우, 출력을 조금 더 쉽게 읽을 수 있는 것이 유용합니다. 이러한 경우 `println!` 문자열에서 `{:?}` 대신 `{:#?}`를 사용할 수 있습니다. 이 예에서 `{:#?}` 스타일을 사용하면 다음과 같이 출력됩니다.

    rect1 is Rectangle {
        width: 30,
        height: 50,
    }

`Debug` 형식을 사용하여 값을 출력하는 또 다른 방법은 `dbg!` 매크로를 사용하는 것입니다. 이 매크로는 표현식의 소유권을 가져와 (참조를 사용하는 `println!`과 반대) 코드에서 해당 `dbg!` 매크로 호출이 발생하는 파일 및 줄 번호와 해당 표현식의 결과 값을 출력하고 값의 소유권을 반환합니다.

> 참고: `dbg!` 매크로를 호출하면 표준 오류 콘솔 스트림 (`stderr`) 에 출력됩니다. `println!`은 표준 출력 콘솔 스트림 (`stdout`) 에 출력됩니다. "표준 출력 대신 표준 오류에 오류 메시지 쓰기"에서 `stderr` 및 `stdout`에 대해 자세히 설명합니다.

다음은 `width` 필드에 할당되는 값과 `rect1`의 전체 구조체 값에 관심이 있는 예입니다.

파일 이름: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

`dbg!`를 표현식 `30 * scale` \[1] 주위에 넣을 수 있으며, `dbg!`는 표현식 값의 소유권을 반환하므로 `width` 필드는 `dbg!` 호출이 없었을 때와 동일한 값을 얻게 됩니다. `dbg!`가 `rect1`의 소유권을 가져가도록 하고 싶지 않으므로 다음 호출에서 `rect1`에 대한 참조를 사용합니다 \[2]. 이 예의 출력은 다음과 같습니다.

    [src/main.rs:10] 30 * scale = 60
    [src/main.rs:14] &rect1 = Rectangle {
        width: 60,
        height: 50,
    }

첫 번째 출력은 \[1]에서 `30 * scale` 표현식을 디버깅하고 결과 값은 `60`입니다 (정수에 대해 구현된 `Debug` 형식은 값만 출력하는 것입니다). \[2]의 `dbg!` 호출은 `Rectangle` 구조체인 `&rect1`의 값을 출력합니다. 이 출력은 `Rectangle` 타입의 예쁜 `Debug` 형식을 사용합니다. `dbg!` 매크로는 코드가 무엇을 하고 있는지 파악하려는 경우 정말 도움이 될 수 있습니다!

`Debug` 트레이트 외에도 Rust 는 사용자 정의 타입에 유용한 동작을 추가할 수 있는 `derive` 속성과 함께 사용할 수 있는 여러 트레이트를 제공했습니다. 해당 트레이트와 해당 동작은 부록 C 에 나열되어 있습니다. 이러한 트레이트를 사용자 지정 동작으로 구현하는 방법과 고유한 트레이트를 만드는 방법을 10 장에서 다룹니다. `derive` 외에도 다른 많은 속성이 있습니다. 자세한 내용은 *https://doc.rust-lang.org/reference/attributes.html*의 Rust 참조의 "속성" 섹션을 참조하십시오.

`area` 함수는 매우 구체적입니다. 직사각형의 면적만 계산합니다. 이 동작을 다른 타입에서는 작동하지 않으므로 `Rectangle` 구조체에 더 가깝게 연결하는 것이 도움이 될 것입니다. `area` 함수를 `Rectangle` 타입에 정의된 `area` *메서드*로 변환하여 이 코드를 계속 리팩토링하는 방법을 살펴보겠습니다.
