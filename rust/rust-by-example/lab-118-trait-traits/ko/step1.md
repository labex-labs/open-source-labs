# 트레이트 (Traits)

`트레이트(trait)`는 알 수 없는 타입인 `Self`에 대해 정의된 메서드의 모음입니다. 트레이트는 동일한 트레이트 내에 선언된 다른 메서드에 접근할 수 있습니다.

트레이트는 모든 데이터 타입에 대해 구현될 수 있습니다. 아래 예제에서는 메서드 그룹인 `Animal`을 정의합니다. 그런 다음 `Animal` `트레이트`는 `Sheep` 데이터 타입에 대해 구현되어 `Sheep`과 함께 `Animal`의 메서드를 사용할 수 있도록 합니다.

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // 연관 함수 시그니처; `Self` 는 구현자 타입을 참조합니다.
    fn new(name: &'static str) -> Self;

    // 메서드 시그니처; 문자열을 반환합니다.
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // 트레이트는 기본 메서드 정의를 제공할 수 있습니다.
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // 구현자 메서드는 구현자의 트레이트 메서드를 사용할 수 있습니다.
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// `Sheep` 에 대한 `Animal` 트레이트를 구현합니다.
impl Animal for Sheep {
    // `Self` 는 구현자 타입입니다: `Sheep`.
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // 기본 트레이트 메서드는 재정의될 수 있습니다.
    fn talk(&self) {
        // 예를 들어, 조용한 묵상을 추가할 수 있습니다.
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // 이 경우 타입 어노테이션이 필요합니다.
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ 타입 어노테이션을 제거해 보세요.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
