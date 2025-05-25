# 동일한 이름을 가진 메서드 간의 모호성 제거

Rust 에서는 트레이트가 다른 트레이트의 메서드와 동일한 이름을 가진 메서드를 갖는 것을 방지하지 않으며, 한 타입에 두 트레이트를 모두 구현하는 것도 방지하지 않습니다. 또한 트레이트의 메서드와 동일한 이름을 가진 메서드를 타입에 직접 구현하는 것도 가능합니다.

동일한 이름을 가진 메서드를 호출할 때, 어떤 메서드를 사용하고 싶은지 Rust 에 알려줘야 합니다. Listing 19-16 의 코드를 살펴보겠습니다. 여기서는 `fly`라는 메서드를 모두 가진 `Pilot`와 `Wizard`라는 두 개의 트레이트를 정의했습니다. 그런 다음, 이미 `fly`라는 메서드가 구현된 `Human` 타입에 두 트레이트를 모두 구현합니다. 각 `fly` 메서드는 서로 다른 작업을 수행합니다.

Filename: `src/main.rs`

```rust
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}
```

Listing 19-16: `fly` 메서드를 갖도록 정의된 두 개의 트레이트가 `Human` 타입에 구현되었으며, `fly` 메서드가 `Human`에 직접 구현되었습니다.

`Human`의 인스턴스에서 `fly`를 호출하면, 컴파일러는 Listing 19-17 과 같이 타입에 직접 구현된 메서드를 호출하는 것을 기본으로 합니다.

Filename: `src/main.rs`

```rust
fn main() {
    let person = Human;
    person.fly();
}
```

Listing 19-17: `Human`의 인스턴스에서 `fly` 호출

이 코드를 실행하면 `*waving arms furiously*`가 출력되어 Rust 가 `Human`에 직접 구현된 `fly` 메서드를 호출했음을 보여줍니다.

`Pilot` 트레이트 또는 `Wizard` 트레이트에서 `fly` 메서드를 호출하려면, 어떤 `fly` 메서드를 의미하는지 지정하기 위해 더 명시적인 구문을 사용해야 합니다. Listing 19-18 은 이 구문을 보여줍니다.

Filename: `src/main.rs`

