# `dyn`을 사용하여 트레이트 반환하기

Rust 컴파일러는 모든 함수의 반환 타입이 얼마나 많은 공간을 필요로 하는지 알아야 합니다. 이는 모든 함수가 구체적인 타입을 반환해야 함을 의미합니다. 다른 언어와 달리, `Animal`과 같은 트레이트가 있는 경우, `Animal`을 반환하는 함수를 작성할 수 없습니다. 왜냐하면, 서로 다른 구현은 서로 다른 양의 메모리를 필요로 하기 때문입니다.

하지만, 쉬운 해결 방법이 있습니다. 트레이트 객체를 직접 반환하는 대신, 함수는 `Animal`을 _포함하는_ `Box`를 반환합니다. `box`는 힙의 메모리에 대한 참조일 뿐입니다. 참조는 정적으로 알려진 크기를 가지며, 컴파일러는 힙에 할당된 `Animal`을 가리킨다는 것을 보장할 수 있으므로, 함수에서 트레이트를 반환할 수 있습니다!

Rust 는 힙에 메모리를 할당할 때마다 가능한 한 명시적으로 하려고 합니다. 따라서 함수가 이 방식으로 힙에 있는 트레이트에 대한 포인터를 반환하는 경우, `dyn` 키워드를 사용하여 반환 타입을 작성해야 합니다. 예를 들어, `Box<dyn Animal>`입니다.

```rust
struct Sheep {}
struct Cow {}

trait Animal {
    // Instance method signature
    fn noise(&self) -> &'static str;
}

// Implement the `Animal` trait for `Sheep`.
impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// Implement the `Animal` trait for `Cow`.
impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// Returns some struct that implements Animal, but we don't know which one at compile time.
fn random_animal(random_number: f64) -> Box<dyn Animal> {
    if random_number < 0.5 {
        Box::new(Sheep {})
    } else {
        Box::new(Cow {})
    }
}

fn main() {
    let random_number = 0.234;
    let animal = random_animal(random_number);
    println!("You've randomly chosen an animal, and it says {}", animal.noise());
}
```