```rust
fn main() {
    let person = Human;
    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

Listing 19-18: 호출하려는 트레이트의 `fly` 메서드 지정

메서드 이름 앞에 트레이트 이름을 지정하면 Rust 가 호출하려는 `fly`의 구현을 명확하게 알 수 있습니다. `Human::fly(&person)`을 작성할 수도 있습니다. 이는 Listing 19-18 에서 사용한 `person.fly()`와 동일하지만, 모호성을 제거할 필요가 없다면 작성하는 데 약간 더 깁니다.

이 코드를 실행하면 다음과 같이 출력됩니다.

    This is your captain speaking.
    Up!
    *waving arms furiously*

`fly` 메서드가 `self` 매개변수를 사용하기 때문에, 두 개의 *타입*이 모두 하나의 *트레이트*를 구현하는 경우, Rust 는 `self`의 타입을 기반으로 사용할 트레이트의 구현을 파악할 수 있습니다.

그러나 메서드가 아닌 연관 함수에는 `self` 매개변수가 없습니다. 동일한 함수 이름을 가진 비 메서드 함수를 정의하는 여러 타입 또는 트레이트가 있는 경우, 완전한 정규화된 구문을 사용하지 않으면 Rust 는 어떤 타입을 의미하는지 항상 알지 못합니다. 예를 들어, Listing 19-19 에서 모든 강아지 이름을 Spot 으로 지정하려는 동물 보호소에 대한 트레이트를 만듭니다. `baby_name`이라는 연관 비 메서드 함수가 있는 `Animal` 트레이트를 만듭니다. `Animal` 트레이트는 `Dog` 구조체에 대해 구현되며, 여기에도 `baby_name` 연관 비 메서드 함수를 직접 제공합니다.

Filename: `src/main.rs`

```rust
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("A baby dog is called a {}", Dog::baby_name());
}
```

Listing 19-19: 동일한 이름을 가진 연관 함수와 트레이트를 구현하는 연관 함수를 가진 타입이 있는 트레이트

모든 강아지 이름을 Spot 으로 지정하는 코드를 `Dog`에 정의된 `baby_name` 연관 함수에 구현합니다. `Dog` 타입은 또한 모든 동물이 갖는 특성을 설명하는 `Animal` 트레이트를 구현합니다. 강아지는 puppy 라고 불리며, 이는 `Animal` 트레이트의 `Dog`에 대한 구현에서 `Animal` 트레이트와 관련된 `baby_name` 함수로 표현됩니다.

`main`에서 `Dog::baby_name` 함수를 호출하면, `Dog`에 직접 정의된 연관 함수가 호출됩니다. 이 코드는 다음을 출력합니다.

```rust
A baby dog is called a Spot
```

이 출력은 우리가 원하는 것이 아닙니다. `Dog`에 구현된 `Animal` 트레이트의 일부인 `baby_name` 함수를 호출하여 코드가 `A baby dog is called a puppy`를 출력하도록 하려고 합니다. Listing 19-18 에서 사용한 트레이트 이름을 지정하는 기술은 여기서는 도움이 되지 않습니다. Listing 19-20 의 코드로 `main`을 변경하면 컴파일 오류가 발생합니다.

Filename: `src/main.rs`

```rust
fn main() {
    println!("A baby dog is called a {}", Animal::baby_name());
}
```

Listing 19-20: `Animal` 트레이트에서 `baby_name` 함수를 호출하려고 시도하지만, Rust 는 어떤 구현을 사용할지 알 수 없습니다.

`Animal::baby_name`에는 `self` 매개변수가 없고, `Animal` 트레이트를 구현하는 다른 타입이 있을 수 있으므로, Rust 는 어떤 `Animal::baby_name` 구현을 원하는지 파악할 수 없습니다. 다음과 같은 컴파일러 오류가 발생합니다.

```bash
error[E0283]: type annotations needed
  --> src/main.rs:20:43
   |
20 |     println!("A baby dog is called a {}", Animal::baby_name());
   |                                           ^^^^^^^^^^^^^^^^^ cannot infer
type
   |
   = note: cannot satisfy `_: Animal`
```

모호성을 제거하고 다른 타입에 대한 `Animal` 구현이 아닌 `Dog`에 대한 `Animal` 구현을 사용하려는 것을 Rust 에 알리려면, 완전한 정규화된 구문을 사용해야 합니다. Listing 19-21 은 완전한 정규화된 구문을 사용하는 방법을 보여줍니다.

Filename: `src/main.rs`

```rust
fn main() {
    println!(
        "A baby dog is called a {}",
        <Dog as Animal>::baby_name()
    );
}
```

Listing 19-21: `Dog`에 구현된 `Animal` 트레이트에서 `baby_name` 함수를 호출하려는 것을 지정하기 위해 완전한 정규화된 구문 사용

꺽쇠 괄호 안에 타입 주석을 제공하여, 이 함수 호출에 대해 `Dog` 타입을 `Animal`로 취급하겠다고 말함으로써 `Dog`에 구현된 `Animal` 트레이트에서 `baby_name` 메서드를 호출하려는 것을 Rust 에 나타냅니다. 이 코드는 이제 우리가 원하는 것을 출력합니다.

```rust
A baby dog is called a puppy
```

일반적으로 완전한 정규화된 구문은 다음과 같이 정의됩니다.

```rust
<Type as Trait>::function(receiver_if_method, next_arg, ...);
```

메서드가 아닌 연관 함수의 경우, `receiver`가 없습니다. 다른 인수의 목록만 있을 것입니다. 함수 또는 메서드를 호출하는 모든 곳에서 완전한 정규화된 구문을 사용할 수 있습니다. 그러나 Rust 가 프로그램의 다른 정보에서 파악할 수 있는 이 구문의 모든 부분을 생략할 수 있습니다. 동일한 이름을 사용하는 여러 구현이 있고 Rust 가 호출하려는 구현을 식별하는 데 도움이 필요한 경우에만 이 더 자세한 구문을 사용해야 합니다.
